# #683 「FormArray.clear() - 全削除」

## 概要
FormArray.clearは全要素を削除して空の配列にリセットし、valueChangesも発火するため追加のUX処理を検討する必要がある。

## 学習目標
- clearメソッドの挙動を理解する
- クリア後の状態とUXを把握する
- emitEventオプションの利用場面を学ぶ

## 技術ポイント
- clear()で全要素を削除
- lengthが0になりvalueは空配列
- emitEvent:falseで通知抑制可能

## 📺 画面表示用コード（動画用）
```typescript
protected clearPhones(): void {
  this.phonesCtrl.clear();
  this.phonesCtrl.push(new FormControl(''));
}
```

## 💻 詳細実装例（学習用）
```typescript
protected clearPhones(): void {
  this.phonesCtrl.clear({ emitEvent: false });
  this.phonesCtrl.push(new FormControl('', { validators: [Validators.required] }));
}
```

## ベストプラクティス
- クリア後に必要な初期要素を再追加する
- ユーザーに削除確認を促す
- clearの前後でログや監査情報を残す

## 注意点
- emitEventを抑制するとUI更新ロジックを追加で呼ぶ必要がある
- クリア後にvalueを参照すると空配列になる
- 大量要素のclearはパフォーマンスに注意

## 関連技術
- FormArray.clear
- UX
- イベント制御
