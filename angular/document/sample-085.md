# #085 Lifecycle のよくあるエラー

## 概要
Angular v20におけるLifecycle Hooksのよくあるエラーを学びます。典型的なエラーパターンとその解決方法、予防策について解説します。

## 学習目標
- よくあるエラーパターンを理解する
- エラーの原因と解決方法を習得する
- エラーを防ぐベストプラクティスを身につける

## 📺 画面表示用コード

```typescript
// よくあるエラー: DOM要素への早期アクセス
export class CommonErrorComponent implements OnInit {
  @ViewChild('element') element?: ElementRef;
  
  ngOnInit() {
    // ❌ エラー: DOM要素がまだ利用できない
    this.element?.nativeElement.focus();
  }
}

// 正しい実装
export class CorrectComponent implements AfterViewInit {
  @ViewChild('element') element?: ElementRef;
  
  ngAfterViewInit() {
    // ✅ 正しい: DOM要素が利用可能
    this.element?.nativeElement.focus();
  }
}
```

```typescript
// よくあるエラー: 購読の未解除
export class SubscriptionErrorComponent implements OnInit {
  ngOnInit() {
    // ❌ エラー: 購読が解除されていない
    this.dataService.getData().subscribe(data => {
      // 処理
    });
  }
}

// 正しい実装
export class SubscriptionCorrectComponent implements OnInit, OnDestroy {
  private subscription = new Subscription();
  
  ngOnInit() {
    this.subscription.add(
      this.dataService.getData().subscribe(data => {
        // 処理
      })
    );
  }
  
  ngOnDestroy() {
    this.subscription.unsubscribe();
  }
}
```

## 技術ポイント

### 1. よくあるエラーパターン
- **DOM要素への早期アクセス**: ngOnInitでのDOM操作
- **購読の未解除**: Subscriptionの未解除
- **タイマーの未クリア**: setTimeout/setIntervalの未クリア
- **イベントリスナーの未削除**: イベントリスナーの未削除

### 2. エラーの原因
- **実行タイミングの誤解**: Hookの実行タイミングの誤解
- **リソース管理の不備**: 適切でないリソース管理
- **メモリリーク**: リソースの未解放

### 3. 解決方法
- **適切なHookの選択**: 用途に応じたHookの選択
- **適切なリソース管理**: 確実なリソース解放
- **エラーハンドリング**: 適切な例外処理

## 実践的な活用例

### 1. DOM要素アクセスエラーの解決
```typescript
// ❌ 間違った実装
export class WrongDOMAccessComponent implements OnInit {
  @ViewChild('input') input?: ElementRef;
  
  ngOnInit() {
    // DOM要素がまだ利用できない
    this.input?.nativeElement.focus();
  }
}

// ✅ 正しい実装
export class CorrectDOMAccessComponent implements AfterViewInit {
  @ViewChild('input') input?: ElementRef;
  
  ngAfterViewInit() {
    // DOM要素が利用可能
    if (this.input) {
      this.input.nativeElement.focus();
    }
  }
}
```

### 2. 購読管理エラーの解決
```typescript
// ❌ 間違った実装
export class WrongSubscriptionComponent implements OnInit {
  ngOnInit() {
    this.dataService.getData().subscribe(data => {
      // 購読が解除されていない
    });
  }
}

// ✅ 正しい実装
export class CorrectSubscriptionComponent implements OnInit, OnDestroy {
  private subscription = new Subscription();
  
  ngOnInit() {
    this.subscription.add(
      this.dataService.getData().subscribe(data => {
        // 適切に管理された購読
      })
    );
  }
  
  ngOnDestroy() {
    this.subscription.unsubscribe();
  }
}
```

### 3. タイマー管理エラーの解決
```typescript
// ❌ 間違った実装
export class WrongTimerComponent implements OnInit {
  ngOnInit() {
    setInterval(() => {
      // タイマーがクリアされていない
    }, 1000);
  }
}

// ✅ 正しい実装
export class CorrectTimerComponent implements OnInit, OnDestroy {
  private timer?: number;
  
  ngOnInit() {
    this.timer = setInterval(() => {
      // 適切に管理されたタイマー
    }, 1000);
  }
  
  ngOnDestroy() {
    if (this.timer) {
      clearInterval(this.timer);
    }
  }
}
```

## ベストプラクティス

1. **適切なHookの選択**: 用途に応じたHookの選択
2. **リソース管理**: 確実なリソース解放
3. **エラーハンドリング**: 適切な例外処理
4. **テスト**: エラーパターンのテスト

## 注意点

- 適切なタイミングでの処理実行
- 確実なリソース解放
- エラーハンドリングの実装
- メモリリークの防止

## 関連技術
- エラーハンドリング
- リソース管理
- デバッグ手法
- ベストプラクティス
