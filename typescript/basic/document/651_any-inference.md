# #651 「anyが型推論へ与える影響」

四国めたん「anyが登場すると型推論の結果までanyになります」
ずんだもん「配列にanyが混ざると全体がany[]になるやつだね」
四国めたん「はい。ジェネリクスでも束縛が崩れて安全性が失われます」
ずんだもん「推論に頼るコードほど影響が大きいよ」
四国めたん「推論結果を守りたいならanyを避け、unknownで受けるのが鉄則です」
ずんだもん「推論チェーンを壊さない設計を意識しよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 配列推論 */
const list = [1, "two", undefined as any];
// 推論結果: any[]

/** Example 2: ジェネリクス */
function wrap<T>(value: T) {
  return { value };
}
const wrapped = wrap<any>("text"); // value: any

/** Example 3: unknownで守る */
const safeList = [1, "two", undefined as unknown];
```
