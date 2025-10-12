# #666 「anyはコードの保守性を下げる」

四国めたん「anyが多いコードは保守性が一気に下がります」
ずんだもん「影響範囲が読めないし、修正後の保証も取りづらいんだよね」
四国めたん「はい。レビューも困難になり、開発速度がじわじわ落ちます」
ずんだもん「型を付けて置けば影響範囲が静的に追えるのが強みだよ」
四国めたん「保守性を守るためにもanyを減らす施策が必要です」
ずんだもん「長期運用を見据えて型安全にしていこう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: anyだらけのシグネチャ */
function handle(payload: any, options: any): any {
  return options.process(payload);
}

/** Example 2: 型付きシグネチャ */
interface Options {
  process(payload: User): Result;
}

/** Example 3: 影響範囲可視化 */
type User = { id: number; name: string };
type Result = { ok: boolean };
```
