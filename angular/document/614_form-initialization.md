# #614 「フォームの初期化」

## 概要
フォーム初期化は初期値の設定、非同期データの適用、状態遷移の制御を含み、ライフサイクルに合わせて実装する必要がある。

## 学習目標
- 初期値の設定方法をアプローチ別に理解する
- 非同期データの差し込み方を学ぶ
- 初期化後の状態制御のポイントを把握する

## 技術ポイント
- リアクティブフォームはFormBuilderで初期値を定義
- patchValueで一部のコントロールのみ更新
- テンプレート駆動は[(ngModel)]に初期データを割り当てる

## 📺 画面表示用コード（動画用）
```typescript
this.form = this.fb.group({
  name: ['初期太郎'],
  email: ['', [Validators.email]]
});
```

## 💻 詳細実装例（学習用）
```typescript
protected ngOnInit(): void {
  this.userService.fetch().subscribe(user => {
    this.form.patchValue({
      name: user.name,
      email: user.email
    });
  });
}

protected setTemplateInitialValue(): void {
  this.model = { name: '初期太郎', email: '' };
}
```

## ベストプラクティス
- 初期化処理をメソッド化して再利用しやすくする
- 非同期データはsubscribe内でmarkAsPristineを検討する
- テンプレート駆動ではmodelオブジェクトを定義しておく

## 注意点
- patchValueは存在しないキーに対しては例外を投げないので注意
- 非同期処理のキャンセルを考慮しないとメモリリークになる
- 初期化後に状態をログするときはタイミングを揃える

## 関連技術
- FormBuilder
- patchValue
- ngOnInit
