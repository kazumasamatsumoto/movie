# #673 「FormGroup.value プロパティ」

## 概要
FormGroup.valueプロパティはコントロール構造から型推論され、nonNullable設定でnullを除外できる。値の更新はsetValueやpatchValueを利用する。

## 学習目標
- FormGroup.valueの型推論を理解する
- nonNullable設定での型安全を学ぶ
- 値更新メソッドとの役割分担を把握する

## 技術ポイント
- フォーム構造の型がvalue型に反映される
- 非nullableコントロールはvalueからnullを排除
- valueを書き換えてもフォームは更新されない

## 📺 画面表示用コード（動画用）
```typescript
protected profileGroup = new FormGroup({
  name: new FormControl('', { nonNullable: true }),
  email: new FormControl('', { nonNullable: true })
});

protected get profileValue() {
  return this.profileGroup.value;
}
```

## 💻 詳細実装例（学習用）
```typescript
type ProfileValue = ReturnType<typeof this.profileGroup['value']>;

protected updateProfile(value: ProfileValue): void {
  this.profileGroup.setValue(value);
}
```

## ベストプラクティス
- フォームの型とDTOの型を揃えて変換コストを下げる
- valueをラップしたgetterでテンプレートに渡す
- 非nullable設定を活用してnullチェックを減らす

## 注意点
- valueを直接代入しても状態は変わらない
- FormArrayを含む場合は配列型のnull許容に注意
- strictTemplatesでエラーが出たらフォームの型を確認する

## 関連技術
- 型推論
- nonNullable
- setValue
