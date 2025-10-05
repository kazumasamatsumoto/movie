# #072 ngOnDestroy - クリーンアップ処理

## 概要
Angular v20におけるngOnDestroyの使用方法を学びます。コンポーネントの破棄時に適切なクリーンアップ処理を実行し、メモリリークを防ぐ方法について解説します。

## 学習目標
- ngOnDestroyの基本的な使用方法を理解する
- クリーンアップ処理の種類を把握する
- メモリリークの防止方法を習得する

## 📺 画面表示用コード

```typescript
// ngOnDestroyの基本実装
export class CleanupComponent implements OnDestroy {
  private subscription?: Subscription;
  private timer?: number;
  
  ngOnDestroy() {
    if (this.subscription) {
      this.subscription.unsubscribe();
    }
    if (this.timer) {
      clearInterval(this.timer);
    }
  }
}
```

```typescript
// 複数のリソースのクリーンアップ
export class MultiCleanupComponent implements OnDestroy {
  private subscriptions = new Set<Subscription>();
  private timers: number[] = [];
  
  ngOnDestroy() {
    this.subscriptions.forEach(sub => sub.unsubscribe());
    this.timers.forEach(timer => clearInterval(timer));
  }
}
```

## 技術ポイント

### 1. ngOnDestroyの基本
ngOnDestroyは、コンポーネントが破棄される時に呼び出されるHookです。OnDestroyインターフェースを実装することで使用できます。

### 2. クリーンアップ処理の種類
- **Subscription**: Observableの購読解除
- **タイマー**: setInterval、setTimeoutのクリア
- **イベントリスナー**: DOMイベントの削除
- **WebSocket**: 接続の切断

### 3. メモリリークの防止
適切なクリーンアップにより、メモリリークを防ぎ、アプリケーションの安定性を向上させます。

## 実践的な活用例

### 1. Subscriptionの管理
```typescript
export class SubscriptionComponent implements OnDestroy {
  private subscription = new Subscription();
  
  ngOnInit() {
    this.subscription.add(
      this.dataService.getData().subscribe(data => {
        // データ処理
      })
    );
  }
  
  ngOnDestroy() {
    this.subscription.unsubscribe();
  }
}
```

### 2. タイマーの管理
```typescript
export class TimerComponent implements OnDestroy {
  private timer?: number;
  
  ngOnInit() {
    this.timer = setInterval(() => {
      this.updateTime();
    }, 1000);
  }
  
  ngOnDestroy() {
    if (this.timer) {
      clearInterval(this.timer);
    }
  }
}
```

### 3. イベントリスナーの管理
```typescript
export class EventComponent implements OnDestroy {
  private resizeListener?: () => void;
  
  ngOnInit() {
    this.resizeListener = () => this.onResize();
    window.addEventListener('resize', this.resizeListener);
  }
  
  ngOnDestroy() {
    if (this.resizeListener) {
      window.removeEventListener('resize', this.resizeListener);
    }
  }
}
```

## ベストプラクティス

1. **適切なクリーンアップ**: 全てのリソースを適切に解放
2. **メモリリークの防止**: 購読やタイマーの適切な管理
3. **効率的な管理**: 複数リソースの効率的な管理
4. **エラーハンドリング**: クリーンアップ処理での例外処理

## 注意点

- 全てのリソースを適切に解放
- メモリリークの防止
- 適切なタイミングでのクリーンアップ
- エラーハンドリングの実装

## 関連技術
- メモリ管理
- Subscription
- タイマー管理
- イベントリスナー
