# #578 「unknown制限のベストプラクティス」

四国めたん「unknownの制限を味方にするベストプラクティスを整理します」
ずんだもん「まず制限を無視しない仕組みが大事だよね」
四国めたん「はい。スキーマ検証、型ガード、アサーションを適切に組み合わせます」
ずんだもん「監査ログやテストで未知値を覆うのも有効だよ」
四国めたん「制限をドキュメント化して新人にも共有しましょう」
ずんだもん「守れば安全なキャッチオールになるんだね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 制限ルール表現 */
const policy = {
  schema: "必須",
  guard: "標準",
  assertion: "根拠ありのみ",
} as const;

/** Example 2: 監査ログ */
function audit(value: unknown) {
  console.info("audit unknown", value);
}

/** Example 3: テストで保証 */
function ensureString(value: unknown): string | null {
  return typeof value === "string" ? value : null;
}
console.assert(ensureString(1) === null);
```
