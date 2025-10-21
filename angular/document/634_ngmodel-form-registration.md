# #634 「ngModel とフォーム登録」

## 概要
ngModelはNgFormに登録されることで状態管理やバリデーションが有効になり、必要に応じてstandalone設定でフォーム登録を制御できる。

## 学習目標
- フォーム登録とNgFormの関係を理解する
- 登録されたコントロールの取得方法を学ぶ
- standalone設定で登録制御する方法を把握する

## 技術ポイント
- NgForm.controlsで個別コントロールにアクセス
- ngModelOptions="{ standalone: true }"でフォーム登録を外す
- フォーム登録によりvalid/invalidなどの判定が利用可能

## 📺 画面表示用コード（動画用）
```html
<input name="age" [(ngModel)]="profile.age" [ngModelOptions]="{ updateOn: "blur" }" />
```

## 💻 詳細実装例（学習用）
```typescript
@ViewChild('profileForm')
protected profileForm?: NgForm;

protected logControlState(): void {
    const ageControl = this.profileForm?.controls['age'];
    console.log(ageControl?.valid, ageControl?.value);
}
```

## ベストプラクティス
- フォーム登録が不要なものはstandalone指定する
- NgFormをViewChildで取得して状態を監視する
- updateOnオプションで検証タイミングを調整する

## 注意点
- standalone指定を忘れると予期せぬバリデーションが走る
- controls参照はundefinedチェックを行う
- 更新タイミングを変更するとUXに影響する

## 関連技術
- NgForm.controls
- ngModelOptions
- テンプレート駆動フォーム
