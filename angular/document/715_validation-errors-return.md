# #715 「ValidationErrors の返却」

## 概要
ValidationErrorsはエラー名をキーとした辞書で、複数エラーがある場合は同じオブジェクトに複数キーを追加し、エラーが無ければnullを返す。

## 学習目標
- ValidationErrorsの構造を理解する
- エラー情報の設計方法を学ぶ
- 空オブジェクトを返さない注意点を把握する

## 技術ポイント
- ValidationErrorsは{ [key: string]: any }形式
- multiple errorsは同一オブジェクトに複数キーを設定
- nullを返した場合のみバリデーション成功

## 📺 画面表示用コード（動画用）
```typescript
const passwordValidator: ValidatorFn = control => {
  const value = control.value as string | null;
  if (!value) {
    return null;
  }
  const errors: ValidationErrors = {};
  if (value.length < 8) {
    errors.minLength = { requiredLength: 8, actualLength: value.length };
  }
  if (!/[0-9]/.test(value)) {
    errors.missingNumber = true;
  }
  return Object.keys(errors).length ? errors : null;
};
```

## 💻 詳細実装例（学習用）
```typescript
protected passwordCtrl = new FormControl('', [passwordValidator]);
```

## ベストプラクティス
- エラー情報はUIで必要なデータだけを含める
- 複数エラーを返す場合は優先順位を決める
- ValidationErrorsの型定義を共有して整合性を保つ

## 注意点
- 空オブジェクトを返すとエラー扱いになる
- エラー情報に個人情報を入れない
- キー名の重複で上書きしないよう注意

## 関連技術
- ValidationErrors
- カスタムバリデーション
- エラーメッセージ
