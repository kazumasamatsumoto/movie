# #691 「FormBuilder の省略記法」

## 概要
FormBuilderの省略記法は配列記法で初期値とバリデーションをまとめられるが、可読性とのバランスを考えてfb.controlなどと使い分ける。

## 学習目標
- 省略記法の書き方を理解する
- 可読性を考慮した使い分けを学ぶ
- チームでのスタイルガイド作成の重要性を知る

## 技術ポイント
- 配列記法は[value, validators?, asyncValidators?]
- fb.controlとの併用で柔軟に表現できる
- コーディング規約で統一する

## 📺 画面表示用コード（動画用）
```typescript
this.fb.group({
  name: ['', [Validators.required]],
  age: [20],
  email: this.fb.control('', { validators: [Validators.email] })
});
```

## 💻 詳細実装例（学習用）
```markdown
- 配列記法: `[value, validators, asyncValidators]`
- オブジェクト記法: `fb.control(value, { validators })`
- チームで使い分けルールを決めてレビューでチェック
```

## ベストプラクティス
- 省略記法を使う箇所と使わない箇所をスタイルガイドに明記する
- 複雑なバリデーションはfb.controlでオブジェクト指定に切り替える
- レビューで記法の統一を確認する

## 注意点
- 配列記法にasyncValidatorsを渡し忘れやすい
- 省略記法だけに頼ると可読性が低下する
- チームの合意なしに記法を混在させない

## 関連技術
- FormBuilder
- コーディング規約
- 可読性
