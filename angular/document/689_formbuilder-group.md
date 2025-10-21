# #689 「fb.group() メソッド」

## 概要
fb.groupはオブジェクト記法でFormGroupを生成でき、配列記法と併用して初期値やバリデーションを簡潔に記述できる。

## 学習目標
- fb.groupの構文を理解する
- 配列記法との組み合わせ方を学ぶ
- ネストしたグループの書き方を把握する

## 技術ポイント
- 値は[key: controlConfig]のオブジェクトで渡す
- controlConfigは配列やFormControlで表現できる
- 第二引数でグループレベルのバリデーションを指定

## 📺 画面表示用コード（動画用）
```typescript
this.fb.group({
  email: ['', [Validators.required, Validators.email]],
  password: ['', Validators.required]
});
```

## 💻 詳細実装例（学習用）
```typescript
protected readonly fb = inject(FormBuilder);

protected loginForm = this.fb.group({
  credentials: this.fb.group({
    email: ['', [Validators.required, Validators.email]],
    password: ['', Validators.required]
  })
}, {
  validators: [this.matchDomainValidator]
});

private matchDomainValidator(group: AbstractControl): ValidationErrors | null {
  const email = group.get('credentials.email')?.value as string | null;
  if (email && email.endsWith('@example.com')) {
    return null;
  }
  return { domain: true };
}
```

## ベストプラクティス
- ネスト構造はオブジェクトをそのまま使って表現する
- グループレベルのバリデーションは第二引数で定義する
- 大きなフォームは小さなグループに分割して読みやすくする

## 注意点
- 配列記法は読みづらくなる場合があるのでコメントを付ける
- ネストしたキーへのアクセスはgetで正確に行う
- バリデーション関数は純粋関数にする

## 関連技術
- FormBuilder.group
- ネストフォーム
- バリデーション
