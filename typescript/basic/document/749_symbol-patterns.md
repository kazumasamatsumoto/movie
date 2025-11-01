# #749 「基本パターン」

四国めたん「symbolの基本パターンを3つ押さえましょう。」
ずんだもん「1つ目は隠しプロパティ、2つ目は判別プロパティだね。」
四国めたん「3つ目はDIトークンやレジストリでの識別子利用です。」
ずんだもん「この3つを押さえればほとんどの現場ケースをカバーできるよ。」
四国めたん「TypeScriptの型付けで安全性も担保しましょう。」
ずんだもん「パターン化してリファクタリングしやすくしよう。」
四国めたん「必要に応じてunique symbolと組み合わせるのも効果的です。」
ずんだもん「基本パターンを覚えて実装に活かそう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 隠しプロパティパターン */
const INTERNAL = Symbol("INTERNAL");
const component = { name: "Button", [INTERNAL]: { version: 1 } };

/** Example 2: 判別プロパティパターン */
const NODE_TEXT = Symbol("text");
const NODE_IMAGE = Symbol("image");
type Node =
  | { kind: typeof NODE_TEXT; text: string }
  | { kind: typeof NODE_IMAGE; src: string };

/** Example 3: DIトークンパターン */
const LOGGER_TOKEN = Symbol("LOGGER");
const services = new Map<symbol, unknown>([[LOGGER_TOKEN, console]]);
```
