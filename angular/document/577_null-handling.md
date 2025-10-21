# #577 「null 値の扱い」

## 概要
AsyncPipeはObservableやPromiseがnull/undefinedを返した場合、テンプレートでは空文字列として扱われる。nullチェックが必要な場合は`*ngIf`と組み合わせる。

## 学習目標
- AsyncPipeがnullをどのように扱うか理解する
- null/Undefined対策として`*ngIf`や`default`値を適用する方法を学ぶ
- 非表示時のレイアウトへの影響を把握する

## 技術ポイント
- `{{ value$ | async }}`がnullの場合、何も表示されない
- `*ngIf="value$ | async as value"`でnullガード
- `??`演算子でデフォルト値を設定する方法も有効

## 📺 画面表示用コード（動画用）
```html
<p>{{ user$ | async ?? '取得中...' }}</p>
```

## 💻 詳細実装例（学習用）
```html
<ng-container *ngIf="user$ | async as user; else loading">
  <p>{{ user.name }}</p>
</ng-container>
<ng-template #loading>読み込み中...</ng-template>
```

## ベストプラクティス
- `*ngIf ... as`構文で一度だけPipeを適用し値を再利用
- null時の表示を明確にするためフォールバックテキストを用意
- UIが崩れないようSkeletonやプレースホルダーを併用

## 注意点
- null/undefinedが頻繁に来る場合はUIがちらつく可能性
- Pipeチェーンでnullが渡ると後段Pipeでエラーになるためガード
- Promiseがresolveされる前はundefinedなのでテンプレートで考慮

## 関連技術
- *ngIf + async
- Nullish coalescing operator
- Skeleton UI
