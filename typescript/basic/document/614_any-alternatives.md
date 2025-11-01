# #614 「any型の代替手段」

四国めたん「anyの代替としてunknownやUnion型、ジェネリクスを活用しましょう」
ずんだもん「状況に合わせて意味のある型を選べば安全になるね」
四国めたん「はい。unknownで受けて、必要に応じて型ガードや型パラメータで絞ります」
ずんだもん「型ユーティリティも積極的に使いたいよ」
四国めたん「代替案を知っていればanyに頼る必要が減ります」
ずんだもん「最適な型設計で品質を底上げしよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: unknownで受ける */
function handle(value: unknown) {
  if (typeof value === "string") return value.toUpperCase();
  return String(value);
}

/** Example 2: Union型 */
type ApiResult = { ok: true; data: string } | { ok: false; error: string };

/** Example 3: ジェネリクス */
function wrap<T>(value: T): { value: T } {
  return { value };
}
```
