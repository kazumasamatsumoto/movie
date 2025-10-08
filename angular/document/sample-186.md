# #186 「メディアクエリの活用」

## 概要
レスポンシブデザインの基盤となるCSSメディアクエリの使い方を整理し、Angularコンポーネントでも容易に適用できる記述スタイルを紹介します。

## 学習目標
- CSSメディアクエリの基本構文（`max-width`, `min-width`, `prefers-color-scheme`など）を理解する
- コンポーネントスタイルでのメディアクエリ適用方法を習得する
- SCSSの変数やミックスインを使ってブレークポイント管理を簡略化する

## 技術ポイント
- **基本構文**: `@media (max-width: 600px) { ... }`
- **複合条件**: `@media (min-width: 768px) and (orientation: landscape)`
- **SCSS補助**: ブレークポイント変数やミックスインで共通化

## 📺 画面表示用コード（動画用）

```scss
@media (max-width: 600px) {
  :host {
    padding: 12px;
  }
}
```

```scss
@media (prefers-reduced-motion: reduce) {
  :host {
    transition: none;
  }
}
```

```scss
@use 'styles/breakpoints' as bp;
@media (max-width: bp.$tablet) { ... }
```

## 💻 詳細実装例（学習用）
```scss
/* styles/_breakpoints.scss */
$mobile: 600px;
$tablet: 768px;
$desktop: 1024px;

@mixin respond-to($device) {
  @if $device == mobile {
    @media (max-width: $mobile) { @content; }
  } @else if $device == tablet {
    @media (max-width: $tablet) { @content; }
  } @else if $device == desktop {
    @media (max-width: $desktop) { @content; }
  }
}
```

```scss
/* card.component.scss */
@use 'styles/breakpoints' as bp;

:host {
  display: grid;
  grid-template-columns: 240px 1fr;
  gap: 24px;
}

@include bp.respond-to(tablet) {
  :host {
    grid-template-columns: 1fr;
    gap: 16px;
  }
}
```

## ベストプラクティス
- ブレークポイント値をSCSSファイルにまとめ、ミックスインで簡潔に記述する
- モバイルファーストで書き、必要に応じて`min-width`で上書きする
- `prefers-reduced-motion`や`prefers-color-scheme`などアクセシビリティ用メディアクエリも活用する

## 注意点
- `ViewEncapsulation.Emulated`でもメディアクエリはそのままコンパイルされて有効
- ブレークポイントが多すぎるとスタイルが複雑化するため、デザインシステムに沿った固定ブレークポイントを推奨
- メディアクエリよりコンポーネント分割やCSS Gridを使った柔軟レイアウトを検討する場合もある

## 関連技術
- Angular CDK BreakPointObserver
- CSS GridとFlexbox
- Tailwind CSSなどレスポンシブユーティリティフレームワーク
