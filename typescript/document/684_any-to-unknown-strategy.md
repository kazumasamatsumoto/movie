# #684 「anyからunknownへ置き換え」

四国めたん「any排除の基本はunknownへ置き換えて型ガードを追加することです」
ずんだもん「コンパイルエラーが教えてくれるからガード漏れに気付けるよね」
四国めたん「はい。まず静的境界でunknownに変えてから安全な型へ絞ります」
ずんだもん「既存コードも最小限の変更で効果が出るのが嬉しい」
四国めたん「unknown化は段階的排除の最初のステップとして最適です」
ずんだもん「すぐに試して安全なコードに近づけよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: any → unknown */
function handle(payload: any) {
  const safe: unknown = payload;
  if (typeof safe === "object" && safe !== null) {
    return safe;
  }
  throw new TypeError("invalid payload");
}

/** Example 2: コンパイルエラーで検知 */
const legacy: unknown = JSON.parse("{}");
// legacy.id; // ❌

/** Example 3: ガード関数 */
const hasId = (value: unknown): value is { id: number } =>
  typeof value === "object" && value !== null && "id" in value;
```
