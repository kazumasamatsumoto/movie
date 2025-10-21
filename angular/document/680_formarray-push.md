# #680 「FormArray.push() - 要素追加」

## 概要
FormArray.pushは末尾に新しいコントロールを追加し、動的に入力欄を増やせる。最大数などの制限を設けてUXを保つ。

## 学習目標
- FormArray.pushの使い方を理解する
- 追加時の制約設計を学ぶ
- テンプレートでの表示方法を把握する

## 技術ポイント
- pushはAbstractControlを受け取る
- controls配列に自動的に追加される
- 追加後はvalueChangesが発火する

## 📺 画面表示用コード（動画用）
```typescript
protected addPhone(): void {
  if (this.phonesCtrl.length >= 5) {
    return;
  }
  this.phonesCtrl.push(new FormControl(''));
}
```

## 💻 詳細実装例（学習用）
```typescript
protected phonesCtrl = new FormArray<FormControl<string>>([]);

protected createPhoneControl(): FormControl<string> {
  return new FormControl('', { validators: [Validators.required] });
}

protected addPhone(): void {
  if (this.phonesCtrl.length >= 5) {
    return;
  }
  this.phonesCtrl.push(this.createPhoneControl());
}
```

## ベストプラクティス
- 追加処理は専用メソッドとファクトリで統一する
- 最大数や重複チェックなどのビジネスルールを盛り込む
- 追加後にfocusを移動させるなどUX改善を行う

## 注意点
- push後のvalueChangesが多発する場合はdebounceする
- FormGroup要素を追加する場合は構造を崩さない
- controlsを直接操作して逆順にしないよう注意

## 関連技術
- FormArray.push
- 動的追加
- UX
