# #279 「UI Component Library の構築」

## 概要
UI Component Libraryは、共通UIパターンとデザインシステム資産を集約し、複数プロジェクトで一貫した体験を提供するためのコンポーネント集である。

## 学習目標
- ライブラリ構築の初期ステップを理解する
- StorybookとVisual Regressionで品質を担保する
- npmパッケージ化やバージョニング戦略を学ぶ

## 技術ポイント
- Design Tokenの定義
- Storybookによるドキュメント自動化
- Visual Regressionテスト

## 📺 画面表示用コード（動画用）
```typescript
export const TOKENS = {
  colorPrimary: '#6200ee',
  spacingSm: '8px',
} as const;
```

```typescript
@Component({
  selector: 'ui-button',
  standalone: true,
  template: `<button class="ui-button">{{ label }}</button>`
})
export class UiButtonComponent {
  @Input({ required: true }) label = '';
}
```

```typescript
export default {
  title: 'Button',
  component: UiButtonComponent,
} satisfies Meta<UiButtonComponent>;
```

## 💻 詳細実装例（学習用）
```typescript
@Component({
  selector: 'ui-library-module',
  standalone: true,
  imports: [UiButtonComponent],
  template: `<ui-button label="実行"></ui-button>`
})
export class UiLibraryModuleComponent {}
```

## ベストプラクティス
- Design Tokenを単一ソースとして扱い、コンポーネントやCSS変数に適用する
- StorybookでアクセシビリティアドオンやVisual Regressionを組み合わせる
- バージョン管理とCHANGELOGを自動生成し利用者へ明示する

## 注意点
- ライブラリの破壊的変更にはメジャーバージョンを上げる
- コンポーネントが肥大化したらサブパッケージ化を検討する
- トークン値はデザインチームと同期を取る

## 関連技術
- Design Token
- Storybook
- Visual Regression Testing
