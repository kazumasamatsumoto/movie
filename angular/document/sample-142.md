# #142 「ViewChildren QueryList の活用」

## 概要
Angular v20におけるViewChildrenが返すQueryListの活用方法。forEach、map、filterなどの配列メソッドや変更検知機能を使用した効率的な複数要素管理を学ぶ。

## 学習目標
- QueryListの主要なメソッドを理解する
- 変更検知機能を学ぶ
- 効率的な要素操作を把握する

## 技術ポイント
- QueryList.forEach() での反復処理
- QueryList.map() での変換
- QueryList.filter() での絞り込み
- changes イベントでの変更検知

## 📺 画面表示用コード

### QueryListの活用
```typescript
@Component({
  selector: 'app-query-list',
  template: `
    <div #card *ngFor="let card of cards" class="card">
      {{ card.title }}
    </div>
    <button (click)="processCards()">カード処理</button>
  `
})
export class QueryListComponent implements AfterViewInit {
  @ViewChildren('card') cards!: QueryList<ElementRef>;
  cardData = [
    { title: 'カード1' },
    { title: 'カード2' },
    { title: 'カード3' }
  ];

  ngAfterViewInit() {
    this.cards.changes.subscribe(() => {
      console.log('カード数が変更されました:', this.cards.length);
    });
  }

  processCards() {
    // forEach で各要素を処理
    this.cards.forEach((card, index) => {
      card.nativeElement.style.border = '2px solid blue';
    });

    // length で要素数を取得
    console.log('総カード数:', this.cards.length);
  }
}
```

## 実践的な活用例
- 動的リストの管理
- フォーム要素の一括処理
- 条件付き要素の操作

## ベストプラクティス
- 適切なメソッドを選択する
- 変更検知を活用する
- パフォーマンスを考慮する

## 注意点
- メモリリークを防ぐ
- 適切なクリーンアップ
- 変更検知の効率性

## 関連技術
- QueryList
- 変更検知
- 効率的な操作
