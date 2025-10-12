# #619 「外部ライブラリとの境界」

四国めたん「型定義が不完全な外部ライブラリはunknownで受け止めましょう」
ずんだもん「anyのまま渡されるケースも多いから危ないんだよね」
四国めたん「はい。ラップして型ガードやスキーマで検証します」
ずんだもん「safeWrapperを用意すれば安全に使い回せるよ」
四国めたん「外部境界をunknownに揃えるとバグの侵入を防げます」
ずんだもん「ライブラリ更新にも強い設計になるね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: ライブラリ呼び出し */
declare function legacySdk(method: string): any;
const rawResult: unknown = legacySdk("getUser");

/** Example 2: 包装関数 */
function callSafe(method: string): unknown {
  return legacySdk(method);
}

/** Example 3: 型ガード */
const isUser = (value: unknown): value is { id: number } =>
  typeof value === "object" && value !== null && "id" in value;
```
