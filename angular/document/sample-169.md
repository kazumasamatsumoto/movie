# #169 「Component 固有スタイルの適用」

## 概要
コンポーネント専用のスタイルを整理し、メンテナンスしやすい構造で適用する方法を紹介します。

## 学習目標
- コンポーネント固有スタイルのファイル構成を理解する
- クラス命名やSCSS構造を整えて再利用性を高める手法を習得する
- コンポーネントとグローバルスタイルの責務分離を把握する

## 技術ポイント
- **styleUrls**でスタイルを外部ファイル化
- **BEM記法**など命名規則で可読性を確保
- **SCSS部分化**: `_mixins.scss`や`_variables.scss`を共通化し、各コンポーネントでインポート

## 📺 画面表示用コード（動画用）

```typescript
styleUrls: ['./profile-card.component.scss']
```

```scss
.profile-card { ... }
```

```scss
.profile-card__name { font-weight: bold; }
```

## 💻 詳細実装例（学習用）
```typescript
// profile-card.component.ts
import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-profile-card',
  standalone: true,
  templateUrl: './profile-card.component.html',
  styleUrls: ['./profile-card.component.scss'],
})
export class ProfileCardComponent {
  @Input() name = '';
  @Input() role = '';
}
```

```html
<!-- profile-card.component.html -->
<article class="profile-card">
  <h3 class="profile-card__name">{{ name }}</h3>
  <p class="profile-card__role">{{ role }}</p>
</article>
```

```scss
/* profile-card.component.scss */
@use '../styles/mixins' as mixins;

.profile-card {
  padding: 16px;
  border-radius: 16px;
  background: #ffffff;
  box-shadow: mixins.card-shadow();

  &__name {
    font-weight: 600;
    margin-bottom: 4px;
  }

  &__role {
    color: #607d8b;
  }
}
```

## ベストプラクティス
- コンポーネントごとのスタイルファイルを作り、1ファイル1責務で管理する
- 共通色や影などはSCSSの変数・ミックスインにまとめて再利用する
- 役割を明確にしたクラス命名（BEMなど）でDOM構造の意図が伝わるようにする

## 注意点
- 長いセレクタチェーンはブラウザのマッチングコストを増やすので避ける
- グローバルCSSへ依存しすぎるとコンポーネントが独立しなくなる
- `ViewEncapsulation.None`を使う場合、クラス命名を厳格にし衝突を防ぐ

## 関連技術
- SCSSモジュール化（`@use`, `@forward`）
- デザインシステム/スタイルガイド
- Angular CLIのスタイル生成オプション
