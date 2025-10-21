# #688 「fb.control() メソッド」

## 概要
fb.control(value, options)はFormControlを生成するショートハンドで、nonNullableやvalidatorsなどの設定を簡潔に記述できる。

## 学習目標
- fb.controlの使い方を理解する
- 配列記法との違いを把握する
- nonNullableなどのオプション設定を学ぶ

## 技術ポイント
- 第一引数が初期値、第二引数がオプション
- 配列記法よりも設定が明確になる
- FormControlを生成してgroupやarrayに組み込める

## 📺 画面表示用コード（動画用）
```typescript
const nameCtrl = this.fb.control('', { nonNullable: true });
```

## 💻 詳細実装例（学習用）
```typescript
protected readonly fb = inject(FormBuilder);

protected profileForm = this.fb.group({
  name: this.fb.control('', { nonNullable: true }),
  email: this.fb.control('', { validators: [Validators.email] })
});
```

## ベストプラクティス
- nonNullableやvalidatorsをオブジェクトで明示する
- メソッド内で新しいコントロールを生成するときに利用する
- 配列記法で読みづらい場合はfb.controlへ切り替える

## 注意点
- 第二引数でvalidatorsを指定しないと配列記法より長くなる
- 非同期バリデーションはasyncValidatorsプロパティに指定する
- フォーム構造が複雑な場合は読みやすさを優先する

## 関連技術
- FormBuilder.control
- nonNullable
- バリデーション設定
