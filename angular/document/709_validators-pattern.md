# #709 「Validators.pattern() - 正規表現」

## 概要
Validators.patternは正規表現と一致しない場合にエラーを返し、requiredPatternとactualValueをエラー情報として提供する。

## 学習目標
- patternバリデーションの仕組みを理解する
- 正規表現の指定方法を学ぶ
- エラーメッセージへの反映方法を把握する

## 技術ポイント
- RegExpまたは文字列でパターンを指定できる
- errors.pattern.requiredPatternとactualValueが利用可能
- requiredと併用して空文字入力を防ぐ

## 📺 画面表示用コード（動画用）
```html
<input [formControl]="zipCtrl" />
<span *ngIf="zipCtrl.errors?.pattern">123-4567形式で入力してください</span>
```

## 💻 詳細実装例（学習用）
```typescript
protected zipCtrl = new FormControl('', [
  Validators.required,
  Validators.pattern(/^[0-9]{3}-[0-9]{4}$/)
]);
```

## ベストプラクティス
- 正規表現は定数化してテストにも流用する
- ユーザーに例を示して入力ミスを減らす
- 必要ならmaskコンポーネントなど入力補助を用意する

## 注意点
- 正規表現は読みづらいのでコメントで意図を残す
- localeによって許容文字が異なるケースを考慮する
- パターン変更は影響範囲が広いのでレビューを徹底する

## 関連技術
- Validators.pattern
- 正規表現
- 入力補助
