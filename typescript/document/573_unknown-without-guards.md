# #573 「型ガードなしの危険」

四国めたん「unknownを型ガードなしで扱うとコンパイルが止まります」
ずんだもん「それでもanyに変えたくなるのが危ないんだよね」
四国めたん「型安全性を捨てないように、ガードを追加して解決しましょう」
ずんだもん「ユーティリティを共有しておけば楽に書けるよ」
四国めたん「ガードなしで突き進むのはNGと覚えてください」
ずんだもん「規律を守って安全なコードを維持しよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: ガードなしはエラー */
const raw: unknown = fetchData();
// raw.value; // ❌

/** Example 2: 代わりにガード */
if (typeof raw === "object" && raw !== null && "value" in raw) {
  console.log((raw as { value: number }).value);
}

/** Example 3: ガードを共有 */
const hasValue = (input: unknown): input is { value: number } =>
  typeof input === "object" && input !== null && "value" in input;
```
