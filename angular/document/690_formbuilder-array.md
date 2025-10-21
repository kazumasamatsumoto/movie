# #690 「fb.array() メソッド」

## 概要
fb.arrayはFormArrayを生成するショートハンドで、要素を配列記法やfb.controlで定義し、全体バリデーションも指定できる。

## 学習目標
- fb.arrayの記法を理解する
- 要素ファクトリの設計を学ぶ
- 配列レベルのバリデーション設定を把握する

## 技術ポイント
- fb.array(initialControls, validators)で生成
- 要素は配列記法またはfb.group/fb.controlを利用
- 第二引数でminLengthなどの全体ルールを設定

## 📺 画面表示用コード（動画用）
```typescript
protected linksCtrl = this.fb.array([
  this.fb.control('', Validators.required)
]);
```

## 💻 詳細実装例（学習用）
```typescript
protected readonly fb = inject(FormBuilder);

protected linksCtrl = this.fb.array([
  this.createLinkControl()
], [Validators.minLength(1)]);

protected createLinkControl(): FormControl<string> {
  return this.fb.control('', { nonNullable: true });
}
```

## ベストプラクティス
- 要素生成はcreateXXXControlなどのメソッドにまとめる
- 配列レベルのバリデーションを活用して入力数を制限する
- fb.array内でも型パラメータを活用する

## 注意点
- 配列記法でvalidatorsを指定する場合は構文ミスに注意
- FormArrayの型定義を怠るとvalueがunknownになる
- バリデーション関数内でmutableな処理を避ける

## 関連技術
- FormBuilder.array
- FormArray
- バリデーション
