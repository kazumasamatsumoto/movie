# #190 「スタイリングのベストプラクティス」

## 概要
Angularアプリでスタイルを設計・運用する際の総合的なベストプラクティスをまとめ、保守性と一貫性の高いスタイルガイドを築くための指針を整理します。

## 学習目標
- コンポーネントスタイルとグローバルスタイルの役割分担を理解する
- 命名規則・デザイントークン・テーマ管理など、長期運用に必要なスタイル設計手法を学ぶ
- パフォーマンス・アクセシビリティを意識したスタイル設計を実践できるようになる

## 技術ポイント
- **分離**: コンポーネント固有スタイルは`styleUrls`、共通スタイルは`styles.scss`
- **命名規則**: BEMやFSDなど統一したルールでクラス名を付ける
- **デザイントークン**: SCSS変数・CSSカスタムプロパティでカラー/スペーシングを一元管理

## 📺 画面表示用コード（動画用）

```scss
/* BEM命名 */
.card {}
.card__title {}
.card--highlight {}
```

```scss
:root {
  --spacing-md: 16px;
}
```

```scss
@media (prefers-reduced-motion: reduce) {
  * {
    transition: none;
  }
}
```

## 💻 詳細実装例（学習用）
```scss
/* styles/_tokens.scss */
$spacing-md: 16px;
$radius-md: 12px;
$color-primary: #1976d2;

:root {
  --spacing-md: #{$spacing-md};
  --radius-md: #{$radius-md};
  --color-primary: #{$color-primary};
}
```

```scss
/* card.component.scss */
@use 'styles/tokens' as tokens;

.card {
  padding: tokens.$spacing-md;
  border-radius: tokens.$radius-md;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.15);
}

.card--primary {
  border-left: 4px solid var(--color-primary);
}
```

```typescript
// theming.service.ts（デザイントークン更新例）
import { Injectable, Renderer2, RendererFactory2 } from '@angular/core';

@Injectable({ providedIn: 'root' })
export class ThemingService {
  private renderer: Renderer2;

  constructor(rendererFactory: RendererFactory2) {
    this.renderer = rendererFactory.createRenderer(null, null);
  }

  setSpacingMd(value: string): void {
    this.renderer.setStyle(document.documentElement, '--spacing-md', value);
  }
}
```

## ベストプラクティス
- スタイルガイド（デザイントークン、コンポーネントサンプル、明確な命名規則）をドキュメント化し、チーム内で共有する
- CSS変数とSCSSを組み合わせ、ビルド時・ランタイムの両方でテーマを変更できるようにする
- モバイル・アクセシビリティ・パフォーマンスを考慮し、LighthouseやStorybook等で継続的に検証する
- コンポーネント単位の責務を明確にし、再利用可能なUI部品を整備する（Design System）

## 注意点
- グローバルスタイルの肥大化に注意し、定期的に未使用スタイルを取り除く
- ViewEncapsulation.Noneを安易に利用するとスタイルが衝突しやすい
- `::ng-deep`や複雑なセレクタに頼ると保守が困難になるため、構造から見直す

## 関連技術
- デザインシステム/Style Dictionary
- StorybookでのUIコンポーネント管理
- Tailwind CSSやAngular Materialなど既存スタイルライブラリの活用
