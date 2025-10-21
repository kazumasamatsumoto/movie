# #639 「NgModel の活用」

## 概要
NgModelディレクティブは値・状態・エラーを管理し、テンプレート参照変数を通じてテンプレートから詳細情報を取得できる。

## 学習目標
- NgModelインスタンスの主なプロパティを理解する
- #control="ngModel"の利用方法を学ぶ
- UI制御への応用例を把握する

## 技術ポイント
- ngModel.valueやngModel.validにアクセス可能
- errorsプロパティでバリデーション情報を取得
- statusChanges/valueChangesで変化を監視できる

## 📺 画面表示用コード（動画用）
```html
<input name="name" ngModel #nameCtrl="ngModel" />
```

## 💻 詳細実装例（学習用）
```typescript
@ViewChild('nameCtrl')
protected nameCtrl?: NgModel;

protected logCtrl(): void {
    console.log(this.nameCtrl?.value, this.nameCtrl?.valid);
}
```

## ベストプラクティス
- テンプレート参照でエラーメッセージを制御する
- ViewChildでNgModelを取得してデバッグに活用する
- ステータス変化を監視してUX向上に役立てる

## 注意点
- テンプレート参照変数のスコープに注意
- NgModelへのアクセスはコンポーネント初期化後に行う
- NgModelを過剰に参照するとテンプレートが複雑化する

## 関連技術
- NgModel
- テンプレート参照変数
- 状態管理
