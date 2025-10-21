# #731 「ユーザー名重複チェック」

## 概要
ユーザー名重複チェックは非同期バリデーターでAPIを呼び出し、結果が重複ならusernameTakenエラーを返してフォーム送信を防ぐ。

## 学習目標
- ユーザー名重複チェックの実装手順を理解する
- 入力頻度に応じたリクエスト制御方法を学ぶ
- 大文字小文字の扱いなどビジネスルールを把握する

## 技術ポイント
- debounceTimeとdistinctUntilChangedでリクエスト頻度を抑制
- switchMapで最新リクエストのみ有効にする
- エラーキーはusernameTakenなど明示的にする

## 📺 画面表示用コード（動画用）
```typescript
const usernameTakenValidator: AsyncValidatorFn = control => {
  return control.valueChanges.pipe( // placeholder to illustrate idea
    debounceTime(400),
    distinctUntilChanged(),
    switchMap(value => api.checkUsername(value)),
    map(isTaken => (isTaken ? { usernameTaken: true } : null)),
    catchError(() => of(null))
  );
};
```

## 💻 詳細実装例（学習用）
```typescript
protected usernameCtrl = new FormControl('', {
  asyncValidators: [usernameTakenValidator]
});
```

## ベストプラクティス
- サーバーと同じ正規化（trim/小文字化など）を事前に行う
- PENDING状態をUIに表示する
- 成功時は補助テキストで利用可能なことを知らせる

## 注意点
- valueChangesを非同期バリデーター内で直接購読しない設計を検討する
- レイスコンディションを避けるためswitchMapが必須
- テストではモックAPIで遅延やエラーを再現する

## 関連技術
- AsyncValidatorFn
- debounceTime
- distinctUntilChanged
