# #197 「select クラス名での選択」

## 概要
`select`属性にクラスセレクタを指定して、親コンポーネントから渡される特定クラスの要素だけをスロットへ投影する方法を学びます。

## 学習目標
- クラスセレクタを使ったスロットの分岐方法を理解する
- 複数クラス条件やBEM命名と組み合わせた運用を把握する
- セレクタ設計をAPIとしてドキュメント化する重要性を認識する

## 技術ポイント
- **クラスセレクタ**: `<ng-content select=".card-footer"></ng-content>`
- **複数クラス**: `.card-footer.primary` のように組み合わせることも可能
- **命名規則**: BEMなど統一したクラス命名でユーザーが迷わないAPIを設計

## 📺 画面表示用コード（動画用）

```html
<ng-content select=".panel__header"></ng-content>
<ng-content></ng-content>
```

```html
<app-panel>
  <div class="panel__header">ヘッダー</div>
  <p>本文</p>
</app-panel>
```

```scss
.panel__header { font-weight: 600; }
```

## 💻 詳細実装例（学習用）
```html
<!-- panel.component.html -->
<article class="panel">
  <header class="panel__header">
    <ng-content select=".panel__header"></ng-content>
  </header>
  <section class="panel__body">
    <ng-content></ng-content>
  </section>
</article>
```

```html
<!-- parent.component.html -->
<app-panel>
  <div class="panel__header primary">クラスで投影</div>
  <p>本文に入るコンテンツです。</p>
</app-panel>
```

## ベストプラクティス
- クラス名をAPIとして定義し、利用者が参照できるドキュメントを提供する
- BEM記法やプレフィックス（例：`panel__`）を用いて衝突を避ける
- クラス名をInputで指定できるようにし、柔軟なAPIを提供するパターンも有効

## 注意点
- 親が複数のクラスを持つ要素を渡す場合、意図せず複数スロットにマッチしないようセレクタを厳密に定義する
- クラス名に依存するため、命名が変わるとAPI互換性が失われる
- マッチしない場合はデフォルトスロットへ入るため、フォールバックを用意する

## 関連技術
- select タグ名/属性/ディレクティブ（#196, #198, #199）
- `ContentChild`によるクラス存在の検証
- CSS ModulesやTailwindなど他のスタイル戦略との併用

