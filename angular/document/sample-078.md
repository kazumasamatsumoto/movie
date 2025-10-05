# #078 ngOnDestroy での購読解除

## 概要
Angular v20におけるngOnDestroyでの購読解除を学びます。Observableの購読を適切に管理し、メモリリークを防ぐ方法について解説します。

## 学習目標
- 購読解除の重要性を理解する
- 適切な購読管理方法を習得する
- takeUntilパターンの活用方法を身につける

## 📺 画面表示用コード

```typescript
// 基本的な購読解除
export class SubscriptionComponent implements OnInit, OnDestroy {
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

```typescript
// takeUntilパターン
export class TakeUntilComponent implements OnInit, OnDestroy {
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

### 1. 購読解除の重要性
- **メモリリークの防止**: 適切な購読解除によりメモリリークを防ぐ
- **パフォーマンス向上**: 不要な処理の停止
- **アプリケーションの安定性**: 予期しない動作の防止

### 2. 購読管理の方法
- **Subscription**: 複数購読の集約管理
- **takeUntil**: 自動購読解除パターン
- **手動解除**: 個別の購読解除

### 3. takeUntilパターン
- 自動的な購読解除
- コードの簡潔性
- エラーハンドリングの向上

## 実践的な活用例

### 1. 複数購読の管理
```typescript
export class MultipleSubscriptionComponent implements OnInit, OnDestroy {
  private subscriptions = new Subscription();
  
  ngOnInit() {
    this.subscriptions.add(
      this.userService.getUser().subscribe(user => {
        this.handleUser(user);
      })
    );
    
    this.subscriptions.add(
      this.dataService.getData().subscribe(data => {
        this.handleData(data);
      })
    );
  }
  
  ngOnDestroy() {
    this.subscriptions.unsubscribe();
  }
}
```

### 2. takeUntilパターンの活用
```typescript
export class TakeUntilPatternComponent implements OnInit, OnDestroy {
  private destroy$ = new Subject<void>();
  
  ngOnInit() {
    // 複数のObservableを自動購読解除
    this.userService.getUser()
      .pipe(takeUntil(this.destroy$))
      .subscribe(user => {
        this.handleUser(user);
      });
      
    this.dataService.getData()
      .pipe(takeUntil(this.destroy$))
      .subscribe(data => {
        this.handleData(data);
      });
  }
  
  ngOnDestroy() {
    this.destroy$.next();
    this.destroy$.complete();
  }
}
```

### 3. 条件付き購読解除
```typescript
export class ConditionalUnsubscribeComponent implements OnInit, OnDestroy {
  private subscription?: Subscription;
  
  ngOnInit() {
    if (this.shouldSubscribe()) {
      this.subscription = this.dataService.getData().subscribe(data => {
        this.handleData(data);
      });
    }
  }
  
  ngOnDestroy() {
    if (this.subscription) {
      this.subscription.unsubscribe();
    }
  }
  
  private shouldSubscribe(): boolean {
    // 購読条件の判定
    return true;
  }
}
```

## ベストプラクティス

1. **自動化**: takeUntilパターンなどの自動化手法の活用
2. **集約管理**: 複数購読の集約的な管理
3. **早期解除**: 不要になった時点での即座な解除
4. **テスト**: 購読解除のテスト実装

## 注意点

- 全ての購読を適切に解除
- メモリリークの早期発見
- 適切なタイミングでの解除
- エラーハンドリングの実装

## 関連技術
- Observable
- Subscription
- takeUntilパターン
- メモリ管理
