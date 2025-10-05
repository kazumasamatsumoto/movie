# #071 ngAfterViewChecked - ビューチェック後

## 概要
Angular v20におけるngAfterViewCheckedの使用方法を学びます。ビューの変更チェック後に処理を実行し、効率的なビュー監視を行う方法について解説します。

## 学習目標
- ngAfterViewCheckedの基本的な使用方法を理解する
- ngAfterViewInitとの違いを把握する
- パフォーマンスを考慮した実装方法を習得する

## 📺 画面表示用コード

```typescript
// ngAfterViewCheckedの基本実装
export class ViewCheckComponent implements AfterViewChecked {
  @ViewChild('dynamicElement') element?: ElementRef;
  private previousHeight = 0;
  
  ngAfterViewChecked() {
    if (this.element) {
      const currentHeight = this.element.nativeElement.offsetHeight;
      if (currentHeight !== this.previousHeight) {
        this.onHeightChange(currentHeight);
        this.previousHeight = currentHeight;
      }
    }
  }
  
  private onHeightChange(height: number) {
    // 高さ変更時の処理
  }
}
```

```typescript
// 軽量なチェック処理
export class LightweightViewComponent implements AfterViewChecked {
  private checkCount = 0;
  
  ngAfterViewChecked() {
    this.checkCount++;
    if (this.checkCount % 10 === 0) { // 10回に1回実行
      this.performPeriodicCheck();
    }
  }
  
  private performPeriodicCheck() {
    // 定期的なチェック処理
  }
}
```

## 技術ポイント

### 1. ngAfterViewCheckedの基本
ngAfterViewCheckedは、ビューの変更チェック後に実行されるHookです。AfterViewCheckedインターフェースを実装することで使用できます。

### 2. ngAfterViewInitとの違い
- **ngAfterViewInit**: 初回のみ実行
- **ngAfterViewChecked**: 毎回実行（変更検知サイクルごと）

### 3. パフォーマンス考慮
頻繁に実行されるため、軽量で効率的な処理を心がける必要があります。

## 実践的な活用例

### 1. ビューサイズの監視
```typescript
export class ViewSizeMonitorComponent implements AfterViewChecked {
  @ViewChild('container') container?: ElementRef;
  private previousSize = { width: 0, height: 0 };
  
  ngAfterViewChecked() {
    if (this.container) {
      const currentSize = {
        width: this.container.nativeElement.offsetWidth,
        height: this.container.nativeElement.offsetHeight
      };
      
      if (this.hasSizeChanged(currentSize)) {
        this.onSizeChange(currentSize);
        this.previousSize = currentSize;
      }
    }
  }
  
  private hasSizeChanged(currentSize: { width: number; height: number }): boolean {
    return currentSize.width !== this.previousSize.width || 
           currentSize.height !== this.previousSize.height;
  }
  
  private onSizeChange(size: { width: number; height: number }) {
    // サイズ変更時の処理
  }
}
```

### 2. 条件付きビューチェック
```typescript
export class ConditionalViewComponent implements AfterViewChecked {
  @Input() enableMonitoring = false;
  private lastCheckTime = 0;
  
  ngAfterViewChecked() {
    if (this.enableMonitoring) {
      const now = Date.now();
      if (now - this.lastCheckTime > 100) { // 100ms間隔
        this.performViewCheck();
        this.lastCheckTime = now;
      }
    }
  }
  
  private performViewCheck() {
    // ビューチェック処理
  }
}
```

### 3. デバウンス付きビューチェック
```typescript
export class DebouncedViewComponent implements AfterViewChecked {
  private debounceTimer?: number;
  
  ngAfterViewChecked() {
    if (this.debounceTimer) {
      clearTimeout(this.debounceTimer);
    }
    
    this.debounceTimer = setTimeout(() => {
      this.performDebouncedCheck();
    }, 50); // 50ms後に実行
  }
  
  private performDebouncedCheck() {
    // デバウンスされたチェック処理
  }
}
```

## ベストプラクティス

1. **軽量な処理**: 頻繁に実行されるため軽量な処理を心がける
2. **条件付き実行**: 必要な時のみ処理を実行
3. **デバウンス**: 頻繁な実行を避けるためのデバウンス処理
4. **パフォーマンス監視**: パフォーマンスへの影響を監視

## 注意点

- 頻繁に実行されるためパフォーマンスに注意
- 重い処理は避ける
- 適切なデバウンス処理の実装
- メモリリークの防止

## 関連技術
- ViewChild/ViewChildren
- パフォーマンス最適化
- デバウンス処理
- Angular v20のSignal
