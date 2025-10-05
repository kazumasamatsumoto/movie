# #191 「ng-content - 基本的なコンテンツ投影」

## 概要
Angular v20のng-contentディレクティブを使用して、親コンポーネントから子コンポーネントにコンテンツを投影する基本的な方法を学習します。

## 学習目標
- ng-contentディレクティブの基本的な使用方法を理解する
- コンテンツ投影の概念とメリットを理解する
- 再利用可能なコンポーネント設計の基礎を習得する

## 技術ポイント
- ng-contentディレクティブ
- コンテンツ投影（Content Projection）
- 再利用可能なコンポーネント設計

## 📺 画面表示用コード

```html
<!-- 親コンポーネント -->
<app-card>
  <h2>カードタイトル</h2>
  <p>カードの内容です</p>
</app-card>
```

```html
<!-- 子コンポーネント（app-card） -->
<div class="card">
  <div class="card-body">
    <ng-content></ng-content>
  </div>
</div>
```

## 実践的な活用例

```html
<!-- ボタンコンポーネントでの活用 -->
<app-button>
  <i class="icon">🚀</i>
  実行
</app-button>
```

```html
<!-- アラートコンポーネントでの活用 -->
<app-alert type="warning">
  <strong>注意:</strong>
  この操作は取り消せません
</app-alert>
```

## ベストプラクティス
- 投影されるコンテンツの構造を明確に定義する
- 適切なCSSスタイリングを適用する
- アクセシビリティを考慮した設計を行う

## 注意点
- 投影されたコンテンツは子コンポーネントのスコープで実行される
- 親コンポーネントのデータバインディングは投影後は無効になる
- パフォーマンスを考慮して適切に使用する

## 関連技術
- Angular Components
- Template Reference Variables
- Component Communication
