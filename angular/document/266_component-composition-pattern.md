# #266 「Component Composition パターン」

## 概要
Component Compositionパターンは、複数の小さなコンポーネントやテンプレートを組み合わせて機能を構築し、責務を分割しながら柔軟なUIを構成する設計手法である。

## 学習目標
- コンポーネントを組み合わせるスロット設計を理解する
- Context APIでデータを渡すパターンを学ぶ
- テストシナリオでコンポジションを検証する

## 技術ポイント
- ng-contentとngTemplateOutlet
- Context API (`let-`構文)
- Signalでの状態供給

## 📺 画面表示用コード（動画用）
```html
<app-list-composer [items]="items">
  <ng-template let-item>
    <app-item-card [vm]="item"></app-item-card>
  </ng-template>
</app-list-composer>
```

```typescript
@Component({ selector: 'app-list-composer', standalone: true, imports: [NgFor, NgTemplateOutlet], template: `<ng-container *ngFor="let item of items"><ng-container *ngTemplateOutlet="content; context: {$implicit: item}"></ng-container></ng-container>` })
export class ListComposerComponent<T> {
  @Input({ required: true }) items: ReadonlyArray<T> = [];
  @ContentChild(TemplateRef) content?: TemplateRef<T>;
}
```

```typescript
@Component({
  selector: 'app-item-card',
  standalone: true,
  template: `<article><h4>{{ vm.title }}</h4><p>{{ vm.detail }}</p></article>`
})
export class ItemCardComponent {
  @Input({ required: true }) vm!: Readonly<ItemVm>;
}
```

## 💻 詳細実装例（学習用）
```typescript
@Component({
  selector: 'app-item-list',
  standalone: true,
  imports: [ListComposerComponent, ItemCardComponent],
  template: `
    <app-list-composer [items]="vm()">
      <ng-template let-item>
        <app-item-card [vm]="item"></app-item-card>
      </ng-template>
    </app-list-composer>
  `
})
export class ItemListComponent {
  private readonly items = signal<ReadonlyArray<ItemVm>>([]);
  readonly vm = this.items.asReadonly();

  setItems(list: ReadonlyArray<ItemVm>): void {
    this.items.set(list);
  }
}
```

## ベストプラクティス
- SlotとContextの契約をドキュメント化し利用側に明確に伝える
- 小さなコンポーネントを組み合わせる際はInput型を共通化する
- Signalでの供給元を一箇所にまとめてテスト容易性を高める

## 注意点
- Slot数が多い場合はConfigオブジェクトなどの別パターンも検討する
- TemplateRefが未提供の場合のフォールバックを用意する
- Contextが複雑な場合は型エイリアスで整える

## 関連技術
- Content Projection
- Angular Signals
- TemplateRef/Context API
