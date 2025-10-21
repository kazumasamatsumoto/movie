# #675 「FormGroup.setValue() - 全項目設定」

## 概要
FormGroup.setValueは定義された全コントロールに対応する値を要求し、欠けていると例外になる。emitEventなどのオプションで通知制御が可能。

## 学習目標
- FormGroup.setValueの挙動を理解する
- 完全なDTOを渡す場面を把握する
- emitEvent/onlySelfオプションの扱いを学ぶ

## 技術ポイント
- 全てのキーを含むオブジェクトが必要
- emitEvent:falseでvalueChanges通知を抑制
- onlySelf:trueで親グループへの通知を止められる

## 📺 画面表示用コード（動画用）
```typescript
this.profileGroup.setValue({
  name: 'Alice',
  email: 'alice@example.com',
  id: 'readonly-id'
});
```

## 💻 詳細実装例（学習用）
```typescript
protected profileGroup = new FormGroup({
  name: new FormControl('', { nonNullable: true }),
  email: new FormControl('', { nonNullable: true }),
  id: new FormControl('', { nonNullable: true })
});

protected applyProfile(profile: { name: string; email: string; id: string }): void {
  this.profileGroup.setValue(profile, { emitEvent: false });
}
```

## ベストプラクティス
- 完全なDTOを扱う箇所でsetValueを使う
- オプション引数の設定は共通化してミスを減らす
- 型を合わせるためにDTOインターフェースを定義する

## 注意点
- キーが欠けると例外が発生する
- 余分なキーを渡してもエラーになる
- emitEvent:falseにするとUI側の同期を忘れがちになる

## 関連技術
- setValue
- DTO適用
- 通知制御
