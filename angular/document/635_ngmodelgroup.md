# #635 「ngModelGroup - グループ化」

## 概要
ngModelGroupはテンプレート駆動フォームでフィールドをグループ化し、ネストされたフォーム構造とグループ単位のバリデーションを可能にする。

## 学習目標
- ngModelGroupの記法と構造を理解する
- グループ単位の状態確認方法を学ぶ
- ネストオブジェクトとして値を扱う

## 技術ポイント
- ngModelGroup="address"でform.value.addressが生成される
- グループには#addressRef="ngModelGroup"で参照可能
- グループレベルのバリデーションディレクティブも適用できる

## 📺 画面表示用コード（動画用）
```html
<div ngModelGroup="address">
  <input name="zip" ngModel />
  <input name="city" ngModel />
</div>
```

## 💻 詳細実装例（学習用）
```typescript
@ViewChild('profileForm')
protected profileForm?: NgForm;

protected logAddress(): void {
    const value = this.profileForm?.value.address;
    console.log(value);
}
```

## ベストプラクティス
- 関連項目をグループ化しform.valueを整理する
- グループ参照をテンプレートで利用して状態表示する
- グループレベルのカスタムバリデーションを活用する

## 注意点
- グループ名の重複に注意
- ネストが深すぎると可読性が落ちる
- グループの有効性チェックを忘れない

## 関連技術
- ngModelGroup
- テンプレート駆動フォーム
- ネストフォーム
