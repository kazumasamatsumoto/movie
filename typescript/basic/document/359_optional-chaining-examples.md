# #359 「?.の使用例」

四国めたん「?. の具体的な使用例を押さえましょう!」
ずんだもん「APIレスポンスのdata?.name ?? 'Unknown' が書きやすいね!」
四国めたん「そうです。avatarのようなネストにも届きます。」
ずんだもん「DOMイベントでも element?.addEventListener で安全?」
四国めたん「はい。要素が存在するときだけリスナーを追加できます。」
ずんだもん「複雑なproduct?.variants?.[0]?.pricing?.amountにも使えるの?」
四国めたん「もちろん。多段アクセスも ?. で途切れたらundefinedを返します。」
ずんだもん「?. を活用して安心して深いデータを読みに行くのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: APIレスポンスの処理 */
const response = await fetchUser(id);
const userName = response?.data?.name ?? "Unknown";
const avatar = response?.data?.profile?.avatar;

/** Example 2: イベントハンドラでの利用 */
element?.addEventListener("click", () => {
  console.log(element?.dataset?.id);
});

/** Example 3: 複雑なデータ構造 */
const price = product?.variants?.[0]?.pricing?.amount ?? 0;
const rating = reviews?.[0]?.rating?.average?.toFixed(1);
```
