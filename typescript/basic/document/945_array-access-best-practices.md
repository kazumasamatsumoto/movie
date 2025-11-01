# #945 「ベストプラクティス」

四国めたん「要素アクセスのベストプラクティスを押さえましょう。」
ずんだもん「範囲チェック、Optionalチェーン、Nullish Coalescing、at活用がポイントだったね。」
四国めたん「pushやpopの前後で長さが変わる場合は都度チェックを行います。」
ずんだもん「安全なアクセサ関数を用意して再利用するのも良い方法だよ。」
四国めたん「レビューでunsafeアクセスがないか確認しましょう。」
ずんだもん「ベストプラクティスを守って堅牢な配列操作を！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: Helper */
function safeAt<T>(items: T[], index: number): T | undefined {
  return items.at(index);
}

/** Example 2: guard */
function firstOrThrow<T>(items: T[]): T {
  const value = items[0];
  if (value === undefined) throw new Error("empty array");
  return value;
}

/** Example 3: fallback */
const result = safeAt(["ok"], 1) ?? "default";
```
