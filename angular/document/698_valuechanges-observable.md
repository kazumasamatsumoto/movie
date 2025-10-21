# #698 「valueChanges Observable」

## 概要
valueChangesはフォーム値の変化を通知するObservableで、FormControlだけでなくFormGroupやFormArrayにも用意されている。複数フォームの統合にはRxJSオペレーターを使う。

## 学習目標
- valueChangesのObservable特性を理解する
- フォーム全体の監視方法を学ぶ
- 複数ストリームの統合手法を把握する

## 技術ポイント
- valueChangesはHot Observableとして最新値を出力
- FormGroupではオブジェクト全体が通知される
- combineLatestやwithLatestFromで複数フォームを連携

## 📺 画面表示用コード（動画用）
```typescript
combineLatest([
  this.profileForm.valueChanges,
  this.settingForm.valueChanges
]).subscribe(([profile, setting]) => {
  console.log(profile, setting);
});
```

## 💻 詳細実装例（学習用）
```typescript
protected emailCtrl = new FormControl('');
protected notify$ = this.emailCtrl.valueChanges.pipe(
  filter((email): email is string => !!email),
  distinctUntilChanged(),
  tap(email => console.log('notify', email))
);
```

## ベストプラクティス
- valueChangesはpipeでオペレーターを組み合わせて使う
- 複数フォームはcombineLatestで同期する
- Observableはコンポーネント外に公開してテストしやすくする

## 注意点
- 初期値でnullが流れる場合はフィルタリングする
- 購読解除しないと副作用が積み上がる
- combineLatestは全ストリームが値を出すまでemitしない

## 関連技術
- valueChanges
- RxJS
- combineLatest
