# #707 「Validators.max() - 最大値」

## 概要
Validators.maxは値が指定上限を超えた場合にエラーを返し、errors.maxにactualとmaxを保持する。

## 学習目標
- maxバリデーションの挙動を理解する
- UIとの組み合わせを学ぶ
- エラー情報を活用したメッセージ設計を把握する

## 技術ポイント
- valueがmaxより大きいとerrors.maxが設定
- max属性と併用して入力段階で制御
- 数値型コントロールで扱うと型安全

## 📺 画面表示用コード（動画用）
```html
<input type="number" [formControl]="quantityCtrl" max="10" />
<span *ngIf="quantityCtrl.errors?.max">最大10まで入力できます</span>
```

## 💻 詳細実装例（学習用）
```typescript
protected quantityCtrl = new FormControl(1, [Validators.max(10)]);
```

## ベストプラクティス
- 上限値は定数として管理し複数箇所で共有する
- 上限超過の理由を具体的に表示する
- range入力ならminとmaxを組み合わせる

## 注意点
- max属性を指定しても貼り付けなどで超える場合がある
- フォーム値が文字列の場合はNumber()で変換する
- 小数点の扱いを要件に合わせて考慮する

## 関連技術
- Validators.max
- 数値入力
- UX
