# #666 「FormControl.setValue() メソッド」

## 概要
setValueはFormControlに完全な値を設定し、バリデーションを再評価する。emitEventやonlySelfオプションで通知の制御が可能。

## 学習目標
- setValueの基本挙動を理解する
- emitEvent/onlySelfオプションの用途を学ぶ
- バリデーション再評価を意識した更新設計を行う

## 技術ポイント
- setValueは同期的に値と状態を更新
- emitEvent:falseでvalueChanges通知を抑制
- onlySelf:trueで親グループへの伝播を止められる

## 📺 画面表示用コード（動画用）
```html
<input [formControl]="priceCtrl" type="number" />
```

## 💻 詳細実装例（学習用）
```typescript
protected priceCtrl = new FormControl(1000, { nonNullable: true });

protected applyDiscount(): void {
  this.priceCtrl.setValue(800, { emitEvent: false });
}
```

## ベストプラクティス
- emitEvent:falseを使って不要なAPI呼び出しを防ぐ
- 値更新後にstatusChangesで状態を確認する
- オプション引数は共通ユーティリティにまとめる

## 注意点
- setValueの値は型と完全に一致している必要がある
- emitEvent:falseにするとUI更新ロジックが動かない可能性がある
- onlySelf:trueで親グループが古い状態のままになる場合がある

## 関連技術
- setValue
- バリデーション再評価
- Reactive Forms API
