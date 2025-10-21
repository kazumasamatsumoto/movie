# #672 「FormGroup の値取得」

## 概要
FormGroup.valueはコントロール辞書と同じ形のオブジェクトを返し、各プロパティはFormControlのnull許容に従う。取得後の型ガードが重要。

## 学習目標
- FormGroup.valueの型仕様を理解する
- null許容を考慮した値処理を学ぶ
- DTO整形の流れを把握する

## 技術ポイント
- valueはコントロールの型に従うオブジェクト
- nonNullable設定でnullを排除できる
- getRawValueを使うとdisabledも含めて取得可能

## 📺 画面表示用コード（動画用）
```typescript
protected submit(): void {
  const value = this.profileGroup.value;
  console.log(value?.name, value?.email);
}
```

## 💻 詳細実装例（学習用）
```typescript
protected profileGroup = new FormGroup({
  name: new FormControl('', { nonNullable: true }),
  email: new FormControl('', { validators: [Validators.email] })
});

protected toDto() {
  const value = this.profileGroup.value;
  if (!value) {
    return null;
  }
  return {
    name: value.name,
    email: value.email ?? ''
  };
}
```

## ベストプラクティス
- 非nullableが必要なフィールドはnonNullableで宣言する
- DTO整形用のユーティリティを用意する
- getRawValueとの違いを理解して使い分ける

## 注意点
- valueがnullを返すケースを想定する
- disabledコントロールの値は含まれない
- FormArrayが含まれる場合は配列の型も確認する

## 関連技術
- FormGroup.value
- DTO整形
- null安全
