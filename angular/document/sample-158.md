# #158 「QueryList のメソッド活用」

## 概要
Angular v20におけるQueryListの豊富なメソッド活用。forEach、map、filter、findなどの配列ライクなメソッドを使用して、効率的で読みやすい要素操作を実現する方法を学ぶ。

## 学習目標
- QueryListの主要メソッドを理解する
- 効率的な要素操作を学ぶ
- 配列ライクな操作を把握する

## 技術ポイント
- QueryList.forEach() での反復処理
- QueryList.map() での変換
- QueryList.filter() での絞り込み
- QueryList.find() での検索

## 📺 画面表示用コード

### QueryListメソッドの活用
```typescript
@Component({
  selector: 'app-query-methods',
  template: `
    <div #item *ngFor="let item of items" class="item" 
         [class.active]="item.active">
      {{ item.name }}
    </div>
    <div class="controls">
      <button (click)="processAll()">全項目処理</button>
      <button (click)="processActive()">アクティブのみ処理</button>
      <button (click)="findFirstActive()">最初のアクティブ検索</button>
    </div>
    <p>アクティブ項目数: {{ activeCount }}</p>
  `
})
export class QueryMethodsComponent implements AfterViewInit {
  @ViewChildren('item') items!: QueryList<ElementRef>;
  data = [
    { name: '項目1', active: true },
    { name: '項目2', active: false },
    { name: '項目3', active: true },
    { name: '項目4', active: false }
  ];

  ngAfterViewInit() {
    this.updateActiveCount();
  }

  processAll() {
    // forEach で全要素を処理
    this.items.forEach((item, index) => {
      item.nativeElement.style.border = '1px solid #ccc';
      item.nativeElement.setAttribute('data-index', index.toString());
    });
  }

  processActive() {
    // filter でアクティブ要素のみを処理
    const activeElements = this.items.filter(item => 
      item.nativeElement.classList.contains('active')
    );
    
    activeElements.forEach(item => {
      item.nativeElement.style.backgroundColor = 'yellow';
    });
  }

  findFirstActive() {
    // find で最初のアクティブ要素を検索
    const firstActive = this.items.find(item => 
      item.nativeElement.classList.contains('active')
    );
    
    if (firstActive) {
      firstActive.nativeElement.style.border = '3px solid red';
      console.log('最初のアクティブ要素を見つけました');
    }
  }

  private updateActiveCount() {
    this.activeCount = this.items.filter(item => 
      item.nativeElement.classList.contains('active')
    ).length;
  }
}
```

## 実践的な活用例
- 条件付き要素処理
- 要素の検索と絞り込み
- 一括操作の実装

## ベストプラクティス
- 適切なメソッドの選択
- 効率的な処理の実装
- 可読性の向上

## 注意点
- パフォーマンスの考慮
- メモリ使用量の管理
- 適切なエラーハンドリング

## 関連技術
- 配列操作
- 要素フィルタリング
- 効率的な処理
