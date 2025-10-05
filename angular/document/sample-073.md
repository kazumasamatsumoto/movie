# #073 ngOnDestroy でのメモリリーク対策

## 概要
Angular v20におけるngOnDestroyでのメモリリーク対策を学びます。適切なリソース解放により、メモリリークを防ぎ安定したアプリケーションを構築する方法について解説します。

## 学習目標
- メモリリークの原因を理解する
- 適切なリソース解放方法を習得する
- 自動購読解除の仕組みを身につける

## 📺 画面表示用コード

```typescript
// メモリリーク対策の実装
export class MemoryLeakPreventionComponent implements OnDestroy {
  private subscription = new Subscription();
  private timer?: number;
  
  ngOnInit() {
    // 複数のSubscriptionを管理
    this.subscription.add(
      this.dataService.getData().subscribe()
    );
    
    this.timer = setInterval(() => {
      this.updateData();
    }, 1000);
  }
  
  ngOnDestroy() {
    // 全てのリソースを解放
    this.subscription.unsubscribe();
    if (this.timer) {
      clearInterval(this.timer);
    }
  }
}
```

```typescript
// takeUntilパターンの使用
export class TakeUntilComponent implements OnDestroy {
  private destroy$ = new Subject<void>();
  
  ngOnInit() {
    this.dataService.getData()
      .pipe(takeUntil(this.destroy$))
      .subscribe(data => {
        // データ処理
      });
  }
  
  ngOnDestroy() {
    this.destroy$.next();
    this.destroy$.complete();
  }
}
```

## 技術ポイント

### 1. メモリリークの原因
- **Subscription**: Observableの購読解除忘れ
- **タイマー**: setInterval/setTimeoutのクリア忘れ
- **イベントリスナー**: DOMイベントの削除忘れ
- **WebSocket**: 接続の切断忘れ

### 2. 適切なリソース解放
- Subscriptionの購読解除
- タイマーのクリア
- イベントリスナーの削除
- WebSocket接続の切断

### 3. 自動購読解除
- `takeUntil`オペレーター
- `Subscription`の集約管理
- 自動クリーンアップパターン

## 実践的な活用例

### 1. Subscriptionの集約管理
```typescript
export class SubscriptionManagerComponent implements OnDestroy {
  private subscriptions = new Subscription();
  
  ngOnInit() {
    this.subscriptions.add(
      this.userService.getUser().subscribe()
    );
    this.subscriptions.add(
      this.dataService.getData().subscribe()
    );
    this.subscriptions.add(
      this.configService.getConfig().subscribe()
    );
  }
  
  ngOnDestroy() {
    this.subscriptions.unsubscribe();
  }
}
```

### 2. takeUntilパターン
```typescript
export class TakeUntilPatternComponent implements OnDestroy {
  private destroy$ = new Subject<void>();
  
  ngOnInit() {
    // 複数のObservableを自動購読解除
    this.dataService.getData()
      .pipe(takeUntil(this.destroy$))
      .subscribe();
      
    this.userService.getUser()
      .pipe(takeUntil(this.destroy$))
      .subscribe();
  }
  
  ngOnDestroy() {
    this.destroy$.next();
    this.destroy$.complete();
  }
}
```

### 3. 包括的なリソース管理
```typescript
export class ComprehensiveResourceComponent implements OnDestroy {
  private resources = new ResourceManager();
  
  ngOnInit() {
    this.resources.addSubscription(
      this.dataService.getData().subscribe()
    );
    this.resources.addTimer(
      setInterval(() => this.update(), 1000)
    );
    this.resources.addEventListener(
      'resize', this.onResize.bind(this)
    );
  }
  
  ngOnDestroy() {
    this.resources.cleanup();
  }
}
```

## ベストプラクティス

1. **包括的なクリーンアップ**: 全てのリソースを適切に解放
2. **自動化**: takeUntilパターンなどの自動化手法の活用
3. **集約管理**: リソースの集約的な管理
4. **監視**: メモリリークの監視とテスト

## 注意点

- 全てのリソースを適切に解放
- メモリリークの早期発見
- 適切なテストの実装
- パフォーマンス監視

## 関連技術
- メモリ管理
- Subscription管理
- takeUntilパターン
- リソース管理
