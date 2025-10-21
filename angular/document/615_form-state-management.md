# #615 「フォームの状態管理」

## 概要
フォーム状態管理は視覚的なフィードバック、バリデーション、外部ストア連携を含めた総合的なUX設計であり、Angularが提供する状態フラグとObservableを活用する。

## 学習目標
- フォーム状態フラグの役割を理解する
- statusChangesやvalueChangesの活用方法を学ぶ
- 外部状態管理との連携イメージを掴む

## 技術ポイント
- pristine/dirtyで変更有無を判定
- touched/untouchedでフォーカス履歴を把握
- statusChangesでvalid/pendingの変化を購読

## 📺 画面表示用コード（動画用）
```typescript
this.form.statusChanges
  .subscribe(status => console.log(status));
```

## 💻 詳細実装例（学習用）
```typescript
protected ngOnInit(): void {
  this.form.statusChanges.subscribe(status => {
    this.isValid = status === 'VALID';
  });
  this.form.valueChanges.subscribe(value => {
    this.store.dispatch(formValueChanged({ value }));
  });
}

protected get cssClass(): Record<string, boolean> {
  const control = this.form.get('email');
  return {
    'is-invalid': !!control && control.invalid && control.touched,
    'is-valid': !!control && control.valid && control.touched
  };
}
```

## ベストプラクティス
- フォーム状態フラグをUIクラスに紐付け視覚的に示す
- statusChangesとvalueChangesを購読するときはtakeUntilで解除する
- 外部ストア連携は双方向同期のルールを決めておく

## 注意点
- 購読を解除しないとメモリリークになる
- 状態フラグの意味を誤解するとN件エラーが非表示になる
- 複雑な状態制御はサービス層に切り出してテストする

## 関連技術
- statusChanges
- valueChanges
- NgRx
