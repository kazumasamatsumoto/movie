# #984 「mapの型」

四国めたん「mapメソッドは戻り値の配列型がコールバックの戻り値型になります。」
ずんだもん「number[]からstring[]に変換するのも簡単だね。」
四国めたん「はい、ジェネリック定義は<U>(callback: (value: T, index: number, array: T[]) => U) => U[]です。」
ずんだもん「コールバックの戻り値に注意すれば意図した型が得られるよ。」
四国めたん「mapの型を理解して型安全な変換を行いましょう。」
ずんだもん「transform処理の基礎だね！」

---

## 📺 画面表示用コード

```typescript
const numbers = [1, 2, 3];

/** Example 1: 変換 */
const strings = numbers.map((n) => n.toString()); // string[]

/** Example 2: Union */
const mixed = numbers.map((n) => (n % 2 ? n : n.toString())); // (string | number)[]

/** Example 3: map型 */
function mapTyped<T, U>(items: T[], mapper: (value: T, index: number, array: T[]) => U): U[] {
  return items.map(mapper);
}
```
