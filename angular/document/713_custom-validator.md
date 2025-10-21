# #713 「カスタムバリデーター作成」

## 概要
カスタムバリデーターはValidatorFnを実装し、条件を満たさないときにValidationErrorsを返す純粋関数として作成する。

## 学習目標
- ValidatorFnの実装手順を理解する
- ValidationErrorsの構造を学ぶ
- 再利用可能な形にまとめる方法を把握する

## 技術ポイント
- ValidatorFnは(AbstractControl) => ValidationErrors | null
- エラーキーに必要な情報を格納する
- 純粋関数として副作用を避ける

## 📺 画面表示用コード（動画用）
```typescript
function forbiddenWord(word: string): ValidatorFn {
  return control => {
    const value = control.value as string | null;
    return value && value.includes(word)
      ? { forbiddenWord: { word } }
      : null;
  };
}
```

## 💻 詳細実装例（学習用）
```typescript
protected commentCtrl = new FormControl('', [forbiddenWord('NG')]);
```

## ベストプラクティス
- 再利用するバリデーターは専用ファイルに切り出す
- 戻り値の型をtype aliasで明確にする
- 境界条件や異常系をユニットテストで確認する

## 注意点
- control.valueの型が不明な場合は型ガードを使う
- DIが必要な場合はクラスベースのバリデーターを検討
- エラー情報に個人情報を含めない

## 関連技術
- ValidatorFn
- ValidationErrors
- 再利用性
