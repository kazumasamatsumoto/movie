# #711 「Validators.compose() - 組み合わせ」

## 概要
Validators.composeは複数のValidatorFnを合成して単一のバリデーターを作成し、共通ルールの再利用を容易にする。

## 学習目標
- composeの使い方を理解する
- 複合バリデーションの設計を学ぶ
- composeAsyncとの違いを把握する

## 技術ポイント
- compose([validatorA, validatorB])で新しいValidatorFnを生成
- nullや空配列を渡すとnullが返る
- composeAsyncで非同期バリデーターを合成できる

## 📺 画面表示用コード（動画用）
```typescript
const positiveInteger = Validators.compose([
  Validators.required,
  Validators.pattern(/^[0-9]+$/)
]);
```

## 💻 詳細実装例（学習用）
```typescript
protected readonly positiveInteger = Validators.compose([
  Validators.required,
  Validators.pattern(/^[0-9]+$/)
]);

protected quantityCtrl = new FormControl('', this.positiveInteger);
```

## ベストプラクティス
- composeでまとめたバリデーターはユニットテストを書く
- 共通ルールをsharedモジュールに置いて再利用する
- エラーキーが重複しないよう命名する

## 注意点
- compose内でnullを返すと以降のバリデーションがスキップされる
- 複数の重い処理を合成するとパフォーマンスに影響
- composeAsyncと混在させる場合は順序に注意

## 関連技術
- Validators.compose
- ValidatorFn
- 再利用性
