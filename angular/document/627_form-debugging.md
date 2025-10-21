# #627 「フォームのデバッグ方法」

## 概要
フォームデバッグは状態・エラーの可視化、valueChangesの監視、テストによる再現を組み合わせて原因を特定する。

## 学習目標
- フォーム状態を確認する基本手順を知る
- valueChangesログの活用方法を学ぶ
- テストと連携したデバッグ手法を把握する

## 技術ポイント
- console.tableでform.valueやerrorsを確認
- valueChanges/statusChangesを一時的にログ
- テストで異常系入力を再現して検証

## 📺 画面表示用コード（動画用）
```typescript
console.table({
  value: this.form.value,
  errors: this.form.errors,
  status: this.form.status
});
```

## 💻 詳細実装例（学習用）
```typescript
protected debugForm(): void {
  console.table({
    value: this.form.getRawValue(),
    status: this.form.status,
    errors: this.collectErrors(this.form)
  });
}

private collectErrors(group: FormGroup | FormArray): Record<string, unknown> {
  return Object.entries(group.controls).reduce((acc, [key, control]) => {
    if (control instanceof FormGroup || control instanceof FormArray) {
      acc[key] = this.collectErrors(control);
    } else {
      acc[key] = control.errors;
    }
    return acc;
  }, {} as Record<string, unknown>);
}
```

## ベストプラクティス
- デバッグログは開発時のみ有効にする仕組みを用意する
- collectErrorsユーティリティでネスト構造も確認する
- テストケースに再現手順を残す

## 注意点
- 本番でconsoleログが残らないようビルド設定を確認
- ログに個人情報が含まれないようマスク処理を行う
- valueChangesのログは処理負荷に注意

## 関連技術
- console.table
- FormGroup
- ユニットテスト
