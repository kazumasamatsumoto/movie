# #710 「複数バリデーターの適用」

## 概要
複数のValidatorsは配列指定で適用でき、errorsオブジェクトにすべてのエラーが格納されるためUIで優先順位を決めて表示する。

## 学習目標
- 複数バリデーションの設定方法を理解する
- errorsオブジェクトの扱いを学ぶ
- エラー表示の設計指針を把握する

## 技術ポイント
- validators: [Validators.required, Validators.maxLength(20)]のように記述
- errorsに各バリデーターのキーが並ぶ
- UIでエラー優先度を制御するヘルパーが有効

## 📺 画面表示用コード（動画用）
```html
<input [formControl]="userCtrl" />
<span *ngIf="userCtrl.errors?.required">必須です</span>
<span *ngIf="userCtrl.errors?.maxlength">20文字以内で入力してください</span>
```

## 💻 詳細実装例（学習用）
```typescript
protected userCtrl = new FormControl('', [
  Validators.required,
  Validators.maxLength(20)
]);
```

## ベストプラクティス
- 共通エラーメッセージマップを準備して表示を統一する
- 最も重要なエラーを先にユーザーへ伝える
- フォーム設定は定数にまとめて再利用する

## 注意点
- バリデーターを増やしすぎると性能に影響する
- 同じエラーキーを複数返さないよう命名する
- 表示ロジックが複雑化しないようユーティリティを使う

## 関連技術
- Validators
- エラー表示
- フォームUX
