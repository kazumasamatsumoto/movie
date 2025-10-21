# #578 「AsyncPipe と *ngIf」

## 概要
AsyncPipeは`*ngIf`と組み合わせることで、非同期値のnullチェックと表示を同時に行える。`as`構文で結果を変数に保持すればテンプレート内で再利用可能。

## 学習目標
- AsyncPipeと*ngIfの組み合わせを理解する
- `as`構文を使ってテンプレート内で値を再利用する手法を学ぶ
- 非同期データの安全な表示パターンを把握する

## 技術ポイント
- `<ng-container *ngIf="data$ | async as data">...</ng-container>`
- null/undefinedは*ngIfで判定され表示されない
- 変数を利用して複数箇所でAsyncPipeを繰り返さない

## 📺 画面表示用コード（動画用）
```html
<ng-container *ngIf="user$ | async as user">
  <h2>{{ user.name }}</h2>
  <p>{{ user.email }}</p>
</ng-container>
```

## 💻 詳細実装例（学習用）
```html
<article *ngIf="post$ | async as post">
  <h1>{{ post.title }}</h1>
  <p>{{ post.body }}</p>
</article>
```

## ベストプラクティス
- `as`変数で値を保持し、AsyncPipeの重複呼び出しを防ぐ
- elseテンプレートでローディングやエラー表示を実装
- 複数のObservableを扱う場合はCombineLatestなどの合成を検討

## 注意点
- `as`構文は`*ngIf`に限定されるため`<ng-container>`や`<div>`で使用
- 値がnullを返す場合はテンプレートが描画されないので代替表示を用意
- Observableがcompleteしない場合も表示は継続される

## 関連技術
- AsyncPipe
- *ngIf
- combineLatest, forkJoin
