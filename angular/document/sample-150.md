# #150 「ContentChildren QueryList 活用」

## 概要
Angular v20におけるContentChildrenのQueryListを活用した高度な投影コンテンツ管理。changesイベント、forEach、filterなどの機能を使った効率的な動的コンテンツ制御を学ぶ。

## 学習目標
- ContentChildrenのQueryList活用方法を理解する
- 変更検知機能を学ぶ
- 高度なコンテンツ制御を把握する

## 技術ポイント
- QueryList.changes イベント
- forEach での反復処理
- filter での絞り込み
- 動的なコンテンツ管理

## 📺 画面表示用コード

### QueryListの高度な活用
```typescript
@Component({
  selector: 'app-advanced-container',
  template: `
    <div class="container">
      <ng-content></ng-content>
    </div>
    <div class="controls">
      <button (click)="processItems()">項目処理</button>
      <button (click)="filterActive()">アクティブのみ表示</button>
    </div>
    <p>総数: {{ totalCount }}, アクティブ: {{ activeCount }}</p>
  `
})
export class AdvancedContainerComponent implements AfterContentInit, OnDestroy {
  @ContentChildren('.item') items!: QueryList<ElementRef>;
  totalCount = 0;
  activeCount = 0;
  private subscription?: Subscription;

  ngAfterContentInit() {
    this.updateCounts();
    
    this.subscription = this.items.changes.subscribe(() => {
      this.updateCounts();
      this.processNewItems();
    });
  }

  ngOnDestroy() {
    this.subscription?.unsubscribe();
  }

  processItems() {
    this.items.forEach((item, index) => {
      const element = item.nativeElement;
      element.style.border = '1px solid #ccc';
      element.setAttribute('data-index', index.toString());
    });
  }

  filterActive() {
    this.items.forEach(item => {
      const element = item.nativeElement;
      const isActive = element.classList.contains('active');
      element.style.display = isActive ? 'block' : 'none';
    });
  }

  private updateCounts() {
    this.totalCount = this.items.length;
    this.activeCount = this.items.filter(item => 
      item.nativeElement.classList.contains('active')
    ).length;
  }

  private processNewItems() {
    // 新しく追加されたアイテムの処理
    this.items.forEach(item => {
      if (!item.nativeElement.hasAttribute('processed')) {
        item.nativeElement.setAttribute('processed', 'true');
        item.nativeElement.style.opacity = '0.8';
      }
    });
  }
}
```

## 実践的な活用例
- 動的リスト管理
- フィルタリング機能
- リアルタイム更新

## ベストプラクティス
- 適切なクリーンアップ
- 効率的な変更処理
- パフォーマンスの考慮

## 注意点
- メモリリークの防止
- 無限ループの回避
- 適切なエラーハンドリング

## 関連技術
- 動的コンテンツ管理
- 変更検知
- 効率的な操作
