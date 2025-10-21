# #735 「Promise ベースの検証」

## 概要
AsyncValidatorFnはPromiseを返す処理にも対応しており、async/awaitで読みやすい非同期バリデーションを実装できる。

## 学習目標
- Promiseで非同期バリデーションを記述する方法を理解する
- async/awaitで検証ロジックを整理する
- resolve時はnull、エラー時はValidationErrorsを返す仕様を確認する

## 技術ポイント
- AsyncValidatorFnの戻り値はPromise<ValidationErrors | null>でもよい
- async functionをそのままAsyncValidatorとして渡せる
- try/catchでネットワークエラーを補足しUIに伝播させる

## 📺 画面表示用コード（動画用）
```typescript
const uniqueValidator: AsyncValidatorFn = async control => {
  if (!control.value) return null;
  const result = await api.checkUsername(control.value);
  return result.available ? null : { usernameTaken: true };
};
```

## 💻 詳細実装例（学習用）
```typescript
@Injectable({ providedIn: 'root' })
export class UsernameValidatorService {
  private readonly accountApi = inject(AccountApiService);

  unique(): AsyncValidatorFn {
    return async control => {
      if (!control.value) return null;
      try {
        const response = await this.accountApi.verify(control.value);
        return response.available ? null : { usernameTaken: true };
      } catch {
        return { serverError: true };
      }
    };
  }
}

@Component({
  selector: 'app-username-field',
  templateUrl: './username-field.component.html',
  standalone: true,
  imports: [ReactiveFormsModule]
})
export class UsernameFieldComponent {
  private readonly validator = inject(UsernameValidatorService);
  protected readonly usernameCtrl = new FormControl('', {
    validators: [Validators.required],
    asyncValidators: [this.validator.unique()],
    updateOn: 'blur'
  });
}
```

## ベストプラクティス
- async/awaitで可読性を高めつつnullとエラーの返却を厳密に管理する
- updateOn: 'blur'を併用して不要な検証呼び出しを避ける
- finallyでローディングフラグを確実に更新する

## 注意点
- Promiseを返す関数でも検証中はPENDING状態になることを把握する
- resolveでValidationErrors以外を返すと型エラーになる
- キャッシュしないと高速入力で複数Promiseが並列する点に注意する

## 関連技術
- AsyncValidatorFn
- async/await
- updateOnオプション
