# #280 「Component 設計のベストプラクティス」

## 概要
コンポーネント設計のベストプラクティスは、責務分離・パフォーマンス・再利用性を総合的に高めるためのガイドラインであり、Angular開発における品質基準となる。

## 学習目標
- コンポーネント設計で重視すべき観点を横断的に理解する
- OnPushとSignalを活用したパフォーマンス最適化を押さえる
- ドキュメントとレビューで品質を維持する手段を学ぶ

## 技術ポイント
- 責務分離（Container/Presentation）
- OnPush + Signalsによる効率的な状態管理
- ConfigとSlotでの拡張性確保

## 📺 画面表示用コード（動画用）
```typescript
@Component({ selector: 'app-feature-shell', standalone: true, imports: [FeatureContainerComponent], template: `<feature-container></feature-container>` })
export class FeatureShellComponent {}
```

```typescript
@Component({ selector: 'app-feature-container', standalone: true, imports: [FeatureViewComponent], template: `<feature-view [vm]="vm()" (action)="handle($event)"></feature-view>` })
export class FeatureContainerComponent {
  private readonly store = inject(FeatureStore);
  readonly vm = this.store.vm;
  handle(evt: FeatureAction): void { this.store.dispatch(evt); }
}
```

```typescript
export type FeatureGuideline = {
  readonly responsibility: string;
  readonly qualityGate: string;
};
```

## 💻 詳細実装例（学習用）
```markdown
- 責務分離: ContainerがStateとCommandを扱い、PresentationはUI表示に集中する
- パフォーマンス: OnPush + readonly Signalで予測可能な再レンダー
- テスト: HarnessとTesting LibraryでDOM/アクセシビリティを検証
- ドキュメント: StorybookとADRで設計意図を共有
```

## ベストプラクティス
- ViewModelを型で定義しInput/Output契約を明文化する
- Signal Storeを活用して状態と副作用を一元管理する
- Storybook/テスト/ADRをセットで保守し知識を共有する

## 注意点
- 原則の適用コストと効果を評価し過剰設計を避ける
- チームでベストプラクティスを定期的にレビューし更新する
- 新機能追加時は既存の原則に照らして整合性を確認する

## 関連技術
- Angular Signals
- Storybook
- Architecture Decision Record
