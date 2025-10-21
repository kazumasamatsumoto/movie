# #694 「formGroupName ディレクティブ」

## 概要
formGroupNameは親FormGroup内のサブグループをテンプレートで扱うディレクティブで、ネスト構造を整理してformControlNameを再利用できる。

## 学習目標
- formGroupNameの役割を理解する
- ネストフォームの記述方法を学ぶ
- 可読性を高めるテンプレート構造を把握する

## 技術ポイント
- 親に[formGroup]、子にformGroupNameを指定
- formGroupName内部ではformControlNameが親グループのキーになる
- ネストが深い場合はコンポーネント分割が有効

## 📺 画面表示用コード（動画用）
```html
<div formGroupName="profile">
  <input formControlName="displayName" />
  <textarea formControlName="bio"></textarea>
</div>
```

## 💻 詳細実装例（学習用）
```typescript
protected accountForm = new FormGroup({
  profile: new FormGroup({
    displayName: new FormControl(''),
    bio: new FormControl('')
  })
});
```

## ベストプラクティス
- グループ名を定数化してテンプレートと共有する
- サブグループは独立した小コンポーネントで再利用する
- formGroupNameの深さを揃えて読みやすくする

## 注意点
- テンプレート構造が複雑になるとバグが潜みやすい
- フォーム生成前にテンプレートへアクセスするとnull参照になる
- 入れ子が深い場合はChangeDetectionの影響を受けやすい

## 関連技術
- formGroupName
- ネストフォーム
- テンプレート設計
