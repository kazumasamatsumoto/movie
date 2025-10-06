# #233 「動的 Component のライフサイクル」

## 概要
動的に生成されたコンポーネントも、通常のコンポーネントと同じライフサイクルフックが実行されます。ただし生成タイミングが動的なため、親コンポーネントのライフサイクルとは独立して動作します。適切なタイミングでの初期化と破棄が重要です。

## 学習目標
- 動的コンポーネントのライフサイクルを理解する
- フック実行のタイミングを把握する
- ライフサイクルを活用した初期化・破棄処理を実装できる

## 技術ポイント
- **ngOnInit**: createComponent()直後に実行
- **ngOnDestroy**: destroy()時に実行
- **独立したライフサイクル**: 親とは独立して動作

## 📺 画面表示用コード

### ライフサイクルフックの実行
```typescript
@Component({
  selector: 'app-dynamic'
})
export class DynamicComponent implements OnInit, OnDestroy {
  ngOnInit() {
    console.log('Dynamic: ngOnInit');
  }

  ngOnDestroy() {
    console.log('Dynamic: ngOnDestroy');
  }
}

// 生成時
const ref = this.container.createComponent(DynamicComponent);
// → ngOnInit が実行される

// 破棄時
ref.destroy();
// → ngOnDestroy が実行される
```

### 初期化処理の実装
```typescript
@Component({
  selector: 'app-data-loader'
})
export class DataLoaderComponent implements OnInit {
  data = signal<any[]>([]);

  ngOnInit() {
    // 動的生成時に自動的にデータ取得
    this.loadData();
  }

  async loadData() {
    const response = await fetch('/api/data');
    this.data.set(await response.json());
  }
}
```

### クリーンアップ処理
```typescript
@Component({
  selector: 'app-subscription'
})
export class SubscriptionComponent implements OnInit, OnDestroy {
  private subscription?: Subscription;

  ngOnInit() {
    this.subscription = interval(1000).subscribe(n => {
      console.log(n);
    });
  }

  ngOnDestroy() {
    // 購読を確実に解除
    this.subscription?.unsubscribe();
  }
}
```

## 実践的な活用例

### 完全なライフサイクル実装
```typescript
@Component({
  selector: 'app-lifecycle-demo',
  template: `<p>{{ message() }}</p>`
})
export class LifecycleDemoComponent implements
  OnInit, AfterViewInit, OnDestroy {

  message = signal('初期化前');

  constructor() {
    console.log('1. Constructor');
  }

  ngOnInit() {
    console.log('2. ngOnInit');
    this.message.set('初期化完了');
  }

  ngAfterViewInit() {
    console.log('3. ngAfterViewInit');
  }

  ngOnDestroy() {
    console.log('4. ngOnDestroy');
    this.message.set('破棄済み');
  }
}

// ホストコンポーネント
export class HostComponent {
  private container = inject(ViewContainerRef);

  create() {
    console.log('0. createComponent開始');
    const ref = this.container.createComponent(LifecycleDemoComponent);
    console.log('5. createComponent完了');
    return ref;
  }

  destroy(ref: ComponentRef<LifecycleDemoComponent>) {
    console.log('6. destroy開始');
    ref.destroy();
    console.log('7. destroy完了');
  }
}
```

### 非同期初期化パターン
```typescript
@Component({
  selector: 'app-async-init',
  template: `
    @if (loading()) {
      <p>読み込み中...</p>
    } @else if (error()) {
      <p>エラー: {{ error() }}</p>
    } @else {
      <p>データ: {{ data() }}</p>
    }
  `
})
export class AsyncInitComponent implements OnInit {
  loading = signal(true);
  error = signal<string | null>(null);
  data = signal<any>(null);

  ngOnInit() {
    this.initializeAsync();
  }

  private async initializeAsync() {
    try {
      const response = await fetch('/api/data');
      const data = await response.json();
      this.data.set(data);
    } catch (err) {
      this.error.set(err instanceof Error ? err.message : '不明なエラー');
    } finally {
      this.loading.set(false);
    }
  }
}
```

### リソース管理パターン
```typescript
@Component({
  selector: 'app-resource-manager'
})
export class ResourceManagerComponent implements OnInit, OnDestroy {
  private destroyRef = inject(DestroyRef);
  private resources: Array<() => void> = [];

  ngOnInit() {
    // WebSocket接続
    const ws = new WebSocket('ws://example.com');
    this.resources.push(() => ws.close());

    // タイマー
    const timer = setInterval(() => console.log('tick'), 1000);
    this.resources.push(() => clearInterval(timer));

    // イベントリスナー
    const handler = () => console.log('resize');
    window.addEventListener('resize', handler);
    this.resources.push(() => window.removeEventListener('resize', handler));

    // または DestroyRef を使用
    this.destroyRef.onDestroy(() => {
      console.log('DestroyRef: クリーンアップ');
    });
  }

  ngOnDestroy() {
    // 全リソースを解放
    this.resources.forEach(cleanup => cleanup());
    this.resources = [];
  }
}
```

### 遅延初期化パターン
```typescript
@Component({
  selector: 'app-lazy-init'
})
export class LazyInitComponent {
  private initialized = false;
  data = signal<any>(null);

  // ngOnInit ではなく明示的に初期化
  initialize(config: any) {
    if (this.initialized) return;

    console.log('初期化:', config);
    this.data.set(config);
    this.initialized = true;
  }
}

// ホスト側
export class HostComponent {
  create() {
    const ref = this.container.createComponent(LazyInitComponent);

    // 生成後、任意のタイミングで初期化
    setTimeout(() => {
      ref.instance.initialize({ id: 1, name: 'Test' });
    }, 1000);

    return ref;
  }
}
```

### ライフサイクルフックのインターセプト
```typescript
export class LifecycleInterceptor {
  private container = inject(ViewContainerRef);

  createWithHooks<T>(componentType: Type<T>) {
    const ref = this.container.createComponent(componentType);

    // ngOnInit のラッピング
    const originalInit = ref.instance.ngOnInit;
    if (originalInit) {
      ref.instance.ngOnInit = () => {
        console.log('Before ngOnInit');
        originalInit.call(ref.instance);
        console.log('After ngOnInit');
      };
    }

    // ngOnDestroy のラッピング
    const originalDestroy = ref.instance.ngOnDestroy;
    if (originalDestroy) {
      ref.instance.ngOnDestroy = () => {
        console.log('Before ngOnDestroy');
        originalDestroy.call(ref.instance);
        console.log('After ngOnDestroy');
      };
    }

    return ref;
  }
}
```

### 状態管理との統合
```typescript
@Injectable()
export class ComponentStateService {
  private states = new Map<string, any>();

  save(id: string, state: any) {
    this.states.set(id, state);
  }

  restore(id: string): any {
    return this.states.get(id);
  }

  delete(id: string) {
    this.states.delete(id);
  }
}

@Component({
  selector: 'app-stateful'
})
export class StatefulComponent implements OnInit, OnDestroy {
  private stateService = inject(ComponentStateService);
  private componentId = crypto.randomUUID();

  state = signal({ count: 0, text: '' });

  ngOnInit() {
    // 状態を復元
    const savedState = this.stateService.restore(this.componentId);
    if (savedState) {
      this.state.set(savedState);
    }
  }

  ngOnDestroy() {
    // 状態を保存
    this.stateService.save(this.componentId, this.state());
  }
}
```

### エラーハンドリング
```typescript
@Component({
  selector: 'app-safe-init'
})
export class SafeInitComponent implements OnInit, OnDestroy {
  private errorHandler = inject(ErrorHandler);

  ngOnInit() {
    try {
      this.initialize();
    } catch (error) {
      this.errorHandler.handleError(error);
      throw error; // 再スロー
    }
  }

  private initialize() {
    // 初期化処理（エラーが発生する可能性あり）
    const data = JSON.parse(localStorage.getItem('config') || '{}');
    // ...
  }

  ngOnDestroy() {
    try {
      this.cleanup();
    } catch (error) {
      console.error('クリーンアップエラー:', error);
      // エラーを握りつぶす（破棄は継続）
    }
  }

  private cleanup() {
    // クリーンアップ処理
  }
}
```

## ベストプラクティス

### DestroyRefの活用
```typescript
// ✅ DestroyRef を使った自動クリーンアップ
export class ModernComponent {
  private destroyRef = inject(DestroyRef);

  ngOnInit() {
    interval(1000)
      .pipe(takeUntilDestroyed(this.destroyRef))
      .subscribe(n => console.log(n));
  }
}

// ❌ 手動管理は漏れやすい
export class LegacyComponent implements OnDestroy {
  private sub?: Subscription;

  ngOnInit() {
    this.sub = interval(1000).subscribe(n => console.log(n));
  }

  ngOnDestroy() {
    this.sub?.unsubscribe(); // 忘れる可能性
  }
}
```

### 初期化の確実性
```typescript
// ✅ ngOnInit で初期化
ngOnInit() {
  this.loadData(); // 確実に実行される
}

// ❌ コンストラクタでの非同期処理
constructor() {
  this.loadData(); // 推奨されない
}
```

### クリーンアップの徹底
```typescript
ngOnDestroy() {
  // 全てのリソースを解放
  this.subscriptions.forEach(s => s.unsubscribe());
  this.timers.forEach(t => clearInterval(t));
  this.listeners.forEach(l => l.remove());
}
```

## 注意点

### ngOnInit の実行タイミング
`createComponent()`直後に`ngOnInit()`が同期的に実行されます。重い処理は避け、非同期化を検討してください。

### 親子関係の独立性
動的コンポーネントは親のライフサイクルに依存しません。親が破棄されても自動的には破棄されないため、明示的な管理が必要です。

### AfterViewInit のタイミング
`ngAfterViewInit()`は、ビューがDOMに挿入された後に実行されます。DOM操作はこのフック以降で行ってください。

### 破棄後のアクセス
`destroy()`後は、そのコンポーネントインスタンスへのアクセスは避けてください。エラーや予期しない動作の原因になります。

## 関連技術
- **OnInit/OnDestroy**: ライフサイクルインターフェース
- **DestroyRef**: 破棄イベントの検知
- **takeUntilDestroyed**: 自動購読解除オペレータ
- **AfterViewInit**: ビュー初期化フック
- **ChangeDetectorRef**: 変更検知制御
