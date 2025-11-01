# #552 「unknownは型安全なany」

四国めたん「unknownは型安全なanyとして位置づけられています」
ずんだもん「anyと同じで何でも入るのに、どうして安全なの？」
四国めたん「直接操作できない制約があるので、型チェックを通して安全に扱えます」
ずんだもん「つまりコンパイルが危険な使い方を止めてくれるんだね」
四国めたん「はい。トップ型としての柔軟さと静的保証のバランスが魅力です」
ずんだもん「APIレスポンスをまずunknownで受け取るのが実践的だよ」

---

## 📺 画面表示用コード

```typescript
/** Example 1: anyとの違いを比較 */
let unsafe: any = JSON.parse("{\"id\":1}");
unsafe.nonExist.toString(); // ランタイムで落ちる
let safe: unknown = JSON.parse("{\"id\":1}");
// safe.nonExist; // ❌ コンパイルエラー

/** Example 2: unknownを受けるユーティリティ */
function handlePayload(payload: unknown) {
  if (typeof payload === "string") {
    return payload.trim();
  }
  return payload;
}

/** Example 3: try-catchでunknown */
try {
  throw new Error("network");
} catch (error: unknown) {
  if (error instanceof Error) console.error(error.message);
}
```
