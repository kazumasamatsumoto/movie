# #562 「unknownユースケース」

四国めたん「unknownの代表的ユースケースを整理しましょう」
ずんだもん「外部API、ユーザー入力、クロスコンパイルの境界だね」
四国めたん「ワーカー通信やメッセージバスもunknownで受けると安全です」
ずんだもん「ライブラリの公開APIでもunknownを返すと拡張性が高まるよ」
四国めたん「テストでも未知の値をモックするのに使えます」
ずんだもん「境界でunknown、内部で具体化のルールを徹底しよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: Web Worker通信 */
addEventListener("message", (event: MessageEvent<unknown>) => {
  if (Array.isArray(event.data)) console.log(event.data.length);
});

/** Example 2: ライブラリの公開API */
export function parsePayload(payload: string): unknown {
  return JSON.parse(payload);
}

/** Example 3: テストモック */
const mockValue: unknown = { id: 1, name: "test" };
expect(typeof mockValue).toBe("object");
```
