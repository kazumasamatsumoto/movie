# #729 「AsyncValidatorFn 型」

## 概要
AsyncValidatorFnはPromiseまたはObservableでValidationErrors | nullを返す関数型で、非同期バリデーションの基礎となる。

## 学習目標
- AsyncValidatorFnのシグネチャを理解する
- Observableを使った実装を学ぶ
- エラー処理のポイントを把握する

## 技術ポイント
- Observableを返すとRxJSオペレーターが使いやすい
- catchErrorでエラー時にnullを返して検証続行
- Promiseを返す実装も可能だが統一感を意識する

## 📺 画面表示用コード（動画用）
```typescript
const asyncValidator: AsyncValidatorFn = control => {
  return api.check(control.value).pipe(
    map(isValid => (isValid ? null : { duplicated: true })),
    catchError(() => of(null))
  );
};
```

## 💻 詳細実装例（学習用）
```typescript
protected codeCtrl = new FormControl('', {
  asyncValidators: [asyncValidator]
});
```

## ベストプラクティス
- 統一してObservableを返すとテストしやすい
- catchErrorで失敗時にもフォームを破綻させない
- テストではTestSchedulerを使って時間制御する

## 注意点
- 非同期処理が完了しないとフォームがPENDINGのままになる
- 複数購読が残るとメモリリークの原因になる
- Promise実装とObservable実装が混在しないよう整理する

## 関連技術
- AsyncValidatorFn
- Observable
- catchError
