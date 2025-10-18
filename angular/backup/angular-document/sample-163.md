# #163 「ViewEncapsulation.Emulated - デフォルト」

## 概要
Angularのデフォルト設定である`ViewEncapsulation.Emulated`の仕組みとメリットを理解し、コンポーネントステートメントのカプセル化を把握します。

## 学習目標
- Emulatedモードがどのようにスタイルをスコープ化するか説明できる
- 属性セレクタによる擬似カプセル化の動作を理解する
- Emulatedでカバーできないケースを認識する

## 技術ポイント
- **擬似カプセル化**: Angularが要素へ `_ngcontent-xxxx`、スタイルへ `_nghost-xxxx`属性を付与
- **子コンポーネントへの影響**: 親スタイルは子には作用しない（::ng-deepを除く）
- **開発体験**: 通常のCSSがそのまま使え、特別な構文は不要

```typescript
@Component({
  selector: 'app-card',
  templateUrl: './card.component.html',
  styleUrls: ['./card.component.scss'],
  encapsulation: ViewEncapsulation.Emulated,
})
```

```html
<article class="card">...</article>
```

```scss
.card { border-radius: 8px; }
```

## 💻 詳細実装例（学習用）
```typescript
// emulated-card.component.ts
import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'app-emulated-card',
  standalone: true,
  templateUrl: './emulated-card.component.html',
  styleUrls: ['./emulated-card.component.scss'],
  encapsulation: ViewEncapsulation.Emulated,
})
export class EmulatedCardComponent {}
```

```html
<!-- emulated-card.component.html -->
<article class="card">
  <h3>Emulated カプセル化</h3>
  <p>同名クラスでもコンポーネント内に限定されます。</p>
</article>
```

```scss
/* emulated-card.component.scss */
.card {
  padding: 16px;
  border: 1px solid #e0e0e0;
}
```

## ベストプラクティス
- 特別な理由がない限りEmulatedを利用し、スタイル衝突を防ぐ
- カプセル化されたスタイル内で`@media`や`:host`など通常のCSS構文をそのまま活用する
- 共通スタイルはSCSSの`@use`やCSS変数で共有し、Emulated上でも再利用しやすくする

## 注意点
- Emulatedでも継承プロパティ（font-family等）は親の影響を受ける場合がある
- テスト環境では属性名が最適化されるため、DOMアサーションの方法に注意する
- Emulatedのままでは外部Web ComponentsのShadow DOM内にスタイルを届けられない

## 関連技術
- `ViewEncapsulation.None` / `ShadowDom`
- ::ng-deep（非推奨）と代替手段
- Angularスタイルガイドライン
