# #286 「nullとundefinedの違い」

四国めたん「今日はnullとundefinedの違いについて学びましょう！」
ずんだもん「どちらも値がない状態を表すけど、意味が違うんだね。」
四国めたん「nullは明示的な空値、undefinedは未定義の状態です。」
ずんだもん「typeof演算子の結果も異なるよ。」
四国めたん「オプショナルプロパティとnullの使い分けも重要です。」
ずんだもん「Nullish Coalescing演算子ではどちらも同じ扱いだね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 基本的な違い */
let a: null = null;          // 明示的な空
let b: undefined = undefined; // 未定義
typeof null;      // "object"
typeof undefined; // "undefined"
```

```typescript
/** Example 2: オプショナルとnullの使い分け */
interface User {
  name?: string;        // string | undefined
  email: string | null; // 明示的null
}
```

```typescript
/** Example 3: Nullish Coalescing */
const value1 = null ?? "default";      // "default"
const value2 = undefined ?? "default"; // "default"
```
