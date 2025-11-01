# #628 「実践例集①」

四国めたん「unknown活用の実践例を3つ紹介します」
ずんだもん「フォーム入力検証、APIレスポンス、外部イベントだね」
四国めたん「はい。境界でunknownを受けて型ガードで整形します」
ずんだもん「この流れをテンプレート化すると開発が加速するよ」
四国めたん「身近な例でunknownのメリットを確認しましょう」
ずんだもん「パターンを自分のプロジェクトでも試してみよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: フォーム入力 */
const input: unknown = formData.get("email");
if (typeof input === "string") console.log(input.toLowerCase());

/** Example 2: APIレスポンス */
const payload: unknown = await fetch("/api/items").then((res) => res.json());
if (Array.isArray(payload)) console.log(payload.length);

/** Example 3: 外部イベント */
addEventListener("message", (event: MessageEvent<unknown>) => {
  if (typeof event.data === "object") console.log("ok");
});
```
