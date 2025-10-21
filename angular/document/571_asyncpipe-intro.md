# #571 「AsyncPipe - 非同期パイプ」

## 概要
AsyncPipeはObservableやPromiseをテンプレートで購読し、最新値を自動表示しつつ購読解除も行う。非同期データの表示を安全かつ簡潔に実装できる。

## 学習目標
- AsyncPipeの仕組みと用途を理解する
- Observable/Pemiseをテンプレートで扱う手順を学ぶ
- 自動購読解除によるメモリリーク防止を把握する

## 技術ポイント
- `{{ observable$ | async }}`
- Observableの値を購読し、コンポーネント破棄時に自動unsubscribe
- Promiseもサポートし、resolve値を表示

## 📺 画面表示用コード（動画用）
```html
<p>{{ userName$ | async }}</p>
```

## 💻 詳細実装例（学習用）
```html
<h2>ユーザー名: {{ user$ | async | titlecase }}</h2>
<p>残高: {{ balance$ | async | currency:'JPY':'symbol-narrow' }}</p>
```

```typescript
protected readonly user$ = this.userService.currentUser$;
protected readonly balance$ = this.accountService.balance$;
```

## ベストプラクティス
- コンポーネントでsubscribeせずAsyncPipeを使用し、解除の手間を減らす
- `*ngIf="observable$ | async as value"`で複数回Pipeを書くのを避ける
- Observableは`shareReplay`などでマルチキャスト化し、複数AsyncPipeでも効率化

## 注意点
- 同じObservableに複数AsyncPipeを書くと購読が増えるため`as`構文や`share`を活用
- `async` Pipeがnullを返す場合の表示を考慮し、`*ngIf`でガード
- コンポーネント破棄で自動解除されるが、サービス側のホットObservableは停止しない点に注意

## 関連技術
- Observable / Promise
- share/shareReplay
- *ngIf + AsyncPipe組み合わせ
