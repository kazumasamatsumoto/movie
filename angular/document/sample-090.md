# #090 Lifecycle のアンチパターン

## 概要
Angular v20におけるLifecycle Hooksのアンチパターンを学びます。避けるべき実装パターンとその理由を理解し、適切な実装方法について解説します。

## 学習目標
- Lifecycle Hooksのアンチパターンを理解する
- 避けるべき実装パターンを把握する
- 適切な実装方法を習得する

## 📺 画面表示用コード

```typescript
// アンチパターン: 重い処理の実行
export class AntiPatternComponent implements DoCheck {
  ngDoCheck() {
    // ❌ 重い処理を実行（頻繁に呼ばれるため）
    this.heavyCalculation();
  }
  
  private heavyCalculation() {
    // 重い計算処理
  }
}
```

```typescript
// 適切な実装: 軽量な処理
export class ProperComponent implements DoCheck {
  ngDoCheck() {
    // ✅ 軽量な処理のみ
    if (this.shouldUpdate()) {
      this.update();
    }
  }
}
```

## 技術ポイント

### 1. 主要なアンチパターン
- **重い処理の実行**: 頻繁に呼ばれるHookでの重い処理
- **メモリリーク**: 適切でないリソース管理
- **無限ループ**: 変更検知での無限ループ
- **不適切なタイミング**: 間違ったタイミングでの処理

### 2. パフォーマンスへの影響
アンチパターンは以下の問題を引き起こします：
- パフォーマンスの低下
- メモリリーク
- アプリケーションの不安定性
- ユーザーエクスペリエンスの悪化

### 3. 適切な実装パターン
- 軽量で効率的な処理
- 適切なリソース管理
- 適切なタイミングでの処理実行
- エラーハンドリングの実装

## 実践的な活用例

### 1. メモリリークの防止
```typescript
// ❌ アンチパターン: 購読の未解除
export class LeakComponent implements OnInit {
  ngOnInit() {
    this.dataService.getData().subscribe(data => {
      // 購読解除されていない
    });
  }
}

// ✅ 適切な実装: 購読の適切な管理
export class ProperComponent implements OnInit, OnDestroy {
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

### 2. 適切なタイミングでの処理
```typescript
// ❌ アンチパターン: 不適切なタイミングでのDOM操作
export class WrongTimingComponent implements OnInit {
  @ViewChild('element') element?: ElementRef;
  
  ngOnInit() {
    // DOM要素がまだ利用できない可能性
    this.element?.nativeElement.focus();
  }
}

// ✅ 適切な実装: 適切なタイミングでのDOM操作
export class ProperTimingComponent implements AfterViewInit {
  @ViewChild('element') element?: ElementRef;
  
  ngAfterViewInit() {
    // DOM要素が利用可能
    this.element?.nativeElement.focus();
  }
}
```

### 3. 効率的な変更検知
```typescript
// ❌ アンチパターン: 非効率的な変更検知
export class InefficientComponent implements DoCheck {
  ngDoCheck() {
    // 毎回重い処理を実行
    this.processAllData();
  }
}

// ✅ 適切な実装: 効率的な変更検知
export class EfficientComponent implements DoCheck {
  private previousData: any;
  
  ngDoCheck() {
    if (this.hasDataChanged()) {
      this.processData();
    }
  }
  
  private hasDataChanged(): boolean {
    return this.data !== this.previousData;
  }
}
```

## ベストプラクティス

1. **軽量な処理**: 頻繁に呼ばれるHookでは軽量な処理を心がける
2. **適切なリソース管理**: メモリリークを防ぐための適切な管理
3. **適切なタイミング**: 処理を実行する適切なタイミングの選択
4. **エラーハンドリング**: 適切な例外処理の実装

## 注意点

- 重い処理の実行を避ける
- メモリリークの防止
- 適切なタイミングでの処理実行
- 無限ループの回避

## 関連技術
- パフォーマンス最適化
- メモリ管理
- エラーハンドリング
- Angular v20のSignal
