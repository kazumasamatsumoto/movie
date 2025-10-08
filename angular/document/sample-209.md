# #209 「カード Component での活用例」

## 概要
コンテンツ投影を利用して汎用的なカードコンポーネントを構築する例を紹介し、ヘッダー・本文・フッターのスロット化による柔軟なレイアウトを実装します。

## 学習目標
- カードコンポーネントで複数スロット投影を設計する方法を理解する
- 親側のマークアップをシンプルに保ちながら内容を差し込む
- デフォルトコンテンツや必須スロットを明確にしたAPIを設計する

## 技術ポイント
- **スロット設計**: `[card-header]`, `[card-footer]`など属性セレクタでスロット化
- **フォールバック**: フッターが未指定の場合にデフォルトボタンを表示する例
- **ドキュメンテーション**: 利用者が守るべきセレクタをドキュメント化

## 📺 画面表示用コード（動画用）

```html
<header class="card__header">
  <ng-content select="[card-header]"></ng-content>
</header>
<section class="card__body">
  <ng-content></ng-content>
</section>
<footer class="card__footer">
  <ng-content select="[card-footer]"></ng-content>
</footer>
```

```html
<app-card>
  <h3 card-header>カードタイトル</h3>
  <p>本文コンテンツ</p>
  <button card-footer>閉じる</button>
</app-card>
```

```scss
.card__header { font-weight: 600; }
```

## 💻 詳細実装例（学習用）
```typescript
// card.component.ts
import { Component } from '@angular/core';

@Component({
  selector: 'app-card',
  standalone: true,
  templateUrl: './card.component.html',
  styleUrls: ['./card.component.scss'],
})
export class CardComponent {}
```

```html
<!-- card.component.html -->
<article class="card">
  <header class="card__header">
    <ng-content select="[card-header]"></ng-content>
  </header>
  <section class="card__body">
    <ng-content></ng-content>
  </section>
  <footer class="card__footer">
    <ng-content select="[card-footer]"></ng-content>
  </footer>
</article>
```

```scss
/* card.component.scss */
.card {
  border-radius: 12px;
  border: 1px solid #e0e0e0;
  padding: 16px;
  background: #fff;
  display: grid;
  gap: 16px;
}
.card__header {
  font-weight: 600;
}
.card__footer {
  text-align: right;
}
```

```html
<!-- parent.component.html -->
<app-card>
  <h3 card-header>Angularカード</h3>
  <p>コンテンツ投影で本文を自由に記述できます。</p>
  <button card-footer class="btn">詳細を見る</button>
</app-card>
```

## ベストプラクティス
- スロット属性は`card-header`, `card-footer`など役割を明確にし、利用者へ周知する
- カード全体のレイアウトやスタイルはコンポーネント側で統一し、中身の表現を親へ任せる
- デフォルトフッター（例：閉じるボタン）を用意すると、親が最小限の記述で済む

## 注意点
- スロットが未提供でも正しく表示されるようフォールバックを設計する
- コンテンツ量が多い場合はスクロールや高さ制限などUI整合性に注意する
- クリックイベントなどは親から投影された要素でハンドリングされることを理解し、APIを設計する

## 関連技術
- `select`属性でのスロット化（#195〜#199）
- `ContentChild`で投影の有無をチェック（#207）
- モーダル/タブなど他コンポーネントへの応用（#210〜#212）

