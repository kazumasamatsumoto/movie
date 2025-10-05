# #143 「ViewChildren での反復処理」

## 概要
Angular v20におけるViewChildrenのQueryListを使った反復処理。forEach、map、filterなどのメソッドで効率的な複数要素の操作を実現する方法を学ぶ。

## 学習目標
- QueryListの反復処理メソッドを理解する
- 一括操作の実装方法を学ぶ
- パフォーマンスを考慮した処理を把握する

## 技術ポイント
- QueryList.forEach() での反復処理
- 一括スタイル変更
- 条件付き処理
- 効率的な操作

## 📺 画面表示用コード

### 反復処理の実装
```typescript
@Component({
  selector: 'app-iteration',
  template: `
    <div #item *ngFor="let item of items" class="item">
      {{ item.name }}
    </div>
    <div class="controls">
      <button (click)="selectAll()">全選択</button>
      <button (click)="deselectAll()">全解除</button>
      <button (click)="toggleOdd()">奇数切り替え</button>
    </div>
  `
})
export class IterationComponent implements AfterViewInit {
  @ViewChildren('item') items!: QueryList<ElementRef>;
  data = [
    { name: '項目1' },
    { name: '項目2' },
    { name: '項目3' },
    { name: '項目4' }
  ];

  ngAfterViewInit() {
    console.log('要素数:', this.items.length);
  }

  selectAll() {
    this.items.forEach((item) => {
      item.nativeElement.classList.add('selected');
    });
  }

  deselectAll() {
    this.items.forEach((item) => {
      item.nativeElement.classList.remove('selected');
    });
  }

  toggleOdd() {
    this.items.forEach((item, index) => {
      if (index % 2 === 0) {
        item.nativeElement.classList.toggle('odd');
      }
    });
  }
}
```

## 実践的な活用例
- リストの一括選択
- フォーム要素の一括処理
- 動的スタイルの適用

## ベストプラクティス
- 効率的な反復処理
- 適切な条件分岐
- パフォーマンスの考慮

## 注意点
- 大量要素での処理時間
- メモリ使用量の管理
- 適切なエラーハンドリング

## 関連技術
- 反復処理
- 一括操作
- パフォーマンス最適化
