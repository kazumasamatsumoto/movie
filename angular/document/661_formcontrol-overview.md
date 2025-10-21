# #661 「FormControl - 単一コントロール」

## 概要
FormControlはReactive Formsで単一の入力値とそのバリデーション状態を管理する基礎クラスで、テンプレートと同期させて利用する。

## 学習目標
- FormControlの役割と基本APIを理解する
- テンプレートとFormControlを紐付ける方法を学ぶ
- 値と状態をコードから確認する手順を掴む

## 技術ポイント
- FormControlは値・status・errorsを保持する
- [formControl]ディレクティブでテンプレートと同期
- ReactiveFormsModuleのインポートが必須

## 📺 画面表示用コード（動画用）
```html
<input [formControl]="nameCtrl" placeholder="名前を入力" />
```

## 💻 詳細実装例（学習用）
```typescript
protected nameCtrl = new FormControl('');

protected logStatus(): void {
  console.log(this.nameCtrl.value, this.nameCtrl.status);
}
```

## ベストプラクティス
- 初期化時に型パラメータを指定して補完を効かせる
- 状態プロパティ(valid・invalidなど)をログして挙動を把握する
- フォーム用のプロパティはコンポーネントクラスにまとめる

## 注意点
- ReactiveFormsModuleを読み込まないとディレクティブが動作しない
- テンプレートからvalueを直接書き換えてもFormControlは更新されない
- 同じFormControlインスタンスを複数要素で共有しない

## 関連技術
- FormControl
- ReactiveFormsModule
- 状態管理
