# #505 「判別Union型」

四国めたん「判別Unionならkindやtypeで分岐できるよ。」
ずんだもん「ShapeのgetArea()はkindごとに面積を出してたね。」
四国めたん「defaultでassertNever(shape)を書けば新しい図形も怖くない。」
ずんだもん「ReduxのActionもtypeを見てreducerが網羅してたのだ。」
四国めたん「increment/decrement/setを全部処理して最後にassertNever(action)。」
ずんだもん「Eventハンドラもclickとkeypressをログしてたよ。」
四国めたん「typeを追加した瞬間にhandleEvent()が赤くなるのが狙い。」
ずんだもん「判別Unionはスイッチ漏れ検出の最強パターンだね。」

---

## 📺 画面表示用コード

```typescript
/** Example 1: Shapeの面積 */
type Circle = { kind: "circle"; radius: number };
type Square = { kind: "square"; size: number };
type Triangle = { kind: "triangle"; base: number; height: number };
type Shape = Circle | Square | Triangle;

function assertNever(value: never): never {
  throw new Error(`Unhandled: ${JSON.stringify(value)}`);
}

function getArea(shape: Shape): number {
  switch (shape.kind) {
    case "circle":
      return Math.PI * shape.radius ** 2;
    case "square":
      return shape.size ** 2;
    case "triangle":
      return (shape.base * shape.height) / 2;
    default:
      return assertNever(shape);
  }
}

/** Example 2: Reduxアクション */
type Action =
  | { type: "increment" }
  | { type: "decrement" }
  | { type: "set"; payload: number };

function reducer(state: number, action: Action): number {
  switch (action.type) {
    case "increment":
      return state + 1;
    case "decrement":
      return state - 1;
    case "set":
      return action.payload;
    default:
      return assertNever(action);
  }
}

/** Example 3: イベント処理 */
type Event =
  | { type: "click"; x: number; y: number }
  | { type: "keypress"; key: string };

function handleEvent(event: Event): void {
  switch (event.type) {
    case "click":
      console.log(`Clicked at ${event.x}, ${event.y}`);
      break;
    case "keypress":
      console.log(`Key: ${event.key}`);
      break;
    default:
      assertNever(event);
  }
}
```
