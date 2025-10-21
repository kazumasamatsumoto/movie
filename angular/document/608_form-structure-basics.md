# #608 「フォームの基本構造」

## 概要
Angularのフォームはformタグ、入力コントロール、送信ボタン、状態表示UIで構成され、アプローチに関わらず共通の骨組みがある。

## 学習目標
- フォーム画面を構成する要素を整理する
- 状態表示やエラー表示の配置をイメージする
- 設計段階での情報設計の重要性を理解する

## 技術ポイント
- formタグ + コントロール + 送信ボタンが基本
- ngSubmitやsubmitイベントで処理を紐付け
- エラーメッセージやヒントテキストを近接配置

## 📺 画面表示用コード（動画用）
```html
<form (ngSubmit)="onSubmit()">
  <label>
    名前
    <input name="name" ngModel />
  </label>
  <p class="hint">必須項目です</p>
  <button type="submit">送信</button>
</form>
```

## 💻 詳細実装例（学習用）
```typescript
protected onSubmit(): void {
  // TODO: submit logic
}

protected showError(control: NgModel): boolean {
  return control.invalid && control.touched;
}
```

## ベストプラクティス
- フォーム構造をワイヤーフレームで確認してから実装する
- フィールドセットやlegendで関連項目をグルーピングする
- エラーメッセージはフィールドの直下に表示する

## 注意点
- フォーム構造が複雑だとバリデーションロジックも複雑化する
- 送信ボタンをform外に置くとsubmitイベントが発火しない
- 状態表示のUIを後回しにするとUXが低下する

## 関連技術
- ngSubmit
- フォームデザイン
- アクセシビリティ
