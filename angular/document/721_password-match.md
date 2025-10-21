# #721 「パスワード一致検証」

## 概要
パスワード一致検証はFormGroupバリデーターを使い、passwordとconfirmの値を比較して一致しない場合にmismatchエラーを返す。

## 学習目標
- パスワード一致バリデーターの実装手順を理解する
- エラー表示のテンプレート設計を学ぶ
- リアルタイムフィードバックの考え方を掴む

## 技術ポイント
- FormGroupのvalidatorでpasswordとconfirmを比較
- mismatchエラーを親グループに設定
- valueChangesでリアルタイムに一致状況を確認

## 📺 画面表示用コード（動画用）
```html
<div [formGroup]="passwordForm">
  <input formControlName="password" type="password" />
  <input formControlName="confirm" type="password" />
  <span *ngIf="passwordForm.errors?.mismatch">パスワードが一致しません</span>
</div>
```

## 💻 詳細実装例（学習用）
```typescript
function matchPassword(group: AbstractControl): ValidationErrors | null {
  const password = group.get('password')?.value as string | null;
  const confirm = group.get('confirm')?.value as string | null;
  return password && confirm && password !== confirm ? { mismatch: true } : null;
}

protected passwordForm = new FormGroup({
  password: new FormControl('', { nonNullable: true }),
  confirm: new FormControl('', { nonNullable: true })
}, { validators: [matchPassword] });
```

## ベストプラクティス
- mismatchエラー時にconfirmフィールドへフォーカスを移す
- パスワード強度チェックと組み合わせる
- 送信前にmarkAllAsTouchedでエラーを確実に出す

## 注意点
- controlがnullの時に備えて安全に値を取得する
- ネストが深い場合はgetのパスを定数化する
- valueChangesのループにならないようsubscribeでsetValueしない

## 関連技術
- FormGroup
- クロスフィールド
- mismatchエラー
