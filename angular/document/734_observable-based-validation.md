# #734 「Observable ベースの検証」

## 概要
Reactive FormsのvalueChangesをObservableとして扱い、非同期APIや複数の検証ロジックをストリームで組み立てるパターンを解説する。

## 学習目標
- Observableで検証結果をストリーム化する方法を理解する
- switchMapによる最新入力のみの非同期検証を学ぶ
- エラーとローディング状態の伝播を設計する

## 技術ポイント
- valueChangesにstartWithを加えて初期値を評価する
- switchMapで古いリクエストを自動キャンセルする
- shareReplayで複数購読先へ結果を配信する

## 📺 画面表示用コード（動画用）
```typescript
const emailCtrl = new FormControl('');
const emailStatus$ = emailCtrl.valueChanges.pipe(
  startWith(emailCtrl.value),
  debounceTime(300),
  switchMap(value => api.validateEmail(value)),
  shareReplay({ bufferSize: 1, refCount: true })
);
```

## 💻 詳細実装例（学習用）
```typescript
@Component({
  selector: 'app-email-validator',
  templateUrl: './email-validator.component.html',
  standalone: true,
  imports: [ReactiveFormsModule, AsyncPipe, NgIf]
})
export class EmailValidatorComponent {
  private readonly emailService = inject(EmailValidationService);
  protected readonly emailCtrl = new FormControl('', [Validators.email]);
  protected readonly result$ = this.emailCtrl.valueChanges.pipe(
    startWith(this.emailCtrl.value),
    debounceTime(300),
    distinctUntilChanged(),
    switchMap(email =>
      this.emailService.verify(email).pipe(
        map(valid => (valid ? null : { emailTaken: true })),
        catchError(() => of({ network: true }))
      )
    ),
    shareReplay({ bufferSize: 1, refCount: true })
  );
}
```

## ベストプラクティス
- 検証結果はObservableとして保持し、AsyncPipeでテンプレートに描画する
- APIアクセスはサービス層へ切り出し、テストと再利用性を高める
- shareReplayで検証結果をキャッシュし、余計なHTTP呼び出しを防ぐ

## 注意点
- catchErrorでエラーをnullにすると失敗を検知できないため避ける
- debounceTimeはUI応答性を損なわない値に調整する
- 多段のswitchMapでキャンセルが複雑になる場合はexhaustMap等も検討する

## 関連技術
- FormControl.valueChanges
- RxJS switchMap
- shareReplay
