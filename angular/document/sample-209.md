# #209 「カード Component での活用例」

## 概要
Angular v20のコンテンツ投影を活用したカードコンポーネントの実装例を学習します。

## 学習目標
- カードコンポーネントでのコンテンツ投影パターンを理解する
- 再利用可能なカード設計を習得する
- 実践的なコンテンツ投影アプリケーションを実現できるようになる

## 技術ポイント
- カードコンポーネント設計
- 構造化投影
- 再利用可能設計

## 📺 画面表示用コード

```html
<!-- 親コンポーネント -->
<app-card>
  <div class="card-header">
    <h3>カードタイトル</h3>
    <span class="badge">新着</span>
  </div>
  <div class="card-body">
    <p>カードの内容です</p>
    <ul>
      <li>項目1</li>
      <li>項目2</li>
    </ul>
  </div>
  <div class="card-footer">
    <button>詳細</button>
    <button>削除</button>
  </div>
</app-card>
```

```html
<!-- 子コンポーネント（app-card） -->
<div class="card">
  <div class="card-header">
    <ng-content select=".card-header"></ng-content>
  </div>
  <div class="card-body">
    <ng-content select=".card-body"></ng-content>
  </div>
  <div class="card-footer">
    <ng-content select=".card-footer"></ng-content>
  </div>
</div>
```

```html
<!-- 使用例 -->
<app-card>
  <div class="card-header">
    <h3>商品情報</h3>
  </div>
  <div class="card-body">
    <p>商品の詳細説明</p>
    <div class="price">¥1,000</div>
  </div>
  <div class="card-footer">
    <button>カートに追加</button>
  </div>
</app-card>
```

## 実践的な活用例

```html
<!-- ユーザーカード -->
<app-card>
  <div class="card-header">
    <img src="avatar.jpg" alt="アバター">
    <h3>ユーザー名</h3>
  </div>
  <div class="card-body">
    <p>ユーザーの詳細情報</p>
    <div class="stats">
      <span>投稿数: 100</span>
      <span>フォロワー: 500</span>
    </div>
  </div>
  <div class="card-footer">
    <button>フォロー</button>
    <button>メッセージ</button>
  </div>
</app-card>
```

## ベストプラクティス
- カードの構造を明確に定義する
- 適切なCSSクラスを提供する
- アクセシビリティを考慮した設計を行う

## 注意点
- カード構造の一貫性
- レスポンシブデザインの考慮
- パフォーマンスの最適化

## 関連技術
- Component Design
- CSS Grid/Flexbox
- Accessibility
