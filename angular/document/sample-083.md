# #083 Lifecycle でのリソース解放

## 概要
Angular v20におけるLifecycle Hooksでのリソース解放を学びます。適切なリソース管理により、メモリリークを防ぎ安定したアプリケーションを構築する方法について解説します。

## 学習目標
- リソース解放の重要性を理解する
- 適切なリソース管理方法を習得する
- 包括的なクリーンアップパターンを身につける

## 📺 画面表示用コード

```typescript
// 包括的なリソース解放
export class ResourceManagementComponent implements OnInit, OnDestroy {
  private resources = new ResourceManager();
  
  ngOnInit() {
    this.initializeResources();
  }
  
  ngOnDestroy() {
    this.resources.cleanup();
  }
  
  private initializeResources() {
    // Subscription
    this.resources.addSubscription(
      this.dataService.getData().subscribe()
    );
    
    // タイマー
    this.resources.addTimer(
      setInterval(() => this.update(), 1000)
    );
    
    // イベントリスナー
    this.resources.addEventListener(
      'resize', this.onResize.bind(this)
    );
  }
}
```

```typescript
// 手動リソース管理
export class ManualResourceComponent implements OnInit, OnDestroy {
  private subscription = new Subscription();
  private timers: number[] = [];
  private eventListeners = new Map<string, () => void>();
  
  ngOnInit() {
    this.initializeResources();
  }
  
  ngOnDestroy() {
    this.cleanupAllResources();
  }
  
  private cleanupAllResources() {
    this.subscription.unsubscribe();
    this.timers.forEach(timer => {
      clearTimeout(timer);
      clearInterval(timer);
    });
    this.eventListeners.forEach((listener, event) => {
      window.removeEventListener(event, listener);
    });
  }
}
```

## 技術ポイント

### 1. リソース解放の重要性
- **メモリリークの防止**: 適切なリソース解放によりメモリリークを防ぐ
- **パフォーマンス向上**: 不要なリソースの解放によるパフォーマンス向上
- **アプリケーションの安定性**: 予期しない動作の防止

### 2. リソースの種類
- **Subscription**: Observableの購読
- **タイマー**: setTimeout/setInterval
- **イベントリスナー**: DOMイベント
- **WebSocket**: 接続
- **ファイルハンドル**: ファイル操作

### 3. 管理パターン
- **集約管理**: 複数リソースの集約管理
- **自動管理**: 自動的なリソース解放
- **手動管理**: 個別のリソース管理

## 実践的な活用例

### 1. リソースマネージャーの実装
```typescript
class ResourceManager {
  private subscriptions = new Set<Subscription>();
  private timers = new Set<number>();
  private eventListeners = new Map<string, () => void>();
  
  addSubscription(subscription: Subscription) {
    this.subscriptions.add(subscription);
  }
  
  addTimer(timer: number) {
    this.timers.add(timer);
  }
  
  addEventListener(event: string, listener: () => void) {
    this.eventListeners.set(event, listener);
    window.addEventListener(event, listener);
  }
  
  cleanup() {
    this.subscriptions.forEach(sub => sub.unsubscribe());
    this.timers.forEach(timer => {
      clearTimeout(timer);
      clearInterval(timer);
    });
    this.eventListeners.forEach((listener, event) => {
      window.removeEventListener(event, listener);
    });
  }
}
```

### 2. サービスでのリソース管理
```typescript
@Injectable()
export class DataService implements OnDestroy {
  private resources = new ResourceManager();
  
  getData() {
    return this.http.get('/api/data').pipe(
      takeUntil(this.destroy$)
    );
  }
  
  ngOnDestroy() {
    this.resources.cleanup();
  }
}
```

### 3. コンポーネントでの包括的管理
```typescript
export class ComprehensiveComponent implements OnInit, OnDestroy {
  private resources = new ResourceManager();
  
  ngOnInit() {
    this.setupAllResources();
  }
  
  ngOnDestroy() {
    this.resources.cleanup();
  }
  
  private setupAllResources() {
    // データ購読
    this.resources.addSubscription(
      this.dataService.getData().subscribe()
    );
    
    // 定期的な更新
    this.resources.addTimer(
      setInterval(() => this.updateData(), 5000)
    );
    
    // ウィンドウイベント
    this.resources.addEventListener(
      'resize', this.onWindowResize.bind(this)
    );
    
    // キーボードイベント
    this.resources.addEventListener(
      'keydown', this.onKeyDown.bind(this)
    );
  }
}
```

## ベストプラクティス

1. **包括的な管理**: 全てのリソースを適切に管理
2. **自動化**: 自動的なリソース解放の活用
3. **早期解放**: 不要になった時点での即座な解放
4. **監視**: リソース使用量の監視

## 注意点

- 全てのリソースを適切に解放
- メモリリークの早期発見
- 適切なタイミングでの解放
- パフォーマンスへの影響を考慮

## 関連技術
- メモリ管理
- リソース管理
- パフォーマンス最適化
- 自動クリーンアップ
