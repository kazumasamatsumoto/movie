# #080 Lifecycle での DOM 操作

## 概要
Angular v20におけるLifecycle HooksでのDOM操作を学びます。適切なタイミングでのDOM要素へのアクセスと操作、パフォーマンスを考慮した実装方法について解説します。

## 学習目標
- DOM操作の適切なタイミングを理解する
- ViewChild/ViewChildrenの活用方法を習得する
- パフォーマンスを考慮したDOM操作を身につける

## 📺 画面表示用コード

```typescript
// DOM操作の基本
export class DOMComponent implements AfterViewInit, OnDestroy {
  @ViewChild('inputElement') inputElement?: ElementRef<HTMLInputElement>;
  @ViewChild('canvas') canvas?: ElementRef<HTMLCanvasElement>;
  
  ngAfterViewInit() {
    // DOM要素が利用可能になった後に操作
    if (this.inputElement) {
      this.inputElement.nativeElement.focus();
    }
    
    if (this.canvas) {
      this.setupCanvas();
    }
  }
  
  ngOnDestroy() {
    // クリーンアップ処理
  }
  
  private setupCanvas() {
    const ctx = this.canvas!.nativeElement.getContext('2d');
    if (ctx) {
      ctx.fillRect(0, 0, 100, 100);
    }
  }
}
```

```typescript
// 複数要素の操作
export class MultipleDOMComponent implements AfterViewInit {
  @ViewChildren('item') items?: QueryList<ElementRef>;
  
  ngAfterViewInit() {
    this.items?.forEach((item, index) => {
      item.nativeElement.classList.add(`item-${index}`);
    });
  }
}
```

## 技術ポイント

### 1. DOM操作のタイミング
- **ngAfterViewInit**: DOM要素が利用可能になった後
- **ngOnInit**: DOM要素はまだ利用不可
- **ngAfterViewChecked**: 毎回実行されるため注意

### 2. ViewChild/ViewChildren
- **ViewChild**: 単一のDOM要素へのアクセス
- **ViewChildren**: 複数のDOM要素へのアクセス
- **ElementRef**: DOM要素への参照

### 3. パフォーマンス考慮
- 適切なタイミングでの操作
- 効率的な要素の選択
- 不要な操作の回避

## 実践的な活用例

### 1. フォーカス管理
```typescript
export class FocusComponent implements AfterViewInit {
  @ViewChild('firstInput') firstInput?: ElementRef<HTMLInputElement>;
  @ViewChild('submitButton') submitButton?: ElementRef<HTMLButtonElement>;
  
  ngAfterViewInit() {
    if (this.firstInput) {
      this.firstInput.nativeElement.focus();
    }
  }
  
  onFormSubmit() {
    if (this.submitButton) {
      this.submitButton.nativeElement.blur();
    }
  }
}
```

### 2. キャンバス操作
```typescript
export class CanvasComponent implements AfterViewInit {
  @ViewChild('canvas') canvas?: ElementRef<HTMLCanvasElement>;
  private ctx?: CanvasRenderingContext2D;
  
  ngAfterViewInit() {
    if (this.canvas) {
      this.ctx = this.canvas.nativeElement.getContext('2d');
      this.draw();
    }
  }
  
  private draw() {
    if (this.ctx) {
      this.ctx.fillStyle = 'blue';
      this.ctx.fillRect(0, 0, 100, 100);
    }
  }
}
```

### 3. 動的スタイル適用
```typescript
export class DynamicStyleComponent implements AfterViewInit {
  @ViewChildren('.dynamic-item') items?: QueryList<ElementRef>;
  
  ngAfterViewInit() {
    this.items?.forEach((item, index) => {
      const element = item.nativeElement;
      element.style.backgroundColor = this.getColor(index);
      element.style.padding = '10px';
    });
  }
  
  private getColor(index: number): string {
    const colors = ['red', 'blue', 'green', 'yellow'];
    return colors[index % colors.length];
  }
}
```

## ベストプラクティス

1. **適切なタイミング**: ngAfterViewInitでの操作
2. **存在チェック**: 要素の存在確認
3. **効率的な操作**: 不要な操作の回避
4. **クリーンアップ**: 適切なリソース解放

## 注意点

- DOM要素が存在する場合のみ操作
- 適切なタイミングでの操作
- パフォーマンスへの影響を考慮
- メモリリークの防止

## 関連技術
- ViewChild/ViewChildren
- ElementRef
- DOM操作
- パフォーマンス最適化
