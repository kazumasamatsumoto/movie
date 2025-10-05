# #086 Lifecycle のパフォーマンス影響

## 概要
Angular v20におけるLifecycle Hooksのパフォーマンス影響を学びます。頻繁に実行されるHookの最適化、パフォーマンス監視、効率的な実装方法について解説します。

## 学習目標
- Lifecycle Hooksのパフォーマンス影響を理解する
- パフォーマンス最適化の方法を習得する
- 効率的な実装パターンを身につける

## 📺 画面表示用コード

```typescript
// パフォーマンス監視
export class PerformanceMonitorComponent implements DoCheck {
  private checkCount = 0;
  private lastCheckTime = 0;
  
  ngDoCheck() {
    this.checkCount++;
    const now = performance.now();
    
    if (now - this.lastCheckTime > 100) { // 100ms間隔でチェック
      console.warn(`ngDoCheck実行回数: ${this.checkCount}`);
      this.lastCheckTime = now;
    }
  }
}
```

```typescript
// 効率的な変更検知
export class EfficientChangeComponent implements DoCheck {
  private previousValue: any;
  
  ngDoCheck() {
    if (this.value !== this.previousValue) {
      this.onValueChange();
      this.previousValue = this.value;
    }
  }
  
  private onValueChange() {
    // 値が変更された時のみ処理
  }
}
```

## 技術ポイント

### 1. パフォーマンスへの影響
- **頻繁な実行**: ngDoCheck, ngAfterContentChecked, ngAfterViewChecked
- **処理の重さ**: 重い処理によるパフォーマンス低下
- **メモリ使用量**: 不適切なリソース管理

### 2. 最適化手法
- **条件付き実行**: 必要な時のみ処理実行
- **デバウンス**: 頻繁な実行の制御
- **効率的な比較**: 軽量な比較処理

### 3. 監視方法
- **実行回数の監視**: 頻繁な実行の検出
- **処理時間の測定**: 重い処理の特定
- **メモリ使用量の監視**: メモリリークの検出

## 実践的な活用例

### 1. 効率的な変更検知
```typescript
export class EfficientChangeDetectionComponent implements DoCheck {
  private previousValues = new Map<string, any>();
  
  ngDoCheck() {
    // 効率的な値の比較
    if (this.hasValueChanged('data', this.data)) {
      this.onDataChange();
    }
    
    if (this.hasValueChanged('filter', this.filter)) {
      this.onFilterChange();
    }
  }
  
  private hasValueChanged(key: string, currentValue: any): boolean {
    const previousValue = this.previousValues.get(key);
    if (previousValue !== currentValue) {
      this.previousValues.set(key, currentValue);
      return true;
    }
    return false;
  }
}
```

### 2. デバウンス処理
```typescript
export class DebouncedComponent implements DoCheck {
  private debounceTimer?: number;
  private lastCheckTime = 0;
  
  ngDoCheck() {
    const now = Date.now();
    
    if (now - this.lastCheckTime > 50) { // 50ms間隔
      if (this.debounceTimer) {
        clearTimeout(this.debounceTimer);
      }
      
      this.debounceTimer = setTimeout(() => {
        this.performCheck();
        this.lastCheckTime = now;
      }, 10);
    }
  }
  
  private performCheck() {
    // 実際のチェック処理
  }
}
```

### 3. 条件付き実行
```typescript
export class ConditionalExecutionComponent implements DoCheck {
  @Input() enableMonitoring = false;
  private checkCount = 0;
  
  ngDoCheck() {
    if (this.enableMonitoring) {
      this.checkCount++;
      
      if (this.checkCount % 10 === 0) {
        this.performPeriodicCheck();
      }
    }
  }
  
  private performPeriodicCheck() {
    // 定期的なチェック処理
  }
}
```

## ベストプラクティス

1. **軽量な処理**: 頻繁に実行されるHookでは軽量な処理
2. **条件付き実行**: 必要な時のみ処理実行
3. **デバウンス**: 頻繁な実行の制御
4. **監視**: 定期的なパフォーマンス監視

## 注意点

- 頻繁に実行されるHookでの重い処理を避ける
- 適切なデバウンス処理の実装
- パフォーマンス監視の継続
- メモリリークの防止

## 関連技術
- パフォーマンス最適化
- 変更検知
- デバウンス処理
- パフォーマンス監視
