# #944 「実例」

四国めたん「配列アクセスと分割代入を組み合わせた実例を見ましょう。」
ずんだもん「ログの先頭を取り出して残りをキューに戻す処理とかいいね。」
四国めたん「はい、atやNullish Coalescingも併用して安全に書きます。」
ずんだもん「存在チェックとフォールバックを組み合わせるのがポイントだよ。」
四国めたん「実例で安全なアクセスパターンを体験してください。」
ずんだもん「配列操作がスムーズになるよ！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 先頭取得 */
function shiftLog(logs: string[]): { head?: string; rest: string[] } {
  const [head, ...rest] = logs;
  return { head, rest };
}

/** Example 2: at + fallback */
function peek<T>(items: T[], index: number, fallback: T): T {
  return items.at(index) ?? fallback;
}

/** Example 3: safe dequeue */
function dequeue<T>(queue: T[]): T | undefined {
  if (!queue.length) return undefined;
  const [first] = queue;
  queue.splice(0, 1);
  return first;
}
```
