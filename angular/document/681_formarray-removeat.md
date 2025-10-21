# #681 「FormArray.removeAt() - 要素削除」

## 概要
FormArray.removeAtは指定インデックスのコントロールを削除し、残りの要素が詰められる。削除時のUXやデータ整合性に注意する。

## 学習目標
- removeAtの使い方を理解する
- 削除後の配列状態を把握する
- 削除時のUX設計を考える

## 技術ポイント
- removeAtは0ベースインデックスを受け取る
- 削除後にlengthが減りインデックスが詰まる
- valueChangesやstatusChangesが発火する

## 📺 画面表示用コード（動画用）
```typescript
protected removePhone(index: number): void {
  this.phonesCtrl.removeAt(index);
}
```

## 💻 詳細実装例（学習用）
```typescript
protected phonesCtrl = new FormArray<FormControl<string>>([]);

protected removePhone(index: number): void {
  if (index < 0 || index >= this.phonesCtrl.length) {
    return;
  }
  this.phonesCtrl.removeAt(index);
}
```

## ベストプラクティス
- 削除前に確認ダイアログやundo機能を検討する
- 削除後のフォーカス位置を調整する
- 配列が空になった場合のバリデーションを設計する

## 注意点
- インデックス範囲外を削除すると例外になる
- 削除後にフォーム値が即時反映されるため状態管理に注意
- バックエンドとの同期が必要な場合は削除イベントを記録する

## 関連技術
- FormArray.removeAt
- UX設計
- 状態同期
