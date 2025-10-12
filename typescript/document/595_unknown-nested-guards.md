# #595 「ネストした型ガード」

四国めたん「ネストした型ガードで深い構造のunknownを安全に扱いましょう」
ずんだもん「親オブジェクトを確認してから子プロパティを検証するんだね」
四国めたん「はい。段階的に安全性を証明するのがコツです」
ずんだもん「ヘルパーを分割すれば読みやすさも上がるよ」
四国めたん「ネスト構造を扱うときは戻り値の型述語を活用しましょう」
ずんだもん「複雑なJSONも怖くなくなるね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: トップレベル判定 */
function isObject(value: unknown): value is Record<string, unknown> {
  return typeof value === "object" && value !== null;
}

/** Example 2: ネスト判定 */
function hasProfile(value: unknown): value is { profile: { name: string } } {
  return isObject(value)
    && "profile" in value
    && isObject((value as Record<string, unknown>).profile)
    && "name" in (value as { profile: Record<string, unknown> }).profile
    && typeof (value as { profile: { name: unknown } }).profile.name === "string";
}

/** Example 3: 利用例 */
const payload: unknown = { profile: { name: "Choco" } };
if (hasProfile(payload)) console.log(payload.profile.name);
```
