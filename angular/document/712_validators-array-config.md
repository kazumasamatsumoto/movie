# #712 「バリデーターの配列指定」

## 概要
バリデーターは配列で指定して複数設定でき、FormBuilderの省略記法とも組み合わせられる。エラー表示はUI側で優先度を制御する。

## 学習目標
- 配列指定の構文を理解する
- 省略記法との使い分けを学ぶ
- エラー表示の優先制御を意識する

## 技術ポイント
- FormControl(値, [validatorA, validatorB])形式で設定
- FormBuilderのgroupでも配列指定が可能
- 配列順は実行順を保証するが依存しない設計が望ましい

## 📺 画面表示用コード（動画用）
```typescript
this.fb.control('', [Validators.required, Validators.maxLength(10)]);
```

## 💻 詳細実装例（学習用）
```typescript
protected readonly fb = inject(FormBuilder);

protected profileForm = this.fb.group({
  username: ['', [Validators.required, Validators.maxLength(20)]]
});
```

## ベストプラクティス
- 複数箇所で同じ設定を使うなら配列自体を定数化する
- 読みにくい場合は1行1バリデーターで記述する
- UIでエラー表示順を制御するヘルパー関数を用意する

## 注意点
- 配列にnullを含めるとエラーになる
- オプション付きバリデーターはcomposeでまとめたほうが読みやすい
- 配列記法と省略記法が混在すると可読性が落ちる

## 関連技術
- Validators
- FormBuilder
- 可読性
