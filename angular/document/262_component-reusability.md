# #262 「Component の再利用性向上」

## 概要
コンポーネントの再利用性を高めるには、明確な契約と柔軟な拡張ポイントを設計し、他プロジェクトでも流用できるよう依存を最小限に保つ必要がある。

## 学習目標
- ViewModelとInput/Outputで拡張しやすい契約を設計する
- ng-contentやテンプレート差し替えでカスタマイズ性を提供する
- 依存を外部化して複数コンテキストで再利用する

## 技術ポイント
- Standalone Component化
- Content Projectionの活用
- CSSカスタムプロパティによるスタイル調整

## 📺 画面表示用コード（動画用）
```typescript
@Component({
  selector: 'app-card-shell',
  standalone: true,
  template: `<article class="card"><header>{{ title }}</header><ng-content></ng-content></article>`
})
export class CardShellComponent {
  @Input({ required: true }) title = '';
}
```

```typescript
@Component({ selector: 'app-card-list', standalone: true, imports: [CardShellComponent], template: `<app-card-shell *ngFor="let vm of items" [title]="vm.title">{{ vm.body }}</app-card-shell>` })
export class CardListComponent {
  @Input({ required: true }) items: ReadonlyArray<CardVm> = [];
}
```

```typescript
export type CardVm = {
  readonly title: string;
  readonly body: string;
};
```

## 💻 詳細実装例（学習用）
```typescript
@Component({
  selector: 'app-card-feature',
  standalone: true,
  imports: [CardListComponent, CardShellComponent, NgTemplateOutlet],
  template: `
    <app-card-list [items]="items"></app-card-list>
    <app-card-shell title="カスタム">
      <ng-container *ngTemplateOutlet="action"></ng-container>
    </app-card-shell>

    <ng-template #action>
      <button type="button" class="accent" (click)="onAction()">Action</button>
    </ng-template>
  `
})
export class CardFeatureComponent {
  @Input({ required: true }) items: ReadonlyArray<CardVm> = [];
  @Output() action = new EventEmitter<void>();

  onAction(): void {
    this.action.emit();
  }
}
```

## ベストプラクティス
- ViewModelを共有型で公開し、利用側にも型情報を提供する
- カスタマイズはng-contentやテンプレートOutletで提供し、条件分岐を増やさない
- Storybookでバリエーションをカタログ化して再利用例を示す

## 注意点
- コンポーネント内で特定サービスに依存しすぎない
- Inputが増えた場合はConfigオブジェクト化を検討する
- スタイルの指定はCSS変数やカスタムプロパティで上書き可能にする

## 関連技術
- Content Projection
- Storybook
- Configオブジェクトパターン
