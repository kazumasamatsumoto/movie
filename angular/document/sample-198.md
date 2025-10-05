# #198 「select 属性での選択」

## 概要
Angular v20のselect属性でHTML属性を使用してコンテンツ投影を制御する方法を学習します。

## 学習目標
- 属性セレクターの使用方法を理解する
- データ属性による投影制御を習得する
- 柔軟なコンテンツ投影パターンを実現できるようになる

## 技術ポイント
- 属性セレクター
- データ属性投影
- カスタム属性制御

## 📺 画面表示用コード

```html
<!-- 親コンポーネント -->
<app-form>
  <input data-field="name" placeholder="名前">
  <input data-field="email" placeholder="メール">
  <input data-field="password" type="password">
</app-form>
```

```html
<!-- 子コンポーネント（app-form） -->
<form class="form">
  <div class="field-group">
    <ng-content select="[data-field='name']"></ng-content>
  </div>
  <div class="field-group">
    <ng-content select="[data-field='email']"></ng-content>
  </div>
  <div class="field-group">
    <ng-content select="[data-field='password']"></ng-content>
  </div>
</form>
```

```html
<!-- 使用例 -->
<app-tabs>
  <div data-tab="home">ホーム</div>
  <div data-tab="about">について</div>
  <div data-tab="contact">お問い合わせ</div>
</app-tabs>
```

## 実践的な活用例

```html
<!-- 設定パネル -->
<app-settings>
  <div data-section="general">一般設定</div>
  <div data-section="privacy">プライバシー</div>
  <div data-section="notifications">通知</div>
</app-settings>
```

## ベストプラクティス
- データ属性は意味のある名前を使用する
- 属性値の命名規則を統一する
- 投影される属性構造を明確にする

## 注意点
- 属性値の大文字小文字の区別
- 属性値に特殊文字を含む場合の処理
- 属性の存在チェック

## 関連技術
- Data Attributes
- HTML Attributes
- Selector Matching
