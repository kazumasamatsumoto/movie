# #278 「Shared Component の設計」

## 概要
Shared Componentは複数のFeatureで再利用されるUIコンポーネントで、統一された入力と拡張ポイントを提供することで組織全体の開発効率を高める。

## 学習目標
- Shared Componentの選定基準を理解する
- 拡張性とカスタマイズ可能なAPIを設計する
- テーマやスタイルを汎用的に適用する手法を学ぶ

## 技術ポイント
- Standalone Componentとして公開
- OptionalなInputとSlot
- CSSカスタムプロパティでのテーマ切り替え

## 📺 画面表示用コード（動画用）
```typescript
@Component({
  selector: 'app-shared-button',
  standalone: true,
  template: `<button class="shared" [class.outlined]="variant==='outlined'">{{ label }}</button>`
})
export class SharedButtonComponent {
  @Input({ required: true }) label = '';
  @Input() variant: 'filled' | 'outlined' = 'filled';
}
```

```typescript
@Component({
  selector: 'app-shared-card',
  standalone: true,
  template: `<section class="card"><header>{{ title }}</header><ng-content></ng-content></section>`
})
export class SharedCardComponent {
  @Input({ required: true }) title = '';
}
```

```typescript
export type SharedButtonConfig = {
  readonly label: string;
  readonly variant?: 'filled' | 'outlined';
};
```

## 💻 詳細実装例（学習用）
```typescript
@Component({
  selector: 'app-shared-showcase',
  standalone: true,
  imports: [SharedButtonComponent, SharedCardComponent],
  template: `
    <app-shared-card title="告知">
      <p>{{ message }}</p>
      <app-shared-button [label]="button.label" [variant]="button.variant ?? 'filled'"></app-shared-button>
    </app-shared-card>
  `
})
export class SharedShowcaseComponent {
  @Input({ required: true }) message = '';
  @Input({ required: true }) button!: Readonly<SharedButtonConfig>;
}
```

## ベストプラクティス
- Shared Componentはスタイルとアクセシビリティを含めてドキュメント化する
- OptionalなInputで拡張性を提供し、デフォルト値を設定する
- npmパッケージやStorybookで利用方法をカタログ化する

## 注意点
- ビジネスロジックが入り込まないようにする
- テーマ切り替え時にCSS変数の命名を統一する
- バージョンアップ時は互換性に注意し破壊的変更を明示する

## 関連技術
- デザインシステム
- Storybook
- Angular Standalone Component
