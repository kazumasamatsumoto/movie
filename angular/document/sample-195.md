# #195 「select 属性 - スロット選択」

## 概要
`ng-content`の`select`属性を使って、投影されるコンテンツをセレクタで振り分ける方法を学びます。タグ名・クラス・属性・ディレクティブへ柔軟に対応できます。

## 学習目標
- `select`属性の基本構文を理解する
- CSSセレクタでコンテンツを分岐するパターンを把握する
- セレクタ設計によるAPIドキュメンテーションの重要性を認識する

## 技術ポイント
- **基本構文**: `<ng-content select="[header]"></ng-content>`
- **マッチ順序**: 複数スロットがある場合は宣言順に判定され、最初にマッチしたスロットへ挿入
- **フォールバック**: `select`なしの`ng-content`はマッチしなかったコンテンツを受け取る

## 📺 画面表示用コード（動画用）

```html
<ng-content select="[panel-header]"></ng-content>
<ng-content></ng-content>
```

```html
<app-panel>
  <div panel-header>ヘッダー</div>
  <p>本文</p>
</app-panel>
```

```scss
.panel__header { font-weight: bold; }
```

## 💻 詳細実装例（学習用）
```html
<!-- panel.component.html -->
<article class="panel">
  <header class="panel__header">
    <ng-content select="[panel-header]"></ng-content>
  </header>
  <section class="panel__body">
    <ng-content></ng-content>
  </section>
</article>
```

```html
<!-- parent.component.html -->
<app-panel>
  <h3 panel-header>セレクタ例</h3>
  <p>任意のコンテンツが本文に挿入されます。</p>
</app-panel>
```

## ベストプラクティス
- セレクタは意味のある名前を付け、APIとしてドキュメントに明記する
- `select`が多用される場合は、親が理解しやすい命名規則（例：`header`, `footer`）を採用する
- デフォルトスロットを用意し、必須ではないセクションを省略可能にする

## 注意点
- CSSセレクタとして評価されるため、特定の組み合わせ（`.class[attr]`など）も指定可能だが複雑すぎると混乱を招く
- Slotに該当する要素がない場合、空の要素がレンダリングされるのでフォールバックを検討する
- 親がセレクタを間違えるとコンテンツが表示されないため、テストでカバーする

## 関連技術
- select タグ名/クラス/属性/ディレクティブ（#196〜#199）
- Multi Slot Projection（#194）
- `ContentChild`での存在チェック

