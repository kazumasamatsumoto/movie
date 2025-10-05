# #203 「ng-container との組み合わせ」

## 概要
Angular v20のng-containerとng-contentを組み合わせて、構造化されたコンテンツ投影を実現する方法を学習します。

## 学習目標
- ng-containerとng-contentの組み合わせ方法を理解する
- 構造化されたコンテンツ投影を習得する
- グループ化されたコンテンツ投影を実現できるようになる

## 技術ポイント
- ng-container
- 構造化投影
- グループ化投影

## 📺 画面表示用コード

```html
<!-- 親コンポーネント -->
<app-grouped-content>
  <ng-container class="header-group">
    <h1>タイトル</h1>
    <p>サブタイトル</p>
  </ng-container>
  <ng-container class="content-group">
    <p>メインコンテンツ</p>
    <ul>
      <li>項目1</li>
      <li>項目2</li>
    </ul>
  </ng-container>
</app-grouped-content>
```

```html
<!-- 子コンポーネント（app-grouped-content） -->
<div class="content-wrapper">
  <header class="content-header">
    <ng-content select=".header-group"></ng-content>
  </header>
  <main class="content-main">
    <ng-content select=".content-group"></ng-content>
  </main>
</div>
```

```html
<!-- 使用例 -->
<app-article-layout>
  <ng-container class="meta-info">
    <time>2024-01-01</time>
    <span class="author">著者名</span>
  </ng-container>
  <ng-container class="article-content">
    <h2>記事タイトル</h2>
    <p>記事本文</p>
  </ng-container>
</app-article-layout>
```

## 実践的な活用例

```html
<!-- 複雑なレイアウト -->
<app-dashboard-layout>
  <ng-container class="sidebar-content">
    <nav>ナビゲーション</nav>
    <div class="user-info">ユーザー情報</div>
  </ng-container>
  <ng-container class="main-content">
    <div class="stats">統計情報</div>
    <div class="charts">グラフ</div>
  </ng-container>
</app-dashboard-layout>
```

## ベストプラクティス
- ng-containerは論理的なグループ化に使用する
- グループの責任範囲を明確にする
- 適切なCSSクラスを設定する

## 注意点
- ng-containerはDOM要素を生成しない
- スタイリングの適用方法
- グループ化の複雑さ

## 関連技術
- Template Elements
- Structural Directives
- Component Composition
