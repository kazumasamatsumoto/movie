# #069 ngAfterContentChecked - コンテンツチェック後

## 概要
Angular v20におけるngAfterContentCheckedの使用方法を学びます。コンテンツ投影の変更チェック後に処理を実行する方法について解説します。

## 学習目標
- ngAfterContentCheckedの基本的な使用方法を理解する
- ngAfterContentInitとの違いを把握する
- パフォーマンスを考慮した実装方法を習得する

## 📺 画面表示用コード

```typescript
// ngAfterContentCheckedの基本実装
export class ContentCheckComponent implements AfterContentChecked {
  @ContentChild('dynamicContent') content?: ElementRef;
  private previousContentHeight = 0;
  
  ngAfterContentChecked() {
    if (this.content) {
      const currentHeight = this.content.nativeElement.offsetHeight;
      if (currentHeight !== this.previousContentHeight) {
        this.onContentHeightChange(currentHeight);
        this.previousContentHeight = currentHeight;
      }
    }
  }
  
  private onContentHeightChange(height: number) {
    // コンテンツの高さ変更時の処理
  }
}
```

```typescript
// 軽量なチェック処理
export class LightweightCheckComponent implements AfterContentChecked {
  private lastCheck = 0;
  
  ngAfterContentChecked() {
    const now = Date.now();
    if (now - this.lastCheck > 100) { // 100ms間隔でチェック
      this.performCheck();
      this.lastCheck = now;
    }
  }
  
  private performCheck() {
    // チェック処理
  }
}
```

## 技術ポイント

### 1. ngAfterContentCheckedの基本
ngAfterContentCheckedは、コンテンツ投影の変更チェック後に実行されるHookです。AfterContentCheckedインターフェースを実装することで使用できます。

### 2. ngAfterContentInitとの違い
- **ngAfterContentInit**: 初回のみ実行
- **ngAfterContentChecked**: 毎回実行（変更検知サイクルごと）

### 3. パフォーマンス考慮
頻繁に実行されるため、軽量で効率的な処理を心がける必要があります。

## 実践的な活用例

### 1. コンテンツサイズの監視
```typescript
export class SizeMonitorComponent implements AfterContentChecked {
  @ContentChild('monitoredContent') content?: ElementRef;
  private previousSize = { width: 0, height: 0 };
  
  ngAfterContentChecked() {
    if (this.content) {
      const currentSize = {
        width: this.content.nativeElement.offsetWidth,
        height: this.content.nativeElement.offsetHeight
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
}
```

### 2. 条件付き処理
```typescript
export class ConditionalCheckComponent implements AfterContentChecked {
  @Input() enableCheck = false;
  
  ngAfterContentChecked() {
    if (this.enableCheck) {
      this.performConditionalCheck();
    }
  }
  
  private performConditionalCheck() {
    // 条件付きチェック処理
  }
}
```

### 3. デバウンス処理
```typescript
export class DebouncedCheckComponent implements AfterContentChecked {
  private checkTimeout?: number;
  
  ngAfterContentChecked() {
    if (this.checkTimeout) {
      clearTimeout(this.checkTimeout);
    }
    
    this.checkTimeout = setTimeout(() => {
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
- コンテンツ投影
- パフォーマンス最適化
- デバウンス処理
- Angular v20のSignal
