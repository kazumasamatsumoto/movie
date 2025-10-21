# #738 「バリデーションのパフォーマンス」

## 概要
大規模フォームでの検証負荷を抑えるための最適化手法を解説する。

## 学習目標
- updateOnオプションで検証タイミングを調整する方法を理解する
- 高コストなバリデーターをメモ化・キャッシュする手法を学ぶ
- 非同期検証の呼び出し頻度を抑えてUXを最適化する

## 技術ポイント
- updateOn: 'blur'や'submit'で同期検証を遅延できる
- debounceTimeやdistinctUntilChangedでAPIコールを削減する
- shareReplayやキャッシュサービスで同一入力の再検証を避ける

## 📺 画面表示用コード（動画用）
```typescript
const profileForm = new FormGroup({
  email: new FormControl('', {
    validators: [Validators.required, Validators.email],
    asyncValidators: [this.emailValidator.unique()],
    updateOn: 'blur'
  }),
  bio: new FormControl('', {
    validators: [Validators.maxLength(200)],
    updateOn: 'submit'
  })
});
```

## 💻 詳細実装例（学習用）
```typescript
@Injectable({ providedIn: 'root' })
export class CachedEmailValidatorService {
  private readonly api = inject(AccountApiService);
  private readonly cache = new Map<string, boolean>();

  unique(): AsyncValidatorFn {
    return async control => {
      const email = control.value;
      if (!email) return null;
      if (this.cache.has(email)) {
        return this.cache.get(email) ? null : { emailTaken: true };
      }
      const response = await firstValueFrom(
        this.api.verifyEmail(email).pipe(take(1))
      );
      this.cache.set(email, response.available);
      return response.available ? null : { emailTaken: true };
    };
  }
}

@Component({
  selector: 'app-profile-form',
  templateUrl: './profile-form.component.html',
  standalone: true,
  imports: [ReactiveFormsModule]
})
export class ProfileFormComponent {
  private readonly emailValidator = inject(CachedEmailValidatorService);
  protected readonly form = new FormGroup({
    email: new FormControl('', {
      validators: [Validators.required, Validators.email],
      asyncValidators: [this.emailValidator.unique()],
      updateOn: 'blur'
    }),
    bio: new FormControl('', {
      validators: [Validators.maxLength(200)],
      updateOn: 'submit'
    })
  });
}
```

## ベストプラクティス
- 重いバリデーターはサービスでメモ化して再利用する
- ChangeDetectionStrategy.OnPushと組み合わせて再描画を抑える
- debounceTimeやupdateOnで検証トリガーを適切に抑制する

## 注意点
- setValueやpatchValueの多用は不要な再検証を誘発する
- キャッシュはバックエンドで値が変わったケースを考慮して無効化戦略を持つ
- 同期バリデーター内で重い処理を行うとUIスレッドがブロックされる

## 関連技術
- updateOn
- debounceTime
- firstValueFrom
