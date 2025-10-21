# #544 「name プロパティ」

## 概要
Pipeデコレータの`name`プロパティはテンプレートで使用する識別子を指定し、`{{ value | pipeName }}`という構文で参照される。

## 学習目標
- nameプロパティの役割を理解する
- 命名規約と衝突回避のポイントを学ぶ
- nameを変更するとテンプレート側への影響があることを把握する

## 技術ポイント
- `@Pipe({ name: 'truncate' })`
- 小文字＋単語区切りをハイフンにするなど規約を統一
- 名前変更時はテンプレートも更新

## 📺 画面表示用コード（動画用）
```typescript
@Pipe({ name: 'truncate', standalone: true })
export class TruncatePipe implements PipeTransform { ... }
```

## 💻 詳細実装例（学習用）
```typescript
@Pipe({
  name: 'slugify',
  standalone: true
})
export class SlugifyPipe implements PipeTransform {
  transform(value: string): string {
    return value.trim().toLowerCase().replace(/\s+/g, '-');
  }
}
```

## ベストプラクティス
- nameは機能が伝わる短い名前にする
- ライブラリではプレフィックスを付けて衝突を防ぐ
- 名前を変える場合は破壊的変更として扱いドキュメントを更新

## 注意点
- 名前の重複はビルドエラーになる
- テンプレート内のPipe参照名と一致していないと機能しない
- 名前に大文字を使うとテンプレートで扱いにくい

## 関連技術
- @Pipeデコレータ
- 名前付きエクスポート
- テンプレートバインディング
