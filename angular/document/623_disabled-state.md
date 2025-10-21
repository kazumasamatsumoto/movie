# #623 「disabled - 無効化状態」

## 概要
disabled状態はコントロールを操作不能にし、フォーム値やバリデーションからも除外されるため、条件付き入力やステップフォームで重要になる。

## 学習目標
- disabledの動作を理解する
- フォーム値への影響を把握する
- 有効化・無効化の切り替え方法を学ぶ

## 技術ポイント
- disabledなコントロールはフォーム値に含まれない
- FormControl.disable() / enable()で動的切り替え
- テンプレートでは[disabled]バインディングで制御

## 📺 画面表示用コード（動画用）
```typescript
this.form.get('email')?.disable();
```

## 💻 詳細実装例（学習用）
```typescript
protected toggleNewsletter(enabled: boolean): void {
  const control = this.form.get('newsletter');
  if (!control) {
    return;
  }
  enabled ? control.enable() : control.disable();
}

protected formValue(): unknown {
  return this.form.getRawValue();
}
```

## ベストプラクティス
- 業務ルールに合わせてdisable/enableを明示的に管理する
- disabled時の見た目や説明テキストを用意する
- getRawValueを使ってdisabled項目も含めた値を取得する

## 注意点
- disableすると値がフォーム値から除外されることを忘れない
- テンプレートでdisabled属性と[disabled]を併用すると競合する
- アクセシビリティのためにaria-disabledも検討する

## 関連技術
- FormControl.disable
- getRawValue
- UXメッセージ
