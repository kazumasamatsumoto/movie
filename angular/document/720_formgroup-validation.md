# #720 「FormGroup レベルの検証」

## 概要
FormGroupレベルでvalidatorsを設定すると複数コントロールを対象に整合性チェックができ、エラーはフォーム全体のerrorsに格納される。

## 学習目標
- FormGroupレベルバリデーションの設定方法を理解する
- setErrorsの扱い方を学ぶ
- エラー表示の設計を把握する

## 技術ポイント
- FormGroupコンストラクタ第二引数のvalidatorsで設定
- setErrors(null)でエラーを解除
- errors?.キーをテンプレートで確認

## 📺 画面表示用コード（動画用）
```typescript
protected addressGroup = new FormGroup({
  zip: new FormControl('', Validators.pattern(/^[0-9]{3}-[0-9]{4}$/)),
  prefecture: new FormControl('')
}, { validators: [requirePrefectureIfZipFilled] });
```

## 💻 詳細実装例（学習用）
```typescript
function requirePrefectureIfZipFilled(group: AbstractControl): ValidationErrors | null {
  const zip = group.get('zip')?.value as string | null;
  const prefecture = group.get('prefecture')?.value as string | null;
  if (zip && !prefecture) {
    return { prefectureRequired: true };
  }
  return null;
}
```

## ベストプラクティス
- FormGroupバリデーターは小さな関数に分解する
- エラーキーはUIで使いやすい名前にする
- バリデーション状態をログ出力して調整する

## 注意点
- setErrorsを上書きすると既存エラーが消える点に注意
- ネストしたグループではgetパスが複雑になる
- 有効・無効の状態変化に合わせてエラー解除する

## 関連技術
- FormGroup
- setErrors
- クロスフィールド検証
