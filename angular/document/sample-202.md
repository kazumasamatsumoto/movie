# #202 「動的コンテンツ投影」

## 概要
Angular v20の@forディレクティブとng-contentを組み合わせて、データに基づいて動的にコンテンツを投影する方法を学習します。

## 学習目標
- 動的コンテンツ投影の実装方法を理解する
- @forディレクティブとng-contentの組み合わせを習得する
- データドリブンなコンテンツ投影を実現できるようになる

## 技術ポイント
- 動的投影
- @forディレクティブ
- データドリブン投影

## 📺 画面表示用コード

```html
<!-- 親コンポーネント -->
<app-dynamic-list [items]="userList">
  <div data-user-id="1">ユーザー1</div>
  <div data-user-id="2">ユーザー2</div>
  <div data-user-id="3">ユーザー3</div>
</app-dynamic-list>
```

```html
<!-- 子コンポーネント（app-dynamic-list） -->
<div class="list-container">
  @for (item of items(); track item.id) {
    <div class="list-item">
      <ng-content select="[data-user-id='{{item.id}}']"></ng-content>
    </div>
  }
</div>
```

```html
<!-- 使用例 -->
<app-tab-container [tabs]="tabData">
  <div data-tab="home">ホームコンテンツ</div>
  <div data-tab="about">について</div>
  <div data-tab="contact">お問い合わせ</div>
</app-tab-container>
```

## 実践的な活用例

```html
<!-- 動的フォーム -->
<app-dynamic-form [fields]="formFields">
  <input data-field="name" placeholder="名前">
  <input data-field="email" placeholder="メール">
  <textarea data-field="message" placeholder="メッセージ"></textarea>
</app-dynamic-form>
```

## ベストプラクティス
- trackBy関数を使用してパフォーマンスを最適化する
- データの変更を適切に検知する
- 投影されるコンテンツの一意性を確保する

## 注意点
- 大量のデータでのパフォーマンス
- 動的コンテンツのメモリ管理
- データ変更時の再投影コスト

## 関連技術
- Control Flow (@for)
- Track By Functions
- Data Binding
