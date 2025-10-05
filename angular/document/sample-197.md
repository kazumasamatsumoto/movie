# #197 「select クラス名での選択」

## 概要
Angular v20のselect属性でCSSクラス名を使用してコンテンツ投影を制御する方法を学習します。

## 学習目標
- クラス名セレクターの使用方法を理解する
- CSSクラスによる投影制御を習得する
- スタイルベースのコンテンツ投影を実現できるようになる

## 技術ポイント
- クラス名セレクター
- CSSクラス投影
- スタイルベース制御

## 📺 画面表示用コード

```html
<!-- 親コンポーネント -->
<app-panel>
  <div class="header">パネルヘッダー</div>
  <div class="content">パネルコンテンツ</div>
  <div class="footer">パネルフッター</div>
</app-panel>
```

```html
<!-- 子コンポーネント（app-panel） -->
<div class="panel">
  <div class="panel-header">
    <ng-content select=".header"></ng-content>
  </div>
  <div class="panel-body">
    <ng-content select=".content"></ng-content>
  </div>
  <div class="panel-footer">
    <ng-content select=".footer"></ng-content>
  </div>
</div>
```

```html
<!-- 使用例 -->
<app-modal>
  <div class="modal-header">
    <h2>確認</h2>
  </div>
  <div class="modal-body">
    <p>この操作を実行しますか？</p>
  </div>
  <div class="modal-footer">
    <button>はい</button>
  </div>
</app-modal>
```

## 実践的な活用例

```html
<!-- ダッシュボードコンポーネント -->
<app-dashboard>
  <div class="widget sales">売上データ</div>
  <div class="widget users">ユーザー数</div>
  <div class="widget charts">グラフ</div>
</app-dashboard>
```

## ベストプラクティス
- クラス名は意味のあるものにする
- クラスの命名規則を統一する
- 投影されるクラス構造をドキュメント化する

## 注意点
- クラス名の衝突を避ける
- 複数のクラスが指定された場合の動作
- CSS特異性の考慮

## 関連技術
- CSS Classes
- BEM Methodology
- Component Styling
