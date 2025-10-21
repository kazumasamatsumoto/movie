# #682 「FormArray.at() - 要素取得」

## 概要
FormArray.at(index)は指定インデックスのコントロールを返し、ジェネリクスで型を指定しておくと安全に操作できる。

## 学習目標
- FormArray.atの使い方を理解する
- 型安全なアクセス方法を学ぶ
- 取得したコントロールの操作方法を把握する

## 技術ポイント
- atはAbstractControlを返すので型注釈が重要
- ジェネリクス指定で戻り値の型が推論される
- 値の読み書きは取得したコントロールで行う

## 📺 画面表示用コード（動画用）
```typescript
const first = this.phonesCtrl.at(0) as FormControl<string>;
first.setValue('090-0000-0000');
```

## 💻 詳細実装例（学習用）
```typescript
protected updateFirstPhone(): void {
  const control = this.phonesCtrl.at(0);
  if (control instanceof FormControl) {
    control.setValue('090-0000-0000');
  }
}
```

## ベストプラクティス
- フォーム生成時にジェネリクスで型を固定する
- atの戻り値はinstanceofで確認して操作する
- ユーティリティメソッドで要素アクセス処理を統一する

## 注意点
- インデックス範囲外の場合はundefinedを返す
- 型を決めておかないとany扱いになる
- 取得後にコントロールを置き換えると参照がずれることがある

## 関連技術
- FormArray.at
- 型安全性
- コントロール操作
