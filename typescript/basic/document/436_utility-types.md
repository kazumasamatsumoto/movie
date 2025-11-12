# #436 「Utility Types」

四国めたん「Utility Typesでもvoidを扱えます。」
ずんだもん「ReturnType<typeof log> がvoidになる例があったね。」
四国めたん「はい。Parametersと組み合わせて可変長引数のvoid関数も作れます。」
ずんだもん「Record<string, () => void> でイベントマップを作ってた!」
四国めたん「Utility Typesで型変換を自動化できるので便利です。」
ずんだもん「voidを中心にしたUtilityレシピを覚えるのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: ReturnTypeでvoid */

function log(msg: string): void {
  console.log(msg);
}
type LogReturn = ReturnType<typeof log>;

/** Example 2: Parametersとの組み合わせ */

type VoidFunction<T extends any[]> = (...args: T) => void;
type Handler = VoidFunction<[string, number]>;

/** Example 3: Record */

type EventMap = Record<string, () => void>;
const events: EventMap = {
  click: () => console.log("Click"),
  hover: () => console.log("Hover"),
};
```
