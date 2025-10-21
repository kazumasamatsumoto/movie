# #261 「Component の粒度設計」

## 概要
コンポーネントの粒度設計は、機能のまとまりを見極めて適切なサイズでコンポーネントを構成し、保守性と再利用性を確保するプロセスである。

## 学習目標
- 粒度を判断する指標を理解する
- ViewModelやInput/Outputから適切な境界を引く方法を学ぶ
- デザインシステムと連動した粒度調整を行う

## 技術ポイント
- ユーザーストーリー単位での分割
- Input/Output数による複雑度評価
- ディレクトリ構成との連携

## 📺 画面表示用コード（動画用）
```typescript
@Component({
  selector: 'app-dashboard-summary',
  standalone: true,
  template: `<app-stat-card *ngFor="let card of cards" [vm]="card"></app-stat-card>`
})
export class DashboardSummaryComponent {
  @Input({ required: true }) cards: ReadonlyArray<StatCardVm> = [];
}
```

```typescript
@Component({
  selector: 'app-stat-card',
  standalone: true,
  template: `<article><h4>{{ vm.title }}</h4><p>{{ vm.value }}</p></article>`,
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class StatCardComponent {
  @Input({ required: true }) vm!: Readonly<StatCardVm>;
}
```

```typescript
export type StatCardVm = {
  readonly title: string;
  readonly value: string;
};
```

## 💻 詳細実装例（学習用）
```typescript
@Component({
  selector: 'app-dashboard-feature',
  standalone: true,
  imports: [DashboardSummaryComponent, StatCardComponent],
  template: `
    <app-dashboard-summary [cards]="cards"></app-dashboard-summary>
    <app-stat-card *ngIf="highlight" [vm]="highlight"></app-stat-card>
  `,
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class DashboardFeatureComponent {
  @Input() cards: ReadonlyArray<StatCardVm> = [];
  @Input() highlight?: Readonly<StatCardVm>;
}
```

## ベストプラクティス
- Input/Outputが増え始めたら粒度見直しのサインと捉える
- デザインシステムのコンポーネント層と粒度を揃える
- FeatureとSharedの階層で粒度を記録しチームで共有する

## 注意点
- 細分化しすぎると依存関係が煩雑になるためバランスを取る
- 大きすぎるコンポーネントはレビュー時に視覚化して議論する
- 粒度基準を文書化し新人にも共有する

## 関連技術
- Atomic Design
- Angular Standalone Component
- Featureモジュール設計
