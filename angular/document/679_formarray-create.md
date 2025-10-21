# #679 「FormArray の作成」

## 概要
FormArrayは初期要素の配列を渡して生成し、型パラメータで要素のFormControl型を指定すると補完と型安全性が高まる。

## 学習目標
- FormArrayコンストラクタの書き方を理解する
- 型パラメータで要素型を固定する方法を学ぶ
- 初期値とバリデーションの設定を把握する

## 技術ポイント
- 第一引数にAbstractControlの配列を渡す
- ジェネリクスで要素の型を指定できる
- 同期・非同期バリデーションを付与できる

## 📺 画面表示用コード（動画用）
```typescript
protected phonesCtrl = new FormArray<FormControl<string>>([
  new FormControl('090-1234-5678'),
  new FormControl('03-1111-2222')
]);
```

## 💻 詳細実装例（学習用）
```typescript
protected phonesCtrl = new FormArray<FormControl<string>>([
  new FormControl('', { validators: [Validators.required] })
], {
  validators: [Validators.minLength(1)]
});
```

## ベストプラクティス
- 要素生成はヘルパー関数で統一する
- FormArrayの型をtypeエイリアスで表現する
- バリデーションは配列全体と要素単位で分けて設計する

## 注意点
- 型注釈を省略するとvalueが(unknown)[]になりがち
- 配列全体のバリデーションはValidators.minLengthなどを使う
- FormArray.controlsを直接再代入しない

## 関連技術
- FormArray
- ジェネリクス
- Validators
