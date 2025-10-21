# #573 「Observable の自動購読」

## 概要
AsyncPipeは内部でObservableをsubscribeし、値が流れるたびにテンプレートを更新する。購読解除も自動で行われ、手動管理が不要。

## 学習目標
- AsyncPipeがObservableを自動購読する仕組みを理解する
- 最新値が表示されるまでの流れを把握する
- 手動購読と比較したメリットを学ぶ

## 技術ポイント
- Observableを`| async`でテンプレートに渡すだけでsubscribe
- 値が変わるたびにテンプレートが更新
- コンポーネントdestroy時にunsubscribe

## 📺 画面表示用コード（動画用）
```html
<p>現在値: {{ counter$ | async }}</p>
```

## 💻 詳細実装例（学習用）
```typescript
protected readonly counter$ = this.timerService.counter$;
```

```html
<h3>カウンター: {{ counter$ | async }}</h3>
```

## ベストプラクティス
- Observableはcold/hotに関わらずAsyncPipeに任せると安全
- ハンドル不要のため購読漏れがなくなる
- 値を複数箇所で使う場合は`as`構文で再利用

## 注意点
- AsyncPipeごとに新規購読されるため、共有したい場合は`share`を利用
- Observableがエラーを流すとエラーをthrowするためエラーハンドリングを設計
- long-running Observableはコンポーネント破棄時に自動解除されるが、サービス側でリソースが残らないよう設計

## 関連技術
- AsyncPipe
- subscribe/unsubscribeの手動管理
- RxJS share/shareReplay
