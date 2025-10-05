# #070 ngAfterViewInit - ビュー初期化後

## 概要
Angular v20におけるngAfterViewInitの使用方法を学びます。ビューが初期化された後に処理を実行し、DOM要素に安全にアクセスする方法について解説します。

## 学習目標
- ngAfterViewInitの基本的な使用方法を理解する
- ビュー初期化のタイミングを把握する
- ViewChild/ViewChildrenの活用方法を習得する

## 📺 画面表示用コード

```typescript
// ngAfterViewInitの基本実装
export class ViewInitComponent implements AfterViewInit {
  @ViewChild('inputElement') inputElement?: ElementRef<HTMLInputElement>;
  
  ngAfterViewInit() {
    console.log('ビューが初期化されました');
    if (this.inputElement) {
      this.setupInputElement();
    }
  }
  
  private setupInputElement() {
    this.inputElement!.nativeElement.focus();
  }
}
```

```typescript
// ViewChildrenの活用
export class MultipleViewComponent implements AfterViewInit {
  @ViewChildren(ItemComponent) items?: QueryList<ItemComponent>;
  
  ngAfterViewInit() {
    this.items?.forEach(item => {
      item.initialize();
    });
  }
}
```

## 技術ポイント

### 1. ngAfterViewInitの基本
ngAfterViewInitは、ビューが初期化された後に実行されるHookです。AfterViewInitインターフェースを実装することで使用できます。

### 2. 実行タイミング
- 子コンポーネントのビュー初期化後
- 親のngOnInit後
- DOM要素が利用可能になった後

### 3. ViewChild/ViewChildren
ビュー内の要素にアクセスするためのデコレータ：
- `ViewChild`: 単一の要素
- `ViewChildren`: 複数の要素

## 実践的な活用例

### 1. DOM要素の操作
```typescript
export class DOMComponent implements AfterViewInit {
  @ViewChild('canvas') canvas?: ElementRef<HTMLCanvasElement>;
  
  ngAfterViewInit() {
    if (this.canvas) {
      this.setupCanvas();
    }
  }
  
  private setupCanvas() {
    const ctx = this.canvas!.nativeElement.getContext('2d');
    if (ctx) {
      ctx.fillRect(0, 0, 100, 100);
    }
  }
}
```

### 2. 子コンポーネントの初期化
```typescript
export class ParentComponent implements AfterViewInit {
  @ViewChild(ChildComponent) childComponent?: ChildComponent;
  @ViewChildren(GrandChildComponent) grandChildren?: QueryList<GrandChildComponent>;
  
  ngAfterViewInit() {
    if (this.childComponent) {
      this.childComponent.initialize();
    }
    
    this.grandChildren?.forEach(grandChild => {
      grandChild.setParent(this.childComponent);
    });
  }
}
```

### 3. フォーカス管理
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

## ベストプラクティス

1. **適切なタイミング**: DOM要素が利用可能になった後の処理実行
2. **ViewChild/ViewChildrenの活用**: ビュー内要素への適切なアクセス
3. **エラーハンドリング**: 要素の存在チェック
4. **パフォーマンス考慮**: 効率的なビュー操作

## 注意点

- DOM要素が存在する場合のみ処理を実行
- 適切なエラーハンドリングの実装
- パフォーマンスへの影響を考慮
- ビュー初期化のタイミングを理解

## 関連技術
- ViewChild/ViewChildren
- AfterViewInit
- DOM操作
- Angular v20のSignal
