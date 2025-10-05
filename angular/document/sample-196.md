# #196 「select タグ名での選択」

## 概要
Angular v20のselect属性でHTMLタグ名を使用してコンテンツ投影を制御する方法を学習します。

## 学習目標
- タグ名セレクターの使用方法を理解する
- HTML要素による投影制御を習得する
- セマンティックなコンテンツ投影を実現できるようになる

## 技術ポイント
- タグ名セレクター
- HTML要素投影
- セマンティックHTML

## 📺 画面表示用コード

```html
<!-- 親コンポーネント -->
<app-article>
  <h1>記事タイトル</h1>
  <h2>サブタイトル</h2>
  <p>記事の内容</p>
  <img src="image.jpg" alt="画像">
</app-article>
```

```html
<!-- 子コンポーネント（app-article） -->
<article class="article">
  <header>
    <ng-content select="h1"></ng-content>
    <ng-content select="h2"></ng-content>
  </header>
  <div class="content">
    <ng-content select="p"></ng-content>
    <ng-content select="img"></ng-content>
  </div>
</article>
```

```html
<!-- 使用例 -->
<app-card>
  <h3>商品名</h3>
  <p>商品の説明</p>
  <button>購入</button>
</app-card>
```

## 実践的な活用例

```html
<!-- ブログ投稿コンポーネント -->
<app-blog-post>
  <h1>投稿タイトル</h1>
  <time>2024-01-01</time>
  <p>投稿内容</p>
  <ul>
    <li>タグ1</li>
    <li>タグ2</li>
  </ul>
</app-blog-post>
```

## ベストプラクティス
- セマンティックなHTMLタグを使用する
- 投影されるタグの階層を考慮する
- 適切なHTML構造を維持する

## 注意点
- 同じタグが複数ある場合の動作
- ネストしたタグの投影
- セレクターの特異性

## 関連技術
- Semantic HTML
- CSS Selectors
- HTML Structure
