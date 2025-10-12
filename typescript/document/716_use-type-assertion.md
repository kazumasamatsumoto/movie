# #716 「型アサーションの活用」

四国めたん「必要なときは型アサーションでanyから型を断言できます」
ずんだもん「ただし事前に検証したうえで使うのが前提だよね」
四国めたん「はい。unknownと組み合わせれば安全にアサーションできます」
ずんだもん「`as const` や `as T` を適切に活用して型推論をサポートしよう」
四国めたん「乱用するとany同様に危険なので根拠をコメントに残しましょう」
ずんだもん「アサーションは最後の一押しとして慎重に使おう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 検証＋アサーション */
const payload: unknown = JSON.parse('{ "id": 1 }');
if (typeof payload === "object" && payload !== null && "id" in payload) {
  const user = payload as { id: number };
  console.log(user.id);
}

/** Example 2: as const */
const status = ["success", "error"] as const;
type Status = (typeof status)[number];

/** Example 3: 非nullアサーション */
const el = document.getElementById("app")!;
el.textContent = "Hello";
```
