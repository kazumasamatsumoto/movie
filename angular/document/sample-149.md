# #149 「ContentChildren - 複数投影参照」

## 概要
Angular v20におけるContentChildrenデコレータを使った複数の投影コンテンツの一括管理。QueryListを活用した効率的な複数要素操作と動的なコンテンツ管理を学ぶ。

## 学習目標
- ContentChildrenの基本的な使い方を理解する
- QueryListでの複数要素管理を学ぶ
- 動的コンテンツ制御を把握する

## 技術ポイント
- @ContentChildren() デコレータの使用
- QueryList での複数要素管理
- 動的なコンテンツ制御
- 効率的な操作

## 📺 画面表示用コード

### ContentChildrenの基本的な使用
```typescript
@Component({
  selector: 'app-list-container',
  template: `
    <div class="container">
      <ng-content></ng-content>
    </div>
    <div class="controls">
      <button (click)="highlightAll()">すべて強調</button>
      <button (click)="countItems()">項目数表示</button>
    </div>
    <p>項目数: {{ itemCount }}</p>
  `
})
export class ListContainerComponent implements AfterContentInit {
  @ContentChildren('.list-item') items!: QueryList<ElementRef>;
  itemCount = 0;

  ngAfterContentInit() {
    this.itemCount = this.items.length;
    
    this.items.changes.subscribe(() => {
      this.itemCount = this.items.length;
    });
  }

  highlightAll() {
    this.items.forEach(item => {
      item.nativeElement.style.backgroundColor = 'yellow';
    });
  }

  countItems() {
    console.log('総項目数:', this.items.length);
    this.items.forEach((item, index) => {
      item.nativeElement.setAttribute('data-index', index.toString());
    });
  }
}
```

### 使用例
```typescript
@Component({
  template: `
    <app-list-container>
      <div class="list-item">項目1</div>
      <div class="list-item">項目2</div>
      <div class="list-item">項目3</div>
    </app-list-container>
  `
})
export class ParentComponent {}
```

## 実践的な活用例
- リストコンテナ
- フォームグループ
- タブコンポーネント

## ベストプラクティス
- 適切なセレクタを使用
- 効率的な操作を実装
- 変更検知を活用

## 注意点
- セレクタの一意性
- メモリリークの防止
- パフォーマンスの考慮

## 関連技術
- 複数要素管理
- QueryList
- 動的コンテンツ
