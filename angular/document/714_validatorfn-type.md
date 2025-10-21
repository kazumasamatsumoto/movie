# #714 「ValidatorFn 型」

## 概要
ValidatorFnは(AbstractControl) => ValidationErrors | nullの関数型で、すべての同期カスタムバリデーターやcomposeの土台となる。

## 学習目標
- ValidatorFnの型定義を理解する
- AbstractControlから値を安全に扱う方法を学ぶ
- composeなどのAPIとの互換性を把握する

## 技術ポイント
- controlはFormControl/FormGroup/FormArrayが渡される
- ValidationErrorsは辞書形式
- 非同期バリデーションはAsyncValidatorFnを使用

## 📺 画面表示用コード（動画用）
```typescript
const mustStartWithA: ValidatorFn = control => {
  const value = control.value as string | null;
  return value?.startsWith('A') ? null : { mustStartWithA: true };
};
```

## 💻 詳細実装例（学習用）
```typescript
type MustStartWithAError = { mustStartWithA: true };

const mustStartWithA: ValidatorFn = control => {
  const value = control.value as string | null;
  if (value?.startsWith('A')) {
    return null;
  }
  const error: MustStartWithAError = { mustStartWithA: true };
  return error;
};
```

## ベストプラクティス
- valueの型を絞るヘルパー関数を用意する
- 戻り値の型を型エイリアスで明確にする
- ValidatorFnは副作用を持たせない

## 注意点
- control.parentを参照する場合はnullチェックが必要
- FormArrayで使う場合はvalueが配列になることを想定する
- エラーキーの衝突を避けるため命名規則を決める

## 関連技術
- ValidatorFn
- ValidationErrors
- 型安全性
