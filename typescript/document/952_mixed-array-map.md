# #952 「map操作」

四国めたん「混合型配列でmapを使うと戻り値の型が重要になります。」
ずんだもん「コールバックの結果型がそのまま新しい配列の型になるんだね。」
四国めたん「はい、型を絞りたいときは型ガードを噛ませたり、map後にfilterで整形します。」
ずんだもん「map内でUnionを適切に処理しよう。」
四国めたん「TypeScriptは戻り値のUnionを推論してくれるので、期待する型を設計しましょう。」
ずんだもん「map操作でも型安全を保ってね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: そのままUnion */
const mixed: (string | number)[] = ["ok", 200];
const lengths = mixed.map((item) =>
  typeof item === "string" ? item.length : item.toString().length
); // number[]

/** Example 2: 変換 */
const normalized = mixed.map((item): string => item.toString()); // string[]

/** Example 3: map + filter */
const numbers = mixed.map((item) => (typeof item === "number" ? item : undefined))
  .filter((item): item is number => item !== undefined);
```
