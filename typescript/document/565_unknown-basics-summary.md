# #565 「unknown基本まとめ」

四国めたん「unknownの基本ポイントをまとめましょう」
ずんだもん「トップ型、代入自由、操作前チェックが三本柱だね」
四国めたん「はい。型ガードとアサーションを適切に使うのが前提です」
ずんだもん「anyと違って静的解析に守られるのも大切だよ」
四国めたん「プロジェクトの境界でunknownを採用するのが推奨です」
ずんだもん「基本を押さえて次は制約の理由を深掘りしよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 三本柱コメント */
const basics = {
  topType: true,
  assignable: true,
  needsCheck: true,
} as const;

/** Example 2: チェックユーティリティ */
const isString = (value: unknown): value is string => typeof value === "string";

/** Example 3: 入口でunknown */
function fromExternal(input: unknown) {
  if (isString(input)) return input.toUpperCase();
  return String(input);
}
```
