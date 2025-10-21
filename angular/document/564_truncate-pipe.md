# #564 「Truncate Pipe - 文字列切り詰め」

## 概要
TruncatePipeは文字列が一定の長さを超えた場合に切り詰めて末尾にサフィックスを付与し、一覧やカードUIでの長文表示を整える。

## 学習目標
- TruncatePipeの用途と実装方法を理解する
- transformで文字列長を判定し省略するロジックを学ぶ
- 引数で長さやサフィックスを指定する方法を把握する

## 技術ポイント
- `transform(value: string, limit = 20, suffix = '...')`
- `value.length <= limit`ならそのまま返す
- `substring`や`slice`で文字列を切り出す

## 📺 画面表示用コード（動画用）
```html
<p>{{ article.summary | truncate:80:'…' }}</p>
```

## 💻 詳細実装例（学習用）
```typescript
@Pipe({
  name: 'truncate',
  standalone: true
})
export class TruncatePipe implements PipeTransform {
  transform(value: string, limit = 20, suffix = '...'): string {
    if (!value || value.length <= limit) return value;
    return `${value.slice(0, limit)}${suffix}`;
  }
}
```

## ベストプラクティス
- デフォルト値を設定しテンプレートで簡潔に利用
- サフィックスに`…`や`...`を渡せるよう引数を受け取る
- HTMLタグを含む文字列は別途サニタイズ処理を検討

## 注意点
- 多バイト文字（絵文字など）のカウントに注意（`Array.from(value)`で対処可能）
- null/undefinedの場合は空文字を返す
- 長さ判定に正規化が必要なケースは事前処理を行う

## 関連技術
- PipeTransform
- 文字列操作ユーティリティ
- UIレイアウト最適化
