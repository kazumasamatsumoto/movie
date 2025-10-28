# #940 「Nullish Coalescing」

四国めたん「OptionalチェーンとNullish Coalescingを組み合わせるとフォールバックが書きやすくなります。」
ずんだもん「const value = arr?.[0] ?? defaultValue; みたいにね。」
四国めたん「undefinedだった場合に安全な値を返せます。」
ずんだもん「atメソッドと組み合わせても同じように使えるよ。」
四国めたん「Nullish Coalescingで安全な初期値を提供しましょう。」
ずんだもん「エラーを起こさずに値を渡せるね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: フォールバック */
const list: string[] | undefined = fetchList();
const first = list?.[0] ?? "(empty)";

/** Example 2: atと併用 */
const value = [10, 20].at(5) ?? 0;

/** Example 3: 関数 */
function getOrDefault<T>(items: T[] | undefined, index: number, fallback: T): T {
  return items?.[index] ?? fallback;
}
```
