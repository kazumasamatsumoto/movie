# #569 「配列の並び替え」

## 概要
OrderByPipeでは配列をコピーしてから`sort`を呼び出し、元配列を変更しないようにする。昇順・降順の指定や比較関数のカスタマイズがポイント。

## 学習目標
- 配列をソートするPipeの実装手順を理解する
- 元配列の不変性を保つ理由を学ぶ
- ソート方向やキー指定の方法を把握する

## 技術ポイント
- `const sorted = [...list].sort(compareFn);`
- `direction === 'asc' ? 1 : -1`で昇順/降順を制御
- `localeCompare`で文字列ソートの精度を上げる

## 📺 画面表示用コード（動画用）
```html
<li *ngFor="let user of users | orderBy:'score':'desc'">{{ user.name }}: {{ user.score }}</li>
```

## 💻 詳細実装例（学習用）
```typescript
transform<T>(
  list: readonly T[],
  key: keyof T,
  direction: 'asc' | 'desc' = 'asc'
): T[] {
  if (!Array.isArray(list)) return [];
  return [...list].sort((a, b) => {
    const valueA = a[key];
    const valueB = b[key];
    if (valueA == null || valueB == null) return 0;
    if (typeof valueA === 'string' && typeof valueB === 'string') {
      return direction === 'asc' ? valueA.localeCompare(valueB) : valueB.localeCompare(valueA);
    }
    return direction === 'asc'
      ? (valueA as number) - (valueB as number)
      : (valueB as number) - (valueA as number);
  });
}
```

## ベストプラクティス
- コピーした配列を返し元データを破壊しない
- null/undefinedを含む場合の比較ロジックを明確にする
- ソート条件を引数で指定しテンプレートから制御可能にする

## 注意点
- 大規模配列はPipeでソートするとパフォーマンス低下
- 非純粋Pipeに頼らず、必要ならデータ取得時にソート
- 文字列は`localeCompare`で国際化に対応

## 関連技術
- OrderByPipe
- Array.sort
- Intl.Collator / localeCompare
