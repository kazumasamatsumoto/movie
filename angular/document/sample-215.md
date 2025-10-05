# #215 「コンテンツ投影のパフォーマンス」

## 概要
Angular v20のコンテンツ投影におけるパフォーマンス最適化の手法を学習します。

## 学習目標
- コンテンツ投影のパフォーマンス特性を理解する
- 最適化手法を習得する
- 高性能なコンテンツ投影アプリケーションを実現できるようになる

## 技術ポイント
- パフォーマンス最適化
- OnPush変更検出戦略
- メモリ管理

## 📺 画面表示用コード

```typescript
// パフォーマンス最適化されたコンポーネント
@Component({
  selector: 'app-optimized-list',
  template: `
    <div class="list-container">
      @for (item of items(); track item.id) {
        <div class="list-item">
          <ng-content select="[data-item-id='{{item.id}}']"></ng-content>
        </div>
      }
    </div>
  `,
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class OptimizedListComponent {
  items = input.required<Item[]>();
  
  trackByFn(index: number, item: Item): any {
    return item.id;
  }
}
```

```html
<!-- 使用例 -->
<app-optimized-list [items]="largeDataset">
  <div *ngFor="let item of items; trackBy: trackByFn" 
       [data-item-id]="item.id" 
       class="item-content">
    <h3>{{item.title}}</h3>
    <p>{{item.description}}</p>
  </div>
</app-optimized-list>
```

```typescript
// メモ化を使用したコンポーネント
@Component({
  selector: 'app-memoized-content',
  template: `
    <div class="content-container">
      <ng-content></ng-content>
    </div>
  `,
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class MemoizedContentComponent {
  private _cachedContent: any;
  
  @Input() set data(value: any) {
    if (this._cachedContent !== value) {
      this._cachedContent = value;
      this.cdr.markForCheck();
    }
  }
  
  constructor(private cdr: ChangeDetectorRef) {}
}
```

## 実践的な活用例

```html
<!-- 仮想スクロール対応リスト -->
<app-virtual-list [items]="largeDataset" [itemHeight]="50">
  <ng-template #itemTemplate let-item>
    <div class="virtual-item">
      <h4>{{item.title}}</h4>
      <p>{{item.description}}</p>
    </div>
  </ng-template>
</app-virtual-list>
```

## ベストプラクティス
- OnPush変更検出戦略を使用する
- trackBy関数でリストの最適化を行う
- 不要な投影を避ける
- メモ化を適切に活用する

## 注意点
- 大量のコンテンツ投影でのメモリ使用量
- 変更検出の頻度
- 投影コンテンツの初期化コスト

## 関連技術
- Performance Optimization
- Change Detection
- Memory Management
