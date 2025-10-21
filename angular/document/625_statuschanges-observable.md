# #625 「statusChanges Observable」

## 概要
statusChanges Observableはフォーム状態の遷移をリアルタイムに通知し、非同期バリデーションやUI制御に活用できる。

## 学習目標
- statusChangesが通知するイベントを理解する
- 非同期バリデーション監視への活用方法を学ぶ
- 購読解除のベストプラクティスを把握する

## 技術ポイント
- statusChangesはVALID/INVALID/PENDING/DISABLEDを通知
- FormGroup・FormControlどちらでも利用可能
- takeUntilやAsyncPipeで購読解除を実装

## 📺 画面表示用コード（動画用）
```typescript
this.form.statusChanges
  .pipe(takeUntil(this.destroy$))
  .subscribe(status => this.status = status);
```

## 💻 詳細実装例（学習用）
```typescript
protected ngOnInit(): void {
  this.form.statusChanges
    .pipe(takeUntil(this.destroy$))
    .subscribe(status => {
      this.isPending = status === 'PENDING';
      this.statusLog.push({ status, at: Date.now() });
    });
}

protected trackControlStatus(controlName: string): void {
  this.form.get(controlName)?.statusChanges
    .pipe(takeUntil(this.destroy$))
    .subscribe(status => console.log(controlName, status));
}
```

## ベストプラクティス
- destroy$などで購読解除を徹底する
- 状態ログを蓄積して検証遅延の調査に役立てる
- UIステータス表示をstatusChangesに連動させる

## 注意点
- 購読解除しないとコンポーネント破棄後も通知が続く
- statusChangesは同期処理でも頻繁に発火するためパフォーマンスを監視
- ログに個人情報を含めないよう整形する

## 関連技術
- valueChanges
- AsyncValidator
- RxJS takeUntil
