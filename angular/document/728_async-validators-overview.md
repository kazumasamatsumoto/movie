# #728 「非同期バリデーター」

## 概要
非同期バリデーターはAsyncValidatorFnを実装してPromiseまたはObservableを返し、非同期処理の完了後にValidationErrors | nullを通知する。

## 学習目標
- AsyncValidatorFnの基本を理解する
- 非同期検証のライフサイクルを把握する
- PENDING状態の活用方法を学ぶ

## 技術ポイント
- AsyncValidatorFnはAbstractControlを受け取る関数
- Observable/PROMISEを返して結果を通知
- PENDING → VALID/INVALIDの流れで状態が更新される

## 📺 画面表示用コード（動画用）
```typescript
const uniqueEmailValidator: AsyncValidatorFn = control => {
  return defer(() => api.checkEmail(control.value))
    .pipe(map(isTaken => (isTaken ? { emailTaken: true } : null)));
};
```

## 💻 詳細実装例（学習用）
```typescript
protected emailCtrl = new FormControl('', {
  asyncValidators: [uniqueEmailValidator]
});
```

## ベストプラクティス
- Observableチェーンでエラーハンドリングを行う
- サーバー負荷を考慮してdebounceTimeを併用する
- PENDING状態をUIに表示して待機を促す

## 注意点
- 複数回のリクエストをキャンセルしないとレースコンディションが起こる
- AsyncValidatorFnは必ず完了するObservable/Promiseを返す
- エラー時にnullを返すと検証が成功扱いになるため注意

## 関連技術
- AsyncValidatorFn
- PENDING状態
- 非同期処理
