# #609 「<form> タグの役割」

## 概要
formタグはsubmitイベント管理、ブラウザ機能、アクセシビリティ向上など多くの役割を担い、Angularフォームでも必須の要素である。

## 学習目標
- formタグが提供する標準機能を理解する
- Angularでのsubmitイベント連携方法を学ぶ
- アクセシビリティ観点での役割を把握する

## 技術ポイント
- formタグはEnterキー送信やネイティブ検証を提供
- AngularのngSubmitはformタグから発火
- methodやnovalidate属性で動作を制御可能

## 📺 画面表示用コード（動画用）
```html
<form novalidate (ngSubmit)="submit()">
  <input name="email" ngModel required />
</form>
```

## 💻 詳細実装例（学習用）
```typescript
protected submit(): void {
  console.log('submitted');
}

protected preventNativeValidation(form: HTMLFormElement): void {
  form.setAttribute('novalidate', '');
}
```

## ベストプラクティス
- 必ずformタグでコントロールを囲みネイティブ機能を活かす
- novalidate指定でブラウザ検証を制御しAngular側に統一
- methodやactionを適切に設定しSSRやPOST送信にも備える

## 注意点
- formタグを省略するとngSubmitが発火せず処理が動かない
- ネストしたformは無効で予期せぬ動作を引き起こす
- 特にEnterキー送信をテストしてUXを保証する

## 関連技術
- HTMLフォーム仕様
- ngSubmit
- アクセシビリティ
