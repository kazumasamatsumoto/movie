# #168 「::ng-deep - 子孫セレクタ（非推奨）」

## 概要
`::ng-deep`擬似セレクタの役割と非推奨である理由を整理し、代替手段を検討します。

## 学習目標
- `::ng-deep`が何をしていたのか説明できる
- なぜ非推奨になったのか理解し、代替手段を提示できる
- グローバルスタイルやCSS変数への移行戦略を把握する

## 技術ポイント
- **役割**: カプセル化されたスタイルを子孫コンポーネントへ適用
- **非推奨理由**: カプセル化の破壊、将来互換性がなくなる
- **代替策**: グローバルスタイル、テーマ用CSS、`ViewEncapsulation.None`、CSSカスタムプロパティ

```scss
/* ❌ 非推奨 */
:host ::ng-deep app-child .title {
  color: #ef5350;
}
```

```scss
/* ✅ 代替: global.scss */
app-child .title {
  color: #ef5350;
}
```

```typescript
encapsulation: ViewEncapsulation.None
```

## 💻 詳細実装例（学習用）
```scss
/* styles.scss グローバルテーマ例 */
.dark-theme app-child .title {
  color: #ffee58;
}
```

```typescript
// theme.directive.ts
import { Directive, HostBinding, Input } from '@angular/core';

@Directive({
  selector: '[appThemeToggle]',
  standalone: true,
})
export class ThemeToggleDirective {
  @HostBinding('class.dark-theme')
  @Input()
  dark = false;
}
```

## ベストプラクティス
- `::ng-deep`を使わず、テーマやグローバルスタイルファイルで共有スタイルを管理する
- 子コンポーネント側でInputやCSS変数を受け取れるよう設計し、拡張性を確保する
- ライブラリ側ではドキュメントで拡張ポイント（CSS変数、クラス名等）を明示する

## 注意点
- 最新バージョンでは`::ng-deep`が警告対象となり、将来的に削除される可能性が高い
- 既存コードで`::ng-deep`を使っている場合は段階的に代替へ移行する
- グローバルスタイルへ移行する際はクラス衝突に注意する

## 関連技術
- CSSカスタムプロパティ
- ViewEncapsulation設定
- Angular Materialのテーマ拡張方法
