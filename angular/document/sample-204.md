# #204 「ng-template での投影」

## 概要
Angular v20のng-templateを使用してテンプレート構造をコンテンツ投影する方法を学習します。

## 学習目標
- ng-templateでのコンテンツ投影方法を理解する
- テンプレート構造の投影を習得する
- 高度なテンプレート投影パターンを実現できるようになる

## 技術ポイント
- ng-template投影
- テンプレート構造投影
- 高度な投影パターン

## 📺 画面表示用コード

```html
<!-- 親コンポーネント -->
<app-template-container>
  <ng-template #customTemplate>
    <h3>カスタムテンプレート</h3>
    <p>テンプレートの内容</p>
    <button>アクション</button>
  </ng-template>
</app-template-container>
```

```html
<!-- 子コンポーネント（app-template-container） -->
<div class="template-container">
  <div class="template-content">
    <ng-content select="ng-template"></ng-content>
  </div>
</div>
```

```html
<!-- 使用例 -->
<app-modal>
  <ng-template #modalContent>
    <div class="modal-header">
      <h2>確認</h2>
    </div>
    <div class="modal-body">
      <p>この操作を実行しますか？</p>
    </div>
    <div class="modal-footer">
      <button>はい</button>
      <button>いいえ</button>
    </div>
  </ng-template>
</app-modal>
```

## 実践的な活用例

```html
<!-- 動的フォームテンプレート -->
<app-form-builder>
  <ng-template #fieldTemplate>
    <div class="form-field">
      <label>フィールドラベル</label>
      <input type="text">
      <span class="error">エラーメッセージ</span>
    </div>
  </ng-template>
</app-form-builder>
```

## ベストプラクティス
- テンプレートは再利用可能な構造にする
- テンプレート内でのデータバインディングを適切に処理する
- テンプレートの責任範囲を明確にする

## 注意点
- テンプレートの実行コンテキスト
- データバインディングのスコープ
- テンプレートの再利用性

## 関連技術
- Template References
- Template Syntax
- Dynamic Templates
