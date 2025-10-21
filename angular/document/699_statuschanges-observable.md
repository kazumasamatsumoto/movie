# #699 「statusChanges Observable」

## 概要
statusChangesはフォームやコントロールの状態変化(VALID/INVALID/PENDING/DISABLED)を通知するObservableで、非同期バリデーションの進行表示などに活用できる。

## 学習目標
- statusChangesの通知内容を理解する
- 非同期バリデーションとの連携方法を学ぶ
- フォーム全体の状態監視を把握する

## 技術ポイント
- statusChangesは状態文字列を通知
- FormGroup/FormArrayでも購読可能
- PENDING状態を利用してローディングUIを制御

## 📺 画面表示用コード（動画用）
```typescript
this.emailCtrl.statusChanges
  .pipe(takeUntilDestroyed())
  .subscribe(status => this.isChecking = status === 'PENDING');
```

## 💻 詳細実装例（学習用）
```typescript
protected emailCtrl = new FormControl('', {
  asyncValidators: [this.emailUniqueValidator]
});

protected constructor() {
  this.emailCtrl.statusChanges
    .pipe(takeUntilDestroyed())
    .subscribe(status => {
      this.isChecking = status === 'PENDING';
    });
}
```

## ベストプラクティス
- statusChangesでローディング表示を制御する
- フォーム全体のstatusChangesを使って送信可否を制御
- 購読処理はサービスに委譲しテストしやすくする

## 注意点
- statusChangesは頻繁に発火するため不要な処理を避ける
- PENDING状態が長い場合はタイムアウトやキャンセルを検討する
- 購読解除を忘れるとメモリリークを招く

## 関連技術
- statusChanges
- 非同期バリデーション
- ローディングUI
