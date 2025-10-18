# #164 「ViewEncapsulation.None - グローバル」

## 概要
`ViewEncapsulation.None`を利用し、コンポーネントスタイルをグローバルスコープで適用する方法と注意点を整理します。

## 学習目標
- Noneモードがスタイルに与える影響を理解する
- グローバル適用が有効なユースケースを認識する
- スタイル衝突を防ぐための工夫を把握する

## 技術ポイント
- **グローバル化**: コンポーネントスタイルが`styles.css`と同じ扱いになる
- **ユーティリティ化**: 共通クラスを提供したい場合に便利
- **命名規則**: BEMやプレフィックスで衝突を回避

```typescript
@Component({
  selector: 'app-global-banner',
  templateUrl: './global-banner.component.html',
  styleUrls: ['./global-banner.component.scss'],
  encapsulation: ViewEncapsulation.None,
})
```

```html
<section class="global-banner">...</section>
```

```scss
.global-banner { background: linear-gradient(45deg, #8e24aa, #3949ab); }
```

## 💻 詳細実装例（学習用）
```typescript
// global-banner.component.ts
import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'app-global-banner',
  standalone: true,
  templateUrl: './global-banner.component.html',
  styleUrls: ['./global-banner.component.scss'],
  encapsulation: ViewEncapsulation.None,
})
export class GlobalBannerComponent {}
```

```html
<!-- global-banner.component.html -->
<section class="global-banner">
  <h2>グローバル適用バナー</h2>
  <p>Noneカプセル化なので他コンポーネントでも同じクラスが適用可能です。</p>
</section>
```

```scss
/* global-banner.component.scss */
.global-banner {
  padding: 24px;
  color: #fff;
}
```

## ベストプラクティス
- 共通ユーティリティクラスやテーマカラーなど、グローバルで共有したいスタイルのみに限定する
- クラス名にプレフィックスを付けて衝突を防ぐ（例：`app-`、`u-`）
- ドキュメント化し、どのコンポーネントがグローバルスタイルを提供しているか明示する

## 注意点
- 多用するとスタイルがスパゲッティ化し、コンポーネント単位の独立性が低下する
- CSSの読み込み順によって意図しない上書きが起こる可能性がある
- SSRでも同様にグローバルへ適用されるため、クラス名の衝突管理が必要

## 関連技術
- シングルトンテーマモジュール
- Tailwind CSSやBootstrapなどのユーティリティクラス
- Angularスタイルガイド（グローバルCSSの扱い）
