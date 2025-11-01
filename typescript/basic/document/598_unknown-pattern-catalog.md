# #598 「unknownハンドリングパターン集」

四国めたん「unknownを扱うパターン集を整理しましょう」
ずんだもん「typeof、instanceof、in、Array.isArrayの組み合わせだね」
四国めたん「はい。用途ごとにテンプレート化しておくと迷いません」
ずんだもん「ベースにカスタムガードを用意すれば拡張も楽だよ」
四国めたん「パターン集をドキュメント化して共有しましょう」
ずんだもん「未知の値も即座にさばけるようになるね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: typeofテンプレート */
const asString = (value: unknown): string | null =>
  typeof value === "string" ? value : null;

/** Example 2: instanceofテンプレート */
const asError = (value: unknown): Error | null =>
  value instanceof Error ? value : null;

/** Example 3: inテンプレート */
const asRecordWithId = (value: unknown): { id: number } | null =>
  typeof value === "object"
    && value !== null
    && "id" in value
    && typeof (value as Record<string, unknown>).id === "number"
    ? { id: (value as Record<string, unknown>).id as number }
    : null;
```
