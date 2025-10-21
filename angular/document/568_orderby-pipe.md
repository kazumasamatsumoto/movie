# #568 「OrderBy Pipe - ソート」

## 概要
OrderByPipeは配列を指定キーや比較関数でソートするカスタムPipeで、テンプレートから並び順を切り替えられる。元配列を変更しないようコピーしてからソートする。

## 学習目標
- OrderByPipeの実装方法を理解する
- ソート対象と順序を引数で設定する仕組みを学ぶ
- 元配列の不変性を保つ工夫を把握する

## 技術ポイント
- `transform(list: T[], key: keyof T, direction: 'asc' | 'desc' = 'asc')`
- `[...list].sort(...)`でコピーしてソート
- 比較関数を引数で受け取る設計も可能

## 📺 画面表示用コード（動画用）
```html
<li *ngFor="let user of users | orderBy:'name':'asc'">{{ user.name }}</li>
```

## 💻 詳細実装例（学習用）
```typescript
@Pipe({ name: 'orderBy', standalone: true })
export class OrderByPipe implements PipeTransform {
  transform<T>(list: readonly T[], key: keyof T, direction: 'asc' | 'desc' = 'asc'): T[] {
    if (!Array.isArray(list)) return [];
    const sorted = [...list].sort((a, b) => {
      const valueA = a[key]!;
      const valueB = b[key]!;
      if (valueA < valueB) return direction === 'asc' ? -1 : 1;
      if (valueA > valueB) return direction === 'asc' ? 1 : -1;
      return 0;
    });
    return sorted;
  }
}
```

## ベストプラクティス
- 元配列を変更せずコピーしてソート
- 比較対象にnullが含まれる場合の処理を定義
- ソート条件を定数化しテンプレートで読みやすくする

## 注意点
- 配列サイズが大きいと毎回ソートが高コスト
- 非純粋Pipeにすると全変更検知でソートされるため性能に注意
- 文字列比較はロケールを考慮した`localeCompare`の使用も検討

## 関連技術
- Array.prototype.sort
- Pure/Impure Pipe
- Intl.Collator
