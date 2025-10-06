# #234 「動的ローディング実装」

## 概要
動的ローディングは、データ取得やリソース読み込みの進捗を表示しながらコンポーネントを動的に生成する技術です。loading、success、errorの状態を管理し、それぞれに応じた適切なコンポーネントを表示することで、優れたUXを実現できます。

## 学習目標
- ローディング状態の管理方法を習得する
- 非同期データ取得と動的コンポーネント生成の統合を理解する
- エラーハンドリングを含む堅牢な実装方法を学ぶ

## 技術ポイント
- **状態管理**: loading/success/error の3状態
- **非同期処理**: async/awaitとの統合
- **UI切り替え**: 状態に応じたコンポーネント表示

## 📺 画面表示用コード

### 基本的なローディング実装
```typescript
export class LoadingHost {
  private container = inject(ViewContainerRef);
  loading = signal(false);

  async loadComponent() {
    this.loading.set(true);
    const data = await this.fetchData();
    this.loading.set(false);

    const ref = this.container.createComponent(DataComponent);
    ref.setInput('data', data);
  }
}
```

### 3状態管理パターン
```typescript
type LoadState = 'idle' | 'loading' | 'success' | 'error';

export class StateManagementHost {
  private container = inject(ViewContainerRef);
  state = signal<LoadState>('idle');

  async load() {
    this.state.set('loading');
    try {
      const data = await this.fetchData();
      this.state.set('success');
      this.showContent(data);
    } catch (error) {
      this.state.set('error');
      this.showError(error);
    }
  }
}
```

### ローディングコンポーネント表示
```typescript
async loadWithSpinner() {
  const spinner = this.container.createComponent(SpinnerComponent);

  try {
    const data = await this.fetchData();
    spinner.destroy();
    const content = this.container.createComponent(ContentComponent);
    content.setInput('data', data);
  } catch (error) {
    spinner.destroy();
    this.container.createComponent(ErrorComponent);
  }
}
```

## 実践的な活用例

### 完全なローディングシステム
```typescript
interface LoadingState<T> {
  status: 'idle' | 'loading' | 'success' | 'error';
  data?: T;
  error?: Error;
}

@Injectable()
export class DynamicLoader {
  private container = inject(ViewContainerRef);
  private state = signal<LoadingState<any>>({ status: 'idle' });

  async load<T>(
    fetcher: () => Promise<T>,
    componentType: Type<any>
  ): Promise<void> {
    this.state.update(s => ({ ...s, status: 'loading' }));
    this.showLoading();

    try {
      const data = await fetcher();
      this.state.set({ status: 'success', data });
      this.showContent(componentType, data);
    } catch (error) {
      this.state.set({
        status: 'error',
        error: error instanceof Error ? error : new Error(String(error))
      });
      this.showError(this.state().error!);
    }
  }

  private showLoading() {
    this.container.clear();
    this.container.createComponent(LoadingSpinnerComponent);
  }

  private showContent(componentType: Type<any>, data: any) {
    this.container.clear();
    const ref = this.container.createComponent(componentType);
    ref.setInput('data', data);
  }

  private showError(error: Error) {
    this.container.clear();
    const ref = this.container.createComponent(ErrorDisplayComponent);
    ref.setInput('error', error);
  }
}
```

### プログレスバー付きローディング
```typescript
@Component({
  selector: 'app-progress-loader',
  template: `
    @if (progress() < 100) {
      <div class="progress">
        <div class="bar" [style.width.%]="progress()"></div>
        <p>{{ progress() }}% 読み込み中...</p>
      </div>
    }
    <ng-container #content></ng-container>
  `
})
export class ProgressLoaderComponent {
  @ViewChild('content', { read: ViewContainerRef })
  container!: ViewContainerRef;

  progress = signal(0);

  async loadWithProgress(urls: string[]) {
    const total = urls.length;
    const results: any[] = [];

    for (let i = 0; i < urls.length; i++) {
      const data = await fetch(urls[i]).then(r => r.json());
      results.push(data);
      this.progress.set(Math.round(((i + 1) / total) * 100));
    }

    // 完了後、コンテンツを表示
    const ref = this.container.createComponent(DataListComponent);
    ref.setInput('items', results);
  }
}
```

### リトライ機能付きローダー
```typescript
@Injectable()
export class RetryableLoader {
  private container = inject(ViewContainerRef);

  async loadWithRetry<T>(
    fetcher: () => Promise<T>,
    componentType: Type<any>,
    maxRetries = 3
  ): Promise<void> {
    let lastError: Error | null = null;

    for (let attempt = 1; attempt <= maxRetries; attempt++) {
      try {
        // リトライ表示
        this.showRetryStatus(attempt, maxRetries);

        const data = await fetcher();

        // 成功時、コンテンツを表示
        this.container.clear();
        const ref = this.container.createComponent(componentType);
        ref.setInput('data', data);
        return;

      } catch (error) {
        lastError = error instanceof Error ? error : new Error(String(error));
        console.warn(`Attempt ${attempt} failed:`, lastError);

        if (attempt < maxRetries) {
          // 次のリトライまで待機
          await new Promise(resolve => setTimeout(resolve, 1000 * attempt));
        }
      }
    }

    // 全てのリトライ失敗
    this.showRetryError(lastError!, maxRetries);
  }

  private showRetryStatus(attempt: number, max: number) {
    this.container.clear();
    const ref = this.container.createComponent(RetryStatusComponent);
    ref.setInput('attempt', attempt);
    ref.setInput('maxAttempts', max);
  }

  private showRetryError(error: Error, maxRetries: number) {
    this.container.clear();
    const ref = this.container.createComponent(RetryErrorComponent);
    ref.setInput('error', error);
    ref.setInput('attempts', maxRetries);
  }
}
```

### スケルトンスクリーン実装
```typescript
@Component({
  selector: 'app-skeleton-loader',
  template: `
    <ng-container #skeletonContainer></ng-container>
    <ng-container #contentContainer></ng-container>
  `
})
export class SkeletonLoaderComponent {
  @ViewChild('skeletonContainer', { read: ViewContainerRef })
  skeletonContainer!: ViewContainerRef;

  @ViewChild('contentContainer', { read: ViewContainerRef })
  contentContainer!: ViewContainerRef;

  async loadWithSkeleton(
    skeletonType: Type<any>,
    contentType: Type<any>,
    fetcher: () => Promise<any>
  ) {
    // スケルトン表示
    const skeleton = this.skeletonContainer.createComponent(skeletonType);

    try {
      const data = await fetcher();

      // スケルトンをフェードアウト
      const element = skeleton.location.nativeElement;
      element.style.transition = 'opacity 0.3s';
      element.style.opacity = '0';

      await new Promise(resolve => setTimeout(resolve, 300));
      skeleton.destroy();

      // コンテンツをフェードイン
      const content = this.contentContainer.createComponent(contentType);
      content.setInput('data', data);

      const contentEl = content.location.nativeElement;
      contentEl.style.opacity = '0';
      contentEl.style.transition = 'opacity 0.3s';
      requestAnimationFrame(() => {
        contentEl.style.opacity = '1';
      });

    } catch (error) {
      skeleton.destroy();
      const errorComp = this.contentContainer.createComponent(ErrorComponent);
      errorComp.setInput('error', error);
    }
  }
}
```

### キャッシュ機能付きローダー
```typescript
@Injectable()
export class CachedLoader {
  private container = inject(ViewContainerRef);
  private cache = new Map<string, { data: any; timestamp: number }>();
  private cacheDuration = 5 * 60 * 1000; // 5分

  async load(
    key: string,
    fetcher: () => Promise<any>,
    componentType: Type<any>
  ) {
    // キャッシュチェック
    const cached = this.cache.get(key);
    const now = Date.now();

    if (cached && (now - cached.timestamp) < this.cacheDuration) {
      // キャッシュヒット
      console.log('Using cached data');
      this.showContent(componentType, cached.data);
      return;
    }

    // ローディング表示
    this.container.clear();
    this.container.createComponent(LoadingComponent);

    try {
      const data = await fetcher();

      // キャッシュに保存
      this.cache.set(key, { data, timestamp: now });

      this.showContent(componentType, data);
    } catch (error) {
      this.showError(error);
    }
  }

  private showContent(componentType: Type<any>, data: any) {
    this.container.clear();
    const ref = this.container.createComponent(componentType);
    ref.setInput('data', data);
  }

  private showError(error: any) {
    this.container.clear();
    const ref = this.container.createComponent(ErrorComponent);
    ref.setInput('error', error);
  }

  clearCache(key?: string) {
    if (key) {
      this.cache.delete(key);
    } else {
      this.cache.clear();
    }
  }
}
```

### 並行ローディング
```typescript
export class ParallelLoader {
  private container = inject(ViewContainerRef);

  async loadParallel(
    loaders: Array<{
      fetcher: () => Promise<any>;
      component: Type<any>;
    }>
  ) {
    // 全てローディング表示
    const loadingRefs = loaders.map(() =>
      this.container.createComponent(LoadingComponent)
    );

    try {
      // 並行でデータ取得
      const results = await Promise.all(
        loaders.map(l => l.fetcher())
      );

      // ローディングを削除
      loadingRefs.forEach(ref => ref.destroy());

      // 全てのコンテンツを表示
      results.forEach((data, index) => {
        const ref = this.container.createComponent(loaders[index].component);
        ref.setInput('data', data);
      });

    } catch (error) {
      loadingRefs.forEach(ref => ref.destroy());
      this.container.createComponent(ErrorComponent);
    }
  }
}
```

## ベストプラクティス

### エラーハンドリングの徹底
```typescript
// ✅ 詳細なエラー情報を表示
catch (error) {
  const ref = this.container.createComponent(ErrorComponent);
  ref.setInput('error', error);
  ref.setInput('retryHandler', () => this.load());
}

// ❌ エラーを無視
catch (error) {
  console.error(error); // ユーザーに伝わらない
}
```

### ローディング状態のクリア
```typescript
// ✅ 確実にクリア
try {
  // ...
} finally {
  this.loading.set(false);
  spinner?.destroy();
}
```

### タイムアウト処理
```typescript
async loadWithTimeout(fetcher: () => Promise<any>, timeout = 10000) {
  const timeoutPromise = new Promise((_, reject) =>
    setTimeout(() => reject(new Error('Timeout')), timeout)
  );

  try {
    const data = await Promise.race([fetcher(), timeoutPromise]);
    // ...
  } catch (error) {
    // タイムアウトまたはエラー処理
  }
}
```

## 注意点

### メモリリーク防止
ローディングコンポーネントは必ず削除してください。特にエラー時のクリーンアップを忘れずに。

### 競合状態の回避
連続してload()を呼ぶ場合、前回のローディングをキャンセルする仕組みが必要です。

### UXの考慮
短時間で完了する処理には、ローディング表示を遅延させることで、画面のちらつきを防げます。

### パフォーマンス
大量のデータローディングでは、仮想スクロールやページネーションの併用を検討してください。

## 関連技術
- **Signal**: 状態管理
- **async/await**: 非同期処理
- **Promise**: 非同期操作
- **RxJS**: リアクティブなローディング管理
- **スケルトンスクリーン**: UXパターン
