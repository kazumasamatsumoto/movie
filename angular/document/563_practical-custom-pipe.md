# #563 「実用的なカスタム Pipe」

## 概要
実用的なカスタムPipeは文字列の省略、配列のフィルタやソートなどビューで頻出の整形をまとめ、テンプレートを簡潔に保つ。

## 学習目標
- 実用的なカスタムPipeの例を理解する
- Pipe化することで再利用性が高まることを学ぶ
- Pipeを導入する際の設計ポイントを把握する

## 技術ポイント
- TruncatePipe、FilterPipe、OrderByPipeなど
- transform内で純粋な処理を実装
- 引数で設定を柔軟に受け取る

## 📺 画面表示用コード（動画用）
```html
<p>{{ description | truncate:80:'…' }}</p>
<li *ngFor="let item of items | orderBy:'name'">{{ item.name }}</li>
```

## 💻 詳細実装例（学習用）
```typescript
@Pipe({ name: 'truncate', standalone: true })
export class TruncatePipe implements PipeTransform {
  transform(value: string, limit = 20, suffix = '...'): string {
    if (!value || value.length <= limit) return value;
    return `${value.slice(0, limit)}${suffix}`;
  }
}
```

## ベストプラクティス
- 重い処理は避け、純粋Pipeで軽量に実装
- テンプレートの可読性向上を目的にPipe化
- ドキュメントやspecでPipeの挙動を明記

## 注意点
- 配列操作は大量データで性能へ影響するため慎重に
- 非純粋Pipeはパフォーマンスリスクが高い
- 変換ロジックが複雑になりすぎないようにする

## 関連技術
- Pure/Impure Pipe
- カスタムPipeテスト
- 再利用可能なユーティリティ関数
