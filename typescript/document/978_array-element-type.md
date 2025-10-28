# #978 「要素型」

四国めたん「要素型とは配列の中身の型のことです。」
ずんだもん「number[]なら要素型はnumberだね。」
四国めたん「ジェネリクスでT[]ならTが要素型です。」
ずんだもん「型エイリアスにして使い回すと便利だよ。」
四国めたん「要素型を意識して関数の型を設計しましょう。」
ずんだもん「配列操作の基礎になる概念だね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 型エイリアス */
type Element<T> = T extends (infer U)[] ? U : never;

const ids: string[] = [];
type IdElement = Element<typeof ids>; // string

/** Example 2: ジェネリック関数 */
function first<T>(items: T[]): T | undefined {
  return items[0];
}

/** Example 3: 条件型 */
type ValueType = Element<Array<number>>; // number
```
