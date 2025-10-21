# #704 「Validators.minLength() - 最小文字数」

## 概要
Validators.minLength(n)は入力値の文字数がn未満の場合にエラーを返し、errors.minlengthにactualLengthとrequiredLengthを設定する。

## 学習目標
- minLengthの挙動を理解する
- エラー情報の活用方法を学ぶ
- requiredとの併用理由を把握する

## 技術ポイント
- errors.minlength.requiredLengthとactualLengthが参照可能
- 空文字を許さない場合はrequiredを併用
- 文字数カウントはUTF-16単位で行われる

## 📺 画面表示用コード（動画用）
```html
<textarea [formControl]="bioCtrl"></textarea>
<span *ngIf="bioCtrl.errors?.minlength">
  あと{{ bioCtrl.errors?.minlength.requiredLength - bioCtrl.errors?.minlength.actualLength }}文字
</span>
```

## 💻 詳細実装例（学習用）
```typescript
protected bioCtrl = new FormControl('', [Validators.required, Validators.minLength(50)]);
```

## ベストプラクティス
- 残り文字数をリアルタイムで表示して入力支援する
- ローカライズされたメッセージに置き換える
- textareaにはmaxlength属性と組み合わせてUXを向上させる

## 注意点
- マルチバイト文字のカウントが想定と異なる場合がある
- 自動補完やペーストで文字数を超えるケースをテストする
- モバイル入力で変換中の文字が反映されない場合がある

## 関連技術
- Validators.minLength
- 文字数制限
- UX
