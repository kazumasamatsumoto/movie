# #589 「"property" in x」

四国めたん「"property" in x はunknownにプロパティが存在するか判定します」
ずんだもん「in演算子のベーシックな使い方だね」
四国めたん「はい。typeofガードと組み合わせて安全を保証します」
ずんだもん「プロパティがあるとわかったら型アサーションで取り出せるよ」
四国めたん「存在だけでなくundefinedも考慮してロジックを組みましょう」
ずんだもん「境界チェックの基本テクとして覚えておきたいね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: プロパティ存在チェック */
const obj: unknown = { property: "value" };
if (typeof obj === "object" && obj !== null && "property" in obj) {
  console.log((obj as { property: string }).property);
}

/** Example 2: optional対応 */
const maybe: unknown = { property: undefined };
const hasProperty = typeof maybe === "object" && maybe !== null && "property" in maybe;

/** Example 3: 関数化 */
const has = <K extends PropertyKey>(key: K, value: unknown): value is Record<K, unknown> =>
  typeof value === "object" && value !== null && key in value;
```
