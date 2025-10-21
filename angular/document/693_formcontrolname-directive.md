# #693 「formControlName ディレクティブ」

## 概要
formControlNameディレクティブはFormGroup内のコントロールをテンプレートのフォーム要素に紐付け、値と状態を同期させる。

## 学習目標
- formControlNameの役割を理解する
- キー名とコントロールのマッピング方法を把握する
- エラーステートの取得方法を学ぶ

## 技術ポイント
- キー名はFormGroup定義と一致させる
- formControlNameはinput/select/textareaなどに適用可能
- テンプレートからcontrolプロパティへアクセスできる

## 📺 画面表示用コード（動画用）
```html
<input formControlName="email" type="email" />
<span *ngIf="profileForm.get('email')?.invalid">形式が正しくありません</span>
```

## 💻 詳細実装例（学習用）
```typescript
protected profileForm = new FormGroup({
  email: new FormControl('', { validators: [Validators.email] })
});
```

## ベストプラクティス
- キー名は定数化してタイポを防ぐ
- getメソッドでコントロールを取得しテンプレートに渡す
- エラーメッセージは共通コンポーネントにまとめる

## 注意点
- FormGroupに存在しないキーを指定すると例外になる
- フォーム生成前にテンプレートが描画されるとnullアクセスになる
- 属性とバインディングを混在させると警告が出る場合がある

## 関連技術
- formControlName
- エラー表示
- Reactive Formsテンプレート
