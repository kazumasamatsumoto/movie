# #723 「条件付きバリデーション」

## 概要
条件付きバリデーションはsetValidators/clearValidatorsで動的にルールを切り替え、updateValueAndValidityで状態を再評価する。

## 学習目標
- 条件付きバリデーションの実装手順を理解する
- バリデーター切り替え後の再評価方法を学ぶ
- valueChangesとの連携を把握する

## 技術ポイント
- setValidatorsで新しいバリデーターを設定
- clearValidatorsでルールを解除
- updateValueAndValidityで再評価

## 📺 画面表示用コード（動画用）
```typescript
this.newsletterCtrl.valueChanges
  .subscribe(enabled => {
    if (enabled) {
      this.emailCtrl.setValidators([Validators.required, Validators.email]);
    } else {
      this.emailCtrl.clearValidators();
    }
    this.emailCtrl.updateValueAndValidity();
  });
```

## 💻 詳細実装例（学習用）
```typescript
protected newsletterCtrl = new FormControl(false);
protected emailCtrl = new FormControl('');

protected constructor() {
  this.newsletterCtrl.valueChanges
    .pipe(takeUntilDestroyed())
    .subscribe(enabled => {
      if (enabled) {
        this.emailCtrl.setValidators([Validators.required, Validators.email]);
      } else {
        this.emailCtrl.clearValidators();
      }
      this.emailCtrl.updateValueAndValidity();
    });
}
```

## ベストプラクティス
- 条件切り替えは専用メソッドにまとめてテスト可能にする
- UIで必須化されたことを明示する表示を追加する
- フォーム送信時にも最終的な状態を再評価する

## 注意点
- setValidators後にupdateValueAndValidityを忘れない
- 複数条件が競合する場合はルールを整理する
- clearValidatorsでバリデーション解除した後はエラーメッセージも消す

## 関連技術
- setValidators
- clearValidators
- 動的フォーム
