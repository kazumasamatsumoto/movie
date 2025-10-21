# #719 「クロスフィールドバリデーション」

## 概要
クロスフィールドバリデーションはFormGroupレベルで複数コントロールを参照し、親グループにValidationErrorsを設定して整合性を確認する。

## 学習目標
- クロスフィールドバリデーターの実装方法を理解する
- 親グループから子コントロールを取得する方法を学ぶ
- エラー表示の設計を把握する

## 技術ポイント
- FormGroupを受け取るValidatorFnを定義
- group.get('controlName')で値を参照
- エラーはgroup.setErrorsで親グループに設定

## 📺 画面表示用コード（動画用）
```html
<div [formGroup]="passwordGroup">
  <input formControlName="password" type="password" />
  <input formControlName="confirm" type="password" />
  <span *ngIf="passwordGroup.errors?.mismatch">パスワードが一致しません</span>
</div>
```

## 💻 詳細実装例（学習用）
```typescript
function match(password: string, confirm: string): ValidatorFn {
  return control => {
    const group = control as FormGroup;
    const pass = group.get(password)?.value;
    const conf = group.get(confirm)?.value;
    return pass && conf && pass !== conf ? { mismatch: true } : null;
  };
}

protected passwordGroup = new FormGroup({
  password: new FormControl('', { nonNullable: true }),
  confirm: new FormControl('', { nonNullable: true })
}, { validators: [match('password', 'confirm')] });
```

## ベストプラクティス
- groupレベルのエラーキーはUI用に説明的に命名する
- テンプレートでエラー表示をまとめて行う
- 値変更時にmarkAsTouchedを使ってエラーを表示する

## 注意点
- control.parentがnullのケースを考慮する
- 非同期バリデーションと組み合わせると複雑になる
- 深入りしたネストではメンテナンスが難しくなる

## 関連技術
- FormGroup
- クロスフィールド
- ValidationErrors
