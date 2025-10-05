# #194 「Multi Slot Projection - 複数スロット」

## 概要
Angular v20で複数のスロットにコンテンツを分けて投影する方法を学習します。

## 学習目標
- 複数スロット投影の実装方法を理解する
- select属性の使用方法を習得する
- 構造化されたコンポーネント設計を実現できるようになる

## 技術ポイント
- 複数スロット投影
- select属性
- 構造化コンポーネント設計

## 📺 画面表示用コード

```html
<!-- 親コンポーネント -->
<app-card>
  <div class="header">カードタイトル</div>
  <div class="body">カードの内容</div>
  <div class="footer">アクション</div>
</app-card>
```

```html
<!-- 子コンポーネント（app-card） -->
<div class="card">
  <ng-content select=".header"></ng-content>
  <ng-content select=".body"></ng-content>
  <ng-content select=".footer"></ng-content>
</div>
```

```html
<!-- 使用例 -->
<app-dialog>
  <div class="header">
    <h2>設定</h2>
  </div>
  <div class="body">
    <form>...</form>
  </div>
  <div class="footer">
    <button>保存</button>
  </div>
</app-dialog>
```

## 実践的な活用例

```html
<!-- アコーディオンコンポーネント -->
<app-accordion>
  <div class="header">セクション1</div>
  <div class="content">コンテンツ1</div>
</app-accordion>
```

## ベストプラクティス
- セレクター名を意味のあるものにする
- 投影される構造を明確にドキュメント化する
- デフォルトの投影順序を考慮する

## 注意点
- セレクターが一致しない場合の動作を考慮する
- 投影順序が重要になる場合がある
- CSSクラス名の衝突に注意する

## 関連技術
- CSS Selectors
- Component Composition
- Template Architecture
