# #599 「unknownベストプラクティス」

四国めたん「unknownのベストプラクティスを総チェックしましょう」
ずんだもん「境界でunknown受け取り、ガードとアサーションをルール化するんだよね」
四国めたん「はい。検証ロジックを共通化し、lintとテストで支援します」
ずんだもん「ドキュメント化して合意形成するのも大事だよ」
四国めたん「安全に扱える準備を整えて初めてunknownが真価を発揮します」
ずんだもん「ベストプラクティスを守って型安全な開発を進めよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: ルール定義 */
const policy = {
  entry: "unknown",
  guard: "必須",
  assertion: "根拠付きのみ",
} as const;

/** Example 2: ガード共有 */
export const isRecord = (value: unknown): value is Record<string, unknown> =>
  typeof value === "object" && value !== null;

/** Example 3: lintサポート */
// tsconfig: "noImplicitAny": true
// eslint: "@typescript-eslint/no-unsafe-member-access": "error"
```
