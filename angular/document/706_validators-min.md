# #706 「Validators.min() - 最小値」

## 概要
Validators.minは数値が指定した最小値未満の場合にエラーを返し、errors.minにactualとminを設定する。

## 学習目標
- minバリデーションの挙動を理解する
- UIと組み合わせた最小値制御を学ぶ
- エラー情報の活用方法を把握する

## 技術ポイント
- フォーム値がmin未満でerrors.minが設定される
- type="number"やinputmode="numeric"でUXを向上
- min属性と併用して入力自体を制限できる

## 📺 画面表示用コード（動画用）
```html
<input type="number" [formControl]="ageCtrl" min="18" />
<span *ngIf="ageCtrl.errors?.min">18歳以上が必要です</span>
```

## 💻 詳細実装例（学習用）
```typescript
protected ageCtrl = new FormControl<number | null>(null, Validators.min(18));
```

## ベストプラクティス
- フォーム値はnumber型で扱いparseIntを避ける
- min属性を組み合わせて入力段階で制御する
- エラーメッセージに不足分を表示してユーザーを案内する

## 注意点
- 初期値nullはminチェックに通らない点に注意
- フォーム値が文字列になる環境ではNumber()で変換する
- 国際化で小数点表記が変わる場合を考慮する

## 関連技術
- Validators.min
- number入力
- UX
