# #639 「ミス防止ベストプラクティス」

四国めたん「unknownの扱いミスを防ぐベストプラクティスをまとめます」
ずんだもん「共通ガード、Lint、ユニットテスト、この三枚看板だね」
四国めたん「はい。コードレビューでガード忘れをチェックする運用も重要です」
ずんだもん「型安全なラッパーを共有すれば再発率が下がるよ」
四国めたん「ドキュメントと教育で文化として定着させましょう」
ずんだもん「仕組みでミスを抑えてunknownを信頼しよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 共通ガード */
export const isRecord = (value: unknown): value is Record<string, unknown> =>
  typeof value === "object" && value !== null;

/** Example 2: Lint設定 */
// "@typescript-eslint/no-unsafe-member-access": "error"
// "@typescript-eslint/no-unsafe-call": "error"

/** Example 3: ユニットテスト */
test("guard protects payload", () => {
  expect(isRecord({ id: 1 })).toBe(true);
  expect(isRecord(null)).toBe(false);
});
```
