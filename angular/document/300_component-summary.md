# #300 「Component 総まとめと実践プロジェクト」

## 概要
Component編の締めくくりとして、基礎UIからFeature実装までを統合し、責務分離・状態管理・アクセシビリティを揃えた実践プロジェクト構成を整理する。

## 学習目標
- 基礎コンポーネント/Sharedコンポーネント/Featureコンポーネントの役割を再確認する
- Smart/Dumb + Signalsを組み合わせた設計を復習する
- Storybook・テスト・ドキュメンテーションを含む開発フローを把握する

## 技術ポイント
- Standalone構成のレイヤリング
- Signals + ControlValueAccessor
- Storybook/Testingワークフロー

## 📺 画面表示用コード（動画用）
```typescript
@Component({ selector: 'app-ui-kit', standalone: true, imports: [ButtonComponent, InputComponent, SelectComponent], template: `<app-button label="保存" (pressed)="save.emit()"></app-button><app-input formControlName="name" label="名前"></app-input><app-select formControlName="role" label="権限" [options]="roles"></app-select>` })
export class UiKitComponent {
  @Input({ required: true }) roles!: ReadonlyArray<SelectOption<string>>;
  @Output() save = new EventEmitter<void>();
}
```

```typescript
@Component({ selector: 'app-feature-dashboard', standalone: true, imports: [UiKitComponent, CardComponent, ChartComponent], template: `<ui-kit [roles]="roles" (save)="onSave()"></ui-kit><app-card *ngFor="let item of vm().cards" [attr.data-elevation]="item.elevation"><h3 slot="header">{{ item.title }}</h3><p>{{ item.description }}</p></app-card>` })
export class FeatureDashboardComponent {
  private readonly store = inject(DashboardStore);
  readonly vm = this.store.vm;
  readonly roles = this.store.roles;
  onSave(): void { this.store.persist(); }
}
```

```typescript
describe('FeatureDashboardComponent', () => {
  it('renders cards', async () => {
    await render(FeatureDashboardComponent, { componentProviders: [{ provide: DashboardStore, useValue: mockStore }] });
    expect(screen.getAllByRole('heading').length).toBeGreaterThan(0);
  });
});
```

## 💻 詳細実装例（学習用）
```markdown
1. 基礎UIライブラリ: Button/Input/Select/Badge/ModalなどをStorybookで管理
2. Featureレイヤー: Container + PresentationのペアとSignal Storeで状態管理
3. Project Setup: Lint + Unit Test + AccessibilityチェックをCIで自動実行
4. ドキュメント: Figma/Storybook/ADRでデザインと実装の同期を維持
```

## ベストプラクティス
- コンポーネントはUI、状態、ドメインのレイヤーに分けて責務を明確化する
- SignalsとControlValueAccessorを組み合わせてフォームと状態を統合する
- Storybook・Unit Test・Accessibility監査を自動化し回帰を防ぐ

## 注意点
- 基盤コンポーネントの変更は影響範囲が広いためADRで記録する
- 状態管理とUIの境界が崩れたらリファクタリングを計画する
- デザインシステムとの同期を定期的にレビューする

## 関連技術
- Standalone Component
- Angular Signals
- Storybook / Testing Library
