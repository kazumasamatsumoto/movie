# #705 「Validators.maxLength() - 最大文字数」

## 概要
Validators.maxLength(n)は文字数がnを超えた場合にエラーを返し、errors.maxlengthにactualLengthとrequiredLengthが含まれる。

## 学習目標
- maxLengthの挙動を理解する
- HTML属性との組み合わせを学ぶ
- エラー情報の活用方法を把握する

## 技術ポイント
- actualLengthとrequiredLengthから超過文字数を算出
- maxlength属性で入力自体を制限できる
- 空文字はエラーにならないためrequiredと併用

## 📺 画面表示用コード（動画用）
```html
<input [formControl]="nicknameCtrl" maxlength="12" />
<span *ngIf="nicknameCtrl.errors?.maxlength">
  最大{{ nicknameCtrl.errors?.maxlength.requiredLength }}文字までです
</span>
```

## 💻 詳細実装例（学習用）
```typescript
protected nicknameCtrl = new FormControl('', [Validators.required, Validators.maxLength(12)]);
```

## ベストプラクティス
- maxlength属性とバリデーションを併用してUXを高める
- エラーメッセージに現在の文字数を表示する
- 余裕を持った上限値を設定して入力を阻害しない

## 注意点
- HTML属性だけでは貼り付けによる超過を防げないケースがある
- maxLengthもUTF-16単位でカウントされる
- 多言語対応で文字数制限が異なる場合に注意

## 関連技術
- Validators.maxLength
- maxlength属性
- UX
