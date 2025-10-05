# #195 「select 属性 - スロット選択」

## 概要
Angular v20のselect属性を使用して、どのコンテンツをどのスロットに投影するかを制御する方法を学習します。

## 学習目標
- select属性の基本的な使用方法を理解する
- CSSセレクターによる投影制御を習得する
- 柔軟なコンテンツ投影パターンを実現できるようになる

## 技術ポイント
- select属性
- CSSセレクター
- 投影制御

## 📺 画面表示用コード

```html
<!-- 親コンポーネント -->
<app-layout>
  <header class="main-header">ヘッダー</header>
  <aside class="sidebar">サイドバー</aside>
  <main class="content">メインコンテンツ</main>
</app-layout>
```

```html
<!-- 子コンポーネント（app-layout） -->
<div class="layout">
  <ng-content select="header.main-header"></ng-content>
  <ng-content select="aside.sidebar"></ng-content>
  <ng-content select="main.content"></ng-content>
</div>
```

```html
<!-- 属性セレクターの例 -->
<app-form>
  <input name="email" placeholder="メール">
  <input name="password" type="password">
</app-form>
```

## 実践的な活用例

```html
<!-- 複雑なレイアウト -->
<app-dashboard>
  <nav class="navigation">ナビ</nav>
  <section class="stats">統計</section>
  <section class="chart">グラフ</section>
  <footer class="footer">フッター</footer>
</app-dashboard>
```

## ベストプラクティス
- セレクターは具体的で意味のあるものにする
- 投影されないコンテンツの動作を考慮する
- セレクターの優先度を理解する

## 注意点
- セレクターが複数マッチする場合の動作
- パフォーマンスへの影響
- セレクターの複雑さと保守性のバランス

## 関連技術
- CSS Selectors
- DOM Querying
- Template Matching
