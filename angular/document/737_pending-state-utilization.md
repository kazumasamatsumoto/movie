# #737 「pending 状態の活用」

## 概要
PENDING状態をトリガーにUX改善や処理制御を行うテクニックを紹介する。

## 学習目標
- PENDING状態の発生タイミングを理解する
- statusChangesから状態遷移を監視する方法を学ぶ
- Pending中の操作制限や通知表示の設計方法を把握する

## 技術ポイント
- statusChangesはVALID/INVALID/PENDINGを順次通知する
- PENDING中は送信ボタンをdisableして二重送信を防ぐ
- combineLatestで複数コントロールのPENDING状態を集約する

## 📺 画面表示用コード（動画用）
```typescript
const isPending$ = form.statusChanges.pipe(
  map(status => status === 'PENDING'),
  startWith(form.pending)
);
```

## 💻 詳細実装例（学習用）
```typescript
@Component({
  selector: 'app-pending-sample',
  template: `
    <form [formGroup]="form">
      <input formControlName="email" placeholder="メールアドレス" />
      <button type="submit" [disabled]="isPending()">送信</button>
    </form>
  `,
  standalone: true,
  imports: [ReactiveFormsModule]
})
export class PendingSampleComponent {
  private readonly validator = inject(EmailValidatorService);
  protected readonly form = new FormGroup({
    email: new FormControl('', {
      validators: [Validators.required, Validators.email],
      asyncValidators: [this.validator.unique()],
      updateOn: 'blur'
    })
  });
  protected readonly isPending = toSignal(
    this.form.statusChanges.pipe(map(status => status === 'PENDING')),
    { initialValue: false }
  );
}
```

## ベストプラクティス
- フォーム送信はisPendingがfalseのときだけ許可する
- スピナーやメッセージはpendingフラグを単一のソースにまとめて制御する
- statusChangesはtakeUntilDestroyedで購読解除しメモリリークを防ぐ

## 注意点
- 複数のAsyncValidatorがある場合、いずれかが完了するまでPENDINGが維持される
- setAsyncValidatorsを再設定するとPENDINGが再度発生する点を意識する
- 状態判定をvalueChangesだけで行うとPENDINGの変化を見逃すことがある

## 関連技術
- statusChanges
- toSignal
- ReactiveFormsModule
