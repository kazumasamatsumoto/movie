# #141 「ViewChildren - 複数要素参照」

## 概要
Angular v20におけるViewChildrenデコレータを使った複数要素の参照取得。QueryListを返し、複数の要素を配列のように効率的に管理する方法を学ぶ。

## 学習目標
- ViewChildrenの基本的な使い方を理解する
- QueryListの特徴を学ぶ
- 複数要素の一括操作を把握する

## 技術ポイント
- @ViewChildren() デコレータの使用
- QueryList の活用
- 複数要素の管理
- 効率的な操作

## 📺 画面表示用コード

### 基本的なViewChildrenの使用
```typescript
@Component({
  selector: 'app-list',
  template: `
    <div #item *ngFor="let item of items; let i = index">
      {{ item }} ({{ i }})
    </div>
    <button (click)="highlightAll()">すべて強調</button>
  `
})
export class ListComponent implements AfterViewInit {
  @ViewChildren('item') items!: QueryList<ElementRef>;
  data = ['項目1', '項目2', '項目3'];

  ngAfterViewInit() {
    console.log('要素数:', this.items.length);
  }

  highlightAll() {
    this.items.forEach((item, index) => {
      item.nativeElement.style.backgroundColor = 'yellow';
    });
  }
}
```

## 実践的な活用例
- リスト要素の一括操作
- フォーム要素の管理
- 動的な要素制御

## ベストプラクティス
- 適切なセレクタを使用
- 効率的な操作を心がける
- パフォーマンスを考慮する

## 注意点
- QueryListの特性を理解する
- 動的要素の扱いに注意
- メモリリークを防ぐ

## 関連技術
- QueryList
- 複数要素管理
- 動的要素
