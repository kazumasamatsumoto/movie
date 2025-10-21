# #732 「メールアドレス存在チェック」

## 概要
メールアドレス存在チェックは入力値を正規化した上でAPIに問い合わせ、既存の場合はemailExistsエラーを返して登録を防ぐ。

## 学習目標
- メールアドレス重複チェックの実装を理解する
- 正規化やキャッシュ戦略を学ぶ
- ユーザーフィードバックの設計を把握する

## 技術ポイント
- trim・toLowerCaseで正規化してからAPIへ送信
- レスポンスをキャッシュして同じ入力の再リクエストを防ぐ
- 結果に応じて成功メッセージも用意する

## 📺 画面表示用コード（動画用）
```typescript
const emailExistsValidator: AsyncValidatorFn = control => {
  const normalized = (control.value as string | null)?.trim().toLowerCase() ?? '';
  if (!normalized) {
    return of(null);
  }
  return api.checkEmail(normalized).pipe(
    map(exists => (exists ? { emailExists: true } : null)),
    catchError(() => of(null))
  );
};
```

## 💻 詳細実装例（学習用）
```typescript
protected emailCtrl = new FormControl('', {
  asyncValidators: [emailExistsValidator]
});
```

## ベストプラクティス
- 正規化した値をキャッシュしてリクエストを削減する
- 存在しない場合にもフィードバックを与える
- エラーメッセージはセキュリティを考慮して詳細を出し過ぎない

## 注意点
- メールアドレスの比較ルールがシステムによって異なる
- APIエラー時にユーザーへ案内を出す
- キャッシュを持つ場合は期限を決める

## 関連技術
- AsyncValidatorFn
- メール検証
- キャッシュ
