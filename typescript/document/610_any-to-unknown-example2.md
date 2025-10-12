# #610 「anyからunknown移行・実例2」

四国めたん「次はメッセージイベントのanyをunknownに改善しましょう」
ずんだもん「event.data: anyをunknownに変えてガードするんだよね」
四国めたん「はい。Array.isArrayやin演算子で安全にデータを扱います」
ずんだもん「Type Guardを共有化すれば他のリスナーにも展開できるよ」
四国めたん「ランタイムエラーが激減する構成に変わります」
ずんだもん「フロントのリアルタイム処理も安心だね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 変更前 */
addEventListener("message", (event: MessageEvent<any>) => {
  console.log(event.data.items.length);
});

/** Example 2: 変更後 */
addEventListener("message", (event: MessageEvent<unknown>) => {
  if (Array.isArray(event.data)) console.log(event.data.length);
});

/** Example 3: 型ガード関数 */
const hasItems = (value: unknown): value is { items: unknown[] } =>
  typeof value === "object" && value !== null && "items" in value;
```
