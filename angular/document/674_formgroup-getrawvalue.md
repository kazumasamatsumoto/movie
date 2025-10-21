# #674 「FormGroup.getRawValue() メソッド」

## 概要
FormGroup.getRawValue()はdisabledなコントロールも含めて値を取得でき、valueでは省かれる項目も確実に含まれる。

## 学習目標
- getRawValueの用途を理解する
- valueとの違いを整理する
- DTO変換時にdisabled値が必要なケースを把握する

## 技術ポイント
- disabledなコントロールも値に含まれる
- return型は全コントロールが必須になる
- フォーム送信時の値整形に役立つ

## 📺 画面表示用コード（動画用）
```typescript
protected submit(): void {
  const payload = this.profileGroup.getRawValue();
  console.log(payload);
}
```

## 💻 詳細実装例（学習用）
```typescript
protected profileGroup = new FormGroup({
  name: new FormControl('', { nonNullable: true }),
  email: new FormControl('', { nonNullable: true }),
  id: new FormControl({ value: 'readonly-id', disabled: true })
});

protected buildPayload() {
  return this.profileGroup.getRawValue();
}
```

## ベストプラクティス
- 送信前にgetRawValueでpayloadを生成する
- disabledでも必要な値は別途整形する
- FormBuilderを使う場合もgetRawValueは同様に使える

## 注意点
- disabledコントロールがnullを返す可能性を考慮
- getRawValueは型が非nullableになるので変換を忘れない
- valueChangesとは異なりemitEventオプションは無い

## 関連技術
- getRawValue
- disabledコントロール
- payload整形
