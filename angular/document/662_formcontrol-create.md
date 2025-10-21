# #662 「FormControl の作成」

## 概要
FormControlはコンストラクタに初期値・同期バリデーション・非同期バリデーションを渡して生成し、値型を明示すると安全に扱える。

## 学習目標
- FormControlコンストラクタの引数構成を理解する
- 同期と非同期バリデーターの指定方法を学ぶ
- 型パラメータのメリットを把握する

## 技術ポイント
- 第一引数が初期値、第二引数が同期バリデーター
- 第三引数で非同期バリデーターを渡せる
- FormControl<string>のように型注釈を付けられる

## 📺 画面表示用コード（動画用）
```html
<input [formControl]="emailCtrl" type="email" />
```

## 💻 詳細実装例（学習用）
```typescript
protected emailCtrl = new FormControl<string>('', {
  validators: [Validators.required, Validators.email],
  asyncValidators: []
});
```

## ベストプラクティス
- バリデーション配列はモジュール外へ切り出して再利用する
- 非同期バリデーションは必要時のみ設定する
- constructorではなくフィールド初期化でFormControlを生成する

## 注意点
- Validators.emailだけでは完全なRFCチェックにならない
- 非同期バリデーションはサーバーへの呼び出し頻度に注意
- null初期値は型推論を曖昧にする場合がある

## 関連技術
- FormControl
- Validators
- 非同期バリデーション
