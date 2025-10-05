# #213 「レイアウト Component での活用例」

## 概要
Angular v20のコンテンツ投影を活用したレイアウトコンポーネントの実装例を学習します。

## 学習目標
- レイアウトコンポーネントでのコンテンツ投影パターンを理解する
- 構造化されたレイアウト設計を習得する
- 実践的なレイアウトアプリケーションを実現できるようになる

## 技術ポイント
- レイアウトコンポーネント設計
- 構造化投影
- レスポンシブレイアウト

## 📺 画面表示用コード

```html
<!-- 親コンポーネント -->
<app-layout>
  <div class="layout-header">
    <nav class="main-nav">
      <a href="/">ホーム</a>
      <a href="/about">について</a>
      <a href="/contact">お問い合わせ</a>
    </nav>
  </div>
  <div class="layout-sidebar">
    <div class="sidebar-menu">
      <ul>
        <li>メニュー1</li>
        <li>メニュー2</li>
        <li>メニュー3</li>
      </ul>
    </div>
  </div>
  <div class="layout-main">
    <h1>メインコンテンツ</h1>
    <p>ページの主要なコンテンツがここに表示されます</p>
  </div>
  <div class="layout-footer">
    <p>&copy; 2024 会社名. All rights reserved.</p>
  </div>
</app-layout>
```

```html
<!-- 子コンポーネント（app-layout） -->
<div class="layout-container">
  <header class="layout-header">
    <ng-content select=".layout-header"></ng-content>
  </header>
  <div class="layout-body">
    <aside class="layout-sidebar">
      <ng-content select=".layout-sidebar"></ng-content>
    </aside>
    <main class="layout-main">
      <ng-content select=".layout-main"></ng-content>
    </main>
  </div>
  <footer class="layout-footer">
    <ng-content select=".layout-footer"></ng-content>
  </footer>
</div>
```

```html
<!-- 使用例 -->
<app-layout>
  <div class="layout-header">
    <h1>アプリケーションタイトル</h1>
  </div>
  <div class="layout-main">
    <div class="content-area">
      <h2>コンテンツタイトル</h2>
      <p>メインコンテンツ</p>
    </div>
  </div>
</app-layout>
```

## 実践的な活用例

```html
<!-- ダッシュボードレイアウト -->
<app-layout>
  <div class="layout-header">
    <div class="user-info">
      <span>ユーザー名</span>
      <button>ログアウト</button>
    </div>
  </div>
  <div class="layout-sidebar">
    <div class="dashboard-menu">
      <a href="/dashboard">ダッシュボード</a>
      <a href="/analytics">分析</a>
      <a href="/settings">設定</a>
    </div>
  </div>
  <div class="layout-main">
    <div class="dashboard-content">
      <div class="stats-cards">...</div>
      <div class="charts-section">...</div>
    </div>
  </div>
</app-layout>
```

## ベストプラクティス
- レイアウトの構造を明確に定義する
- レスポンシブデザインを考慮する
- 適切なセマンティックHTMLを使用する

## 注意点
- レイアウトの柔軟性
- コンテンツの流れ
- パフォーマンスの最適化

## 関連技術
- CSS Grid/Flexbox
- Responsive Design
- Semantic HTML
