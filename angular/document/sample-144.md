# #144 「ViewChildren 変更監視」

## 概要
Angular v20におけるViewChildrenのQueryListを使った変更監視。changesイベントで要素の追加・削除をリアルタイムで検知し、動的な要素管理を実現する方法を学ぶ。

## 学習目標
- QueryListの変更検知機能を理解する
- changesイベントの活用方法を学ぶ
- 動的要素管理を把握する

## 技術ポイント
- QueryList.changes イベント
- 要素の追加・削除検知
- 動的な要素管理
- リアルタイム更新

## 📺 画面表示用コード

### 変更監視の実装
```typescript
@Component({
  selector: 'app-change-detection',
  template: `
    <div #item *ngFor="let item of items" class="item">
      {{ item }}
    </div>
    <div class="controls">
      <button (click)="addItem()">項目追加</button>
      <button (click)="removeItem()">項目削除</button>
    </div>
    <p>現在の項目数: {{ itemCount }}</p>
  `
})
export class ChangeDetectionComponent implements AfterViewInit, OnDestroy {
  @ViewChildren('item') items!: QueryList<ElementRef>;
  data = ['項目1', '項目2'];
  itemCount = 0;
  private subscription?: Subscription;

  ngAfterViewInit() {
    this.itemCount = this.items.length;
    
    this.subscription = this.items.changes.subscribe((queryList) => {
      console.log('要素が変更されました:', queryList.length);
      this.itemCount = queryList.length;
      this.updateItemStyles();
    });
  }

  ngOnDestroy() {
    this.subscription?.unsubscribe();
  }

  addItem() {
    this.data.push(`項目${this.data.length + 1}`);
  }

  removeItem() {
    if (this.data.length > 0) {
      this.data.pop();
    }
  }

  private updateItemStyles() {
    this.items.forEach((item, index) => {
      item.nativeElement.style.backgroundColor = 
        index % 2 === 0 ? 'lightblue' : 'lightgreen';
    });
  }
}
```

## 実践的な活用例
- 動的リストの管理
- リアルタイム更新
- 要素数の追跡

## ベストプラクティス
- 適切なクリーンアップ
- メモリリークの防止
- 効率的な変更処理

## 注意点
- サブスクリプションの管理
- パフォーマンスの考慮
- 無限ループの回避

## 関連技術
- 変更検知
- Subscription管理
- 動的要素管理
