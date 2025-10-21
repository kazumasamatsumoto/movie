# #739 「バリデーションのベストプラクティス」

## 概要
Angular v20で堅牢なバリデーションを構築するための基本原則を整理する。

## 学習目標
- 同期・非同期バリデーションの責務分離を理解する
- UIと検証ロジックを疎結合に保つ設計を学ぶ
- SignalとObservableを組み合わせたフィードバックの最適化を把握する

## 技術ポイント
- Validatorsは純粋関数として実装し、副作用を持たせない
- エラーはキーで整理しテンプレートで辞書化して表示する
- FormGroupレベルでのクロスフィールド検証を活用する

## 📺 画面表示用コード（動画用）
```typescript
const errorMessages: Record<string, string> = {
  required: '必須項目です',
  email: 'メールアドレスの形式が正しくありません',
  usernameTaken: '既に使用されています'
};
```

```typescript
const profileForm = new FormGroup({
  email: new FormControl('', [Validators.required, Validators.email]),
  password: new FormControl('', [Validators.required]),
  confirm: new FormControl('', [Validators.required])
}, { validators: [passwordMatchValidator] });
```

## 💻 詳細実装例（学習用）
```typescript
@Component({
  selector: 'app-profile-form',
  templateUrl: './profile-form.component.html',
  standalone: true,
  imports: [ReactiveFormsModule, AsyncPipe, NgFor]
})
export class ProfileFormComponent {
  protected readonly form = new FormGroup({
    email: new FormControl('', [Validators.required, Validators.email]),
    password: new FormControl('', [Validators.required, Validators.minLength(8)]),
    confirm: new FormControl('', [Validators.required])
  }, { validators: [passwordMatchValidator] });

  private readonly errorMessages: Record<string, string> = {
    required: '必須項目です',
    minlength: '8文字以上入力してください',
    email: 'メールアドレスの形式が正しくありません',
    passwordMismatch: '確認用パスワードが一致しません'
  };

  protected readonly emailErrors = computed(() => {
    const control = this.form.get('email');
    if (!control || !control.touched || !control.errors) return [];
    return Object.keys(control.errors).map(key => this.errorMessages[key]);
  });
}
```

## ベストプラクティス
- バリデーターは薄い関数としてテストしやすい構造を保つ
- エラーメッセージは辞書化して多言語対応や再利用を容易にする
- FormGroupレベルでのクロスフィールド検証を活用し、責務をコンポーネントに分散させない

## 注意点
- テンプレートにビジネスロジックを書くとテストが困難になる
- setErrorsの直接操作はstatusChangesの流れを乱すため慎重に扱う
- バリデーターの中でHTTPなどの副作用を起こさない

## 関連技術
- Validators
- FormGroup
- computed
