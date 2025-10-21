# #730 「API でのユニーク性チェック」

## 概要
APIを利用したユニーク性チェックはAsyncValidatorFnでサーバーに問い合わせ、結果に応じてuniqueNameなどのエラーを返す。

## 学習目標
- API連携バリデーションの流れを理解する
- UX向上のための工夫を学ぶ
- エラーキーの設計を把握する

## 技術ポイント
- debounceTimeとswitchMapでリクエストを最適化
- tapでPENDING状態をUIに伝える
- エラーキーをuniqueNameなど意味のある名前にする

## 📺 画面表示用コード（動画用）
```typescript
const uniqueNameValidator: AsyncValidatorFn = control => {
  return timer(300).pipe(
    switchMap(() => api.checkName(control.value)),
    map(result => (result.isAvailable ? null : { uniqueName: true })),
    catchError(() => of(null))
  );
};
```

## 💻 詳細実装例（学習用）
```typescript
protected usernameCtrl = new FormControl('', {
  asyncValidators: [uniqueNameValidator]
});
```

## ベストプラクティス
- リクエストをキャンセルできるようswitchMapを使う
- ローディング表示と組み合わせてUXを改善する
- キャッシュ戦略を検討してサーバー負荷を下げる

## 注意点
- ネットワークエラー時にnullを返すと検証成功扱いになる点に注意
- 同時入力で複数リクエストが走らないよう制御する
- APIのレスポンス形式が変わったときにエラーキーも更新する

## 関連技術
- AsyncValidatorFn
- switchMap
- API連携
