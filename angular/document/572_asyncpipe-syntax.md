# #572 「{{ observable$ | async }}」

## 概要
`{{ observable$ | async }}`はテンプレートでObservableを購読し、最新値を表示する最も基本的なAsyncPipeの使用例。nullの場合は空文字として表示される。

## 学習目標
- AsyncPipeの基本構文を理解する
- Observableが提供する直近の値を表示する方法を学ぶ
- null/未発行状態での表示挙動を把握する

## 技術ポイント
- Observableをテンプレートで直接購読
- 値が変化すると自動でテンプレートが更新
- null/undefinedは空文字として扱われる

## 📺 画面表示用コード（動画用）
```html
<span>{{ statusMessage$ | async }}</span>
```

## 💻 詳細実装例（学習用）
```html
<p>残り時間: {{ timer$ | async }}</p>
<span>通知: {{ notification$ | async }}</span>
```

## ベストプラクティス
- `async` Pipeを多用する場合は`*ngIf="obs$ | async as value"`で値をキャッシュ
- Inputバインディングでも利用可能（例: `[value]="count$ | async"`）
- Observableの初期値が必要なときは`startWith`で明示する

## 注意点
- 同じObservableを複数箇所で`| async`すると購読が複数回作られる
- null値や未発行状態ではDOMが空なのでレイアウトに注意
- AsyncPipeはPromiseも扱うが、一度解決したPromiseはキャッシュされる

## 関連技術
- AsyncPipe
- Promiseの表示
- share/shareReplayによる購読共有
