# #192 「ng-content の仕組み」

## 概要
Angular v20のng-contentディレクティブがどのような仕組みで動作するかを詳しく学習します。

## 学習目標
- ng-contentの内部的な動作メカニズムを理解する
- DOM構造の投影プロセスを理解する
- コンポーネント境界でのコンテンツ共有の仕組みを理解する

## 技術ポイント
- DOM投影メカニズム
- コンポーネント境界
- コンテンツ共有

## 📺 画面表示用コード

```html
<!-- 親コンポーネントのテンプレート -->
<app-container>
  <div class="header">ヘッダー</div>
  <div class="content">コンテンツ</div>
</app-container>
```

```html
<!-- 子コンポーネント（app-container） -->
<div class="wrapper">
  <ng-content></ng-content>
</div>
```

```html
<!-- 実際にレンダリングされる結果 -->
<div class="wrapper">
  <div class="header">ヘッダー</div>
  <div class="content">コンテンツ</div>
</div>
```

## 実践的な活用例

```html
<!-- レイアウトコンポーネント -->
<app-layout>
  <nav>ナビゲーション</nav>
  <main>メインコンテンツ</main>
  <footer>フッター</footer>
</app-layout>
```

## ベストプラクティス
- 投影されるコンテンツの構造をドキュメント化する
- 適切なセマンティックHTMLを使用する
- コンポーネントの責任範囲を明確にする

## 注意点
- 投影はコンパイル時に行われる
- 動的なコンテンツ変更には制限がある
- パフォーマンスへの影響を考慮する

## 関連技術
- Angular Change Detection
- DOM Manipulation
- Component Lifecycle
