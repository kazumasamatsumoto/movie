# #293 「nullのJSON表現」

四国めたん「nullのJSON表現について学びましょう!」
ずんだもん「JSONでnullってどう扱われるの?」
四国めたん「はい。nullはJSONの仕様でサポートされているので、そのまま表現できます。」
ずんだもん「undefinedとの違いは?」
四国めたん「重要な違いです。undefinedはJSONで省略されますが、nullは残ります。」
ずんだもん「APIレスポンスの型定義で使い分けるんだね!」
四国めたん「その通りです。JSON互換性が必要な場合はnullを使います。」
ずんだもん「JSON.stringifyとJSON.parseで正しく扱えるのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: nullのJSON表現 */
JSON.stringify({ value: null });
// → '{"value":null}'
JSON.stringify({ a: null, b: undefined });
// → '{"a":null}'

/** Example 2: APIレスポンス型定義 */
interface ApiResponse {
  user: User | null;  // JSON互換
  metadata?: object;  // 省略可能
}

/** Example 3: JSONパース */
const data = JSON.parse('{"name":null}');
// → { name: null }
```
