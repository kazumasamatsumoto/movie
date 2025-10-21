# #740 「バリデーションのテスト」

## 概要
同期・非同期バリデーターをユニットテストで検証する手法を紹介する。

## 学習目標
- ValidatorFnとAsyncValidatorFnを直接呼び出して検証する方法を理解する
- fakeAsyncとtickで非同期バリデーションを待機する手順を学ぶ
- フォーム全体のステータスを検証するテストの書き方を把握する

## 技術ポイント
- FormControlにバリデーターを設定し、errorsの値で期待値を確認する
- AsyncValidatorはfakeAsyncとtick、またはfirstValueFromで待機する
- statusChangesを購読して状態遷移をアサートする

## 📺 画面表示用コード（動画用）
```typescript
it('invalid email triggers email error', () => {
  const control = new FormControl('invalid', [Validators.email]);
  expect(control.errors?.['email']).toBeTrue();
});
```

```typescript
it('marks username as taken', fakeAsync(() => {
  const validator = usernameAsyncValidator();
  const control = new FormControl('zunda');
  let result: ValidationErrors | null = null;
  validator(control).subscribe(value => (result = value));
  tick(300);
  expect(result).toEqual({ usernameTaken: true });
}));
```

## 💻 詳細実装例（学習用）
```typescript
describe('ProfileFormComponent', () => {
  let fixture: ComponentFixture<ProfileFormComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ProfileFormComponent],
      providers: [{ provide: UsernameValidatorService, useClass: FakeUsernameValidator }]
    }).compileComponents();

    fixture = TestBed.createComponent(ProfileFormComponent);
    fixture.detectChanges();
  });

  it('disables submit while pending', fakeAsync(() => {
    const component = fixture.componentInstance;
    component.form.get('username')!.setValue('checking');
    tick();
    expect(component.form.pending).toBeTrue();
  }));
});
```

## ベストプラクティス
- バリデーターは純粋関数として単体テストを優先する
- 非同期テストはfakeAsyncとtick、またはlastValueFromで明示的に待機する
- コンポーネントテストではUIとフォーム状態の両方をアサートする

## 注意点
- setValue直後はstatusChangesが非同期で発火するためtickが必要
- HttpTestingControllerで外部APIをモックし忘れるとテストがハングする
- 複数AsyncValidatorがある場合は結果を配列で検証する

## 関連技術
- fakeAsync
- tick
- TestBed
