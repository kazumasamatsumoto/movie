# #733 「非同期バリデーターのデバウンス」

## 概要
非同期バリデーターではdebounceTimeやdistinctUntilChangedでリクエスト頻度を抑え、switchMapで最新入力のみを検証する設計が推奨される。

## 学習目標
- 非同期バリデーターのデバウンス方法を理解する
- switchMapによるキャンセルパターンを学ぶ
- UX向上のためのローディング表示を把握する

## 技術ポイント
- debounceTimeで入力が落ち着くまで待つ
- distinctUntilChangedで同じ値のリクエストを抑制
- switchMapで前回のリクエストをキャンセル

## 📺 画面表示用コード（動画用）
```typescript
const throttledValidator: AsyncValidatorFn = control => {
  return of(control.value).pipe(
    debounceTime(300),
    distinctUntilChanged(),
    switchMap(value => api.validate(value)),
    map(result => (result.valid ? null : { invalid: true }))
  );
};
```

## 💻 詳細実装例（学習用）
```typescript
protected codeCtrl = new FormControl('', {
  asyncValidators: [throttledValidator]
});
```

## ベストプラクティス
- 非同期バリデーターには必ずdebounceTimeを検討する
- switchMapを使って古いリクエストの結果を破棄する
- PENDING状態をUIに表示しユーザーに待機を伝える

## 注意点
- 短すぎるdebounceTimeはレスポンスが遅く感じる
- distinctUntilChangedではオブジェクト比較に注意
- サービス側でもレート制限やキャッシュを検討する

## 関連技術
- debounceTime
- switchMap
- AsyncValidatorFn
