# #211 「タブ Component での活用例」

## 概要
Angular v20のコンテンツ投影を活用したタブコンポーネントの実装例を学習します。

## 学習目標
- タブコンポーネントでのコンテンツ投影パターンを理解する
- 動的なタブコンテンツ切り替えを習得する
- 実践的なタブアプリケーションを実現できるようになる

## 技術ポイント
- タブコンポーネント設計
- 動的コンテンツ切り替え
- タブ管理

## 📺 画面表示用コード

```html
<!-- 親コンポーネント -->
<app-tabs [activeTab]="currentTab" (tabChange)="onTabChange($event)">
  <div data-tab="home" class="tab-content">
    <h3>ホーム</h3>
    <p>ホームページのコンテンツ</p>
  </div>
  <div data-tab="about" class="tab-content">
    <h3>について</h3>
    <p>会社についての情報</p>
  </div>
  <div data-tab="contact" class="tab-content">
    <h3>お問い合わせ</h3>
    <p>連絡先情報</p>
  </div>
</app-tabs>
```

```html
<!-- 子コンポーネント（app-tabs） -->
<div class="tabs-container">
  <div class="tab-headers">
    @for (tab of tabs(); track tab.id) {
      <button 
        class="tab-header" 
        [class.active]="tab.id === activeTab"
        (click)="selectTab(tab.id)">
        {{tab.label}}
      </button>
    }
  </div>
  <div class="tab-content-area">
    <ng-content select="[data-tab='{{activeTab}}']"></ng-content>
  </div>
</div>
```

```html
<!-- 使用例 -->
<app-tabs [tabs]="userTabs">
  <div data-tab="profile" class="tab-content">
    <h3>プロフィール</h3>
    <form>...</form>
  </div>
  <div data-tab="settings" class="tab-content">
    <h3>設定</h3>
    <div class="settings-form">...</div>
  </div>
</app-tabs>
```

## 実践的な活用例

```html
<!-- ダッシュボードタブ -->
<app-tabs [tabs]="dashboardTabs">
  <div data-tab="overview" class="tab-content">
    <div class="stats-grid">...</div>
  </div>
  <div data-tab="analytics" class="tab-content">
    <div class="charts-container">...</div>
  </div>
  <div data-tab="reports" class="tab-content">
    <div class="reports-list">...</div>
  </div>
</app-tabs>
```

## ベストプラクティス
- タブの構造を明確に定義する
- アクティブタブの状態管理を適切に行う
- アクセシビリティを考慮した設計を行う

## 注意点
- タブ切り替えのパフォーマンス
- 動的コンテンツの初期化
- キーボードナビゲーション

## 関連技術
- Tab Management
- Dynamic Content
- State Management
