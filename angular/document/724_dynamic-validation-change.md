# #724 「動的バリデーション変更」

## 概要
動的バリデーション変更はフォームの状態やユーザー入力に応じてsetValidators/clearValidatorsを切り替え、updateValueAndValidityで反映させる。

## 学習目標
- 動的バリデーション切り替えの流れを理解する
- 実装時のログ・デバッグ方法を学ぶ
- 複数状態の組み合わせを整理する

## 技術ポイント
- 状態変化をvalueChangesで監視
- setValidators/clearValidatorsでルールを更新
- updateValueAndValidityで再評価する

## 📺 画面表示用コード（動画用）
```typescript
protected toggleCompanyFields(required: boolean): void {
  if (required) {
    this.companyCtrl.setValidators([Validators.required]);
  } else {
    this.companyCtrl.clearValidators();
  }
  this.companyCtrl.updateValueAndValidity();
}
```

## 💻 詳細実装例（学習用）
```typescript
protected companyCtrl = new FormControl('');
protected isBusinessCtrl = new FormControl(false);

protected constructor() {
  this.isBusinessCtrl.valueChanges
    .pipe(takeUntilDestroyed())
    .subscribe(required => this.toggleCompanyFields(!!required));
}

private toggleCompanyFields(required: boolean): void {
  if (required) {
    this.companyCtrl.setValidators([Validators.required]);
  } else {
    this.companyCtrl.clearValidators();
  }
  this.companyCtrl.updateValueAndValidity();
}
```

## ベストプラクティス
- バリデーション切り替えは専用メソッドで一元管理する
- 状態の組み合わせを列挙してテストケースを作成する
- ログを仕込んでデバッグしやすくする

## 注意点
- 複数条件が同時に変更される場合は順序を決める
- updateValueAndValidityを呼ばないとエラー状態が更新されない
- UIが必須表示に追従するようテンプレートも更新する

## 関連技術
- setValidators
- clearValidators
- updateValueAndValidity
