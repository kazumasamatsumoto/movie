# #165 「ViewEncapsulation.ShadowDom - Shadow DOM」

## 概要
`ViewEncapsulation.ShadowDom`を利用してブラウザのShadow DOM機能を有効化し、コンポーネントをWeb Components同等の完全カプセル化で提供する方法を学びます。

## 学習目標
- Shadow DOMモードの特徴と利点を理解する
- 外部スタイルが届かないことによる設計上の注意点を把握する
- Web Componentsとの互換性を確保したいケースを認識する

## 技術ポイント
- **ShadowRoot生成**: コンポーネント要素に`attachShadow({ mode: 'open' })`が自動で行われる
- **スタイル隔離**: 外部スタイルシートが届かないため、必要なCSSは内部で読み込む
- **カスタムイベント**: Web Components同様、Shadow DOM内から外へイベント伝達が必要な場合は`dispatchEvent`を使う

## 📺 画面表示用コード（動画用）

```typescript
@Component({
  selector: 'app-shadow-card',
  templateUrl: './shadow-card.component.html',
  styleUrls: ['./shadow-card.component.scss'],
  encapsulation: ViewEncapsulation.ShadowDom,
})
```

```html
<article class="card">Shadow DOM</article>
```

```scss
.card { box-shadow: 0 4px 12px rgba(0,0,0,0.15); }
```

## 💻 詳細実装例（学習用）
```typescript
// shadow-card.component.ts
import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'app-shadow-card',
  standalone: true,
  templateUrl: './shadow-card.component.html',
  styleUrls: ['./shadow-card.component.scss'],
  encapsulation: ViewEncapsulation.ShadowDom,
})
export class ShadowCardComponent {}
```

```html
<!-- shadow-card.component.html -->
<article class="card">
  <h3>Shadow DOM カード</h3>
  <p>外部CSSに影響されません。</p>
</article>
```

```scss
/* shadow-card.component.scss */
.card {
  padding: 20px;
  border-radius: 12px;
  background: white;
  color: #263238;
}
```

## ベストプラクティス
- Web Componentsとして外部アプリへ提供する場合にShadowDomを選択すると互換性が高い
- 必要なフォントやリセットCSSはShadow DOM内へインポートする（`@import`や`<link rel="stylesheet">`）
- CSS変数を利用すると、外側からテーマを注入できる

## 注意点
- 外部グローバルCSSが効かないため、レイアウトやフォント設定を内側でも完結させる必要がある
- SSRではShadow DOMがサポートされないため、Hydrationでの挙動を確認する
- Angular Materialなどのライブラリとは互換性に注意（一部スタイルが届かなくなる）

## 関連技術
- Web Components / Custom Elements
- CSS変数を用いたテーマ注入
- Angular Elements（`@angular/elements`）
