# #547 「引数の受け取り」

## 概要
Pipeの`transform`メソッドは追加引数を受け取り、テンプレートから`| pipe:arg1:arg2`の形式で渡された値を処理に利用できる。

## 学習目標
- Pipeで追加引数を扱う方法を理解する
- 引数の順序とデフォルト値の設定方法を学ぶ
- 引数を型安全に扱うための工夫を把握する

## 技術ポイント
- `transform(value: string, limit: number, suffix = '...')`
- Restパラメータで可変長引数に対応
- テンプレートではコロン区切りで渡す

## 📺 画面表示用コード（動画用）
```html
<p>{{ comment | truncate:50:'…' }}</p>
```

## 💻 詳細実装例（学習用）
```typescript
transform(value: string, limit = 20, suffix = '...'): string {
  if (!value || value.length <= limit) return value;
  return `${value.substring(0, limit)}${suffix}`;
}
```

## ベストプラクティス
- 引数にはデフォルト値を設定し使いやすくする
- 引数の意味が分かるようJSDocやドキュメントで説明
- 引数が多い場合はオブジェクトで受け取るカスタムPipeを検討

## 注意点
- テンプレート側で配列やオブジェクトを引数にすると参照が毎回変わり純粋Pipeで再評価される
- 型注釈を付けて可読性と安全性を高める
- 引数の順序を変えるとテンプレートも更新が必要

## 関連技術
- PipeTransform
- Restパラメータ
- カスタムPipe設計
