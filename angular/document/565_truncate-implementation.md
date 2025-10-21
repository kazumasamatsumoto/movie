# #565 「指定文字数で省略」

## 概要
TruncatePipeでは指定文字数を超えた場合のみ文字列を切り詰め、先頭からlimit文字まで取り出してサフィックスを追加する。デフォルト値を用意すると使いやすい。

## 学習目標
- 指定文字数で文字列を省略する実装を理解する
- `substring`や`slice`を使った切り詰め処理を学ぶ
- null/undefinedなど非文字列入力への対応を把握する

## 技術ポイント
- `if (!value || value.length <= limit) return value;`
- `value.slice(0, limit)`で文字列を切り出す
- サフィックスは可変引数で受け取り柔軟に

## 📺 画面表示用コード（動画用）
```html
<p>{{ product.description | truncate:40:'…' }}</p>
```

## 💻 詳細実装例（学習用）
```typescript
transform(value: string, limit = 20, suffix = '...'): string {
  if (!value || value.length <= limit) {
    return value;
  }
  return `${value.slice(0, limit)}${suffix}`;
}
```

## ベストプラクティス
- limitとsuffixにデフォルト値を設定しテンプレートで簡潔に利用できるようにする
- 多言語対応ではサフィックスを翻訳で切り替える
- 処理が軽量のためPurePipeのままで十分

## 注意点
- 文字列以外の値が渡された場合の処理を定義（型チェックや例外）
- 複数バイト文字の扱いに注意（必要なら`Array.from`でカウント）
- HTMLを含む文字列はタグを破壊する可能性があるため注意

## 関連技術
- PipeTransform
- 文字列操作ユーティリティ
- Pure Pipe
