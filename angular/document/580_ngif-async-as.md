# #580 「*ngIf=\"data$ | async as data\"」

## 概要
`*ngIf="data$ | async as data"`はAsyncPipeの結果を変数`data`に格納し、nullでない場合にテンプレートを表示する一般的なパターン。

## 学習目標
- AsyncPipeと*ngIfの連携パターンを具体的に理解する
- `as`変数のスコープと利用方法を学ぶ
- nullチェックと表示の同時実行を把握する

## 技術ポイント
- `*ngIf`で非null時のみ表示、`else`でフォールバック提供
- `data`変数はテンプレート内で何度でも使用可能
- AsyncPipeの重複評価を回避

## 📺 画面表示用コード（動画用）
```html
<ng-container *ngIf="user$ | async as user; else loading">
  <h2>{{ user.name }}</h2>
  <p>{{ user.email }}</p>
</ng-container>
<ng-template #loading>読み込み中...</ng-template>
```

## 💻 詳細実装例（学習用）
```html
<article *ngIf="product$ | async as product; else skeleton">
  <h1>{{ product.title }}</h1>
  <p>{{ product.description }}</p>
</article>
<ng-template #skeleton>
  <p>読み込み中...</p>
</ng-template>
```

## ベストプラクティス
- `as`構文で再利用し、AsyncPipeの重複使用を避ける
- elseテンプレートでローディングやエラーを表現
- 変数名は意味が分かるものを使用し、ネストを避ける

## 注意点
- `as`変数は`*ngIf`のスコープ内のみ有効
- Observableがnullを返すとテンプレートが表示されないため代替表示を用意
- 後段でPipeチェーンを使う場合はnullガードに注意

## 関連技術
- AsyncPipe
- *ngIf/else
- テンプレート変数
