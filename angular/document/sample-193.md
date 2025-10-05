# #193 「Single Slot Projection - 単一スロット」

## 概要
Angular v20で最も基本的な単一スロット投影の実装方法と使用方法を学習します。

## 学習目標
- 単一スロット投影の実装方法を理解する
- 基本的なコンテンツ投影パターンを習得する
- シンプルな再利用可能コンポーネントを設計できるようになる

## 技術ポイント
- 単一スロット投影
- 基本的なng-content使用法
- シンプルなコンポーネント設計

## 📺 画面表示用コード

```html
<!-- 親コンポーネント -->
<app-card>
  <h3>プロジェクトタイトル</h3>
  <p>プロジェクトの詳細説明</p>
</app-card>
```

```html
<!-- 子コンポーネント（app-card） -->
<div class="card">
  <div class="card-content">
    <ng-content></ng-content>
  </div>
</div>
```

```html
<!-- 使用例 -->
<app-notification>
  <i class="icon">✅</i>
  保存が完了しました
</app-notification>
```

## 実践的な活用例

```html
<!-- モーダルコンポーネント -->
<app-modal>
  <h2>確認</h2>
  <p>この操作を実行しますか？</p>
  <button>はい</button>
  <button>いいえ</button>
</app-modal>
```

```html
<!-- ツールチップコンポーネント -->
<app-tooltip>
  <span>ホバーして詳細を確認</span>
</app-tooltip>
```

## ベストプラクティス
- 投影されるコンテンツの期待値を明確にする
- 適切なCSSクラスを提供する
- デフォルトのスタイリングを設定する

## 注意点
- 投影されるコンテンツの構造に依存する
- 複雑なレイアウトには不向き
- スタイリングの継承に注意する

## 関連技術
- CSS Styling
- Component Architecture
- Template Syntax
