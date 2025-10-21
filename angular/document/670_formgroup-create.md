# #670 「FormGroup の作成」

## 概要
FormGroupはコントロール辞書をコンストラクタに渡して生成し、ネストしたFormGroupやFormArrayを組み合わせて複雑なフォーム構造を表現できる。

## 学習目標
- FormGroupコンストラクタの書き方を理解する
- ネスト構造の定義方法を学ぶ
- フォーム設計時に構造を先に決める重要性を把握する

## 技術ポイント
- 第一引数はAbstractControl辞書
- オプションで同期・非同期バリデーションを渡せる
- ネストしたFormGroupで複雑なフォームを構築

## 📺 画面表示用コード（動画用）
```typescript
protected accountGroup = new FormGroup({
  credentials: new FormGroup({
    email: new FormControl(''),
    password: new FormControl('')
  }),
  profile: new FormGroup({
    displayName: new FormControl('')
  })
});
```

## 💻 詳細実装例（学習用）
```typescript
protected accountGroup = new FormGroup({
  credentials: new FormGroup({
    email: new FormControl('', { validators: [Validators.required, Validators.email] }),
    password: new FormControl('', { validators: [Validators.required] })
  }),
  profile: new FormGroup({
    displayName: new FormControl('', { nonNullable: true })
  })
});
```

## ベストプラクティス
- 辞書型に合わせた型定義を用意して補完を効かせる
- グループ生成は専用ファクトリ関数に切り出す
- ネストが深い場合はFormBuilderで読みやすくする

## 注意点
- キー名のタイプミスでテンプレートと同期しなくなる
- 巨大なグループは責務が肥大化するため分割する
- 同期・非同期バリデーションの順序に注意する

## 関連技術
- FormGroup
- ネストフォーム
- 設計パターン
