# #597 「段階的な絞り込み」

四国めたん「unknownは段階的に絞り込むと安全性と可読性が両立します」
ずんだもん「まずtypeofで広くチェックしてから、細かい条件に進むんだよね」
四国めたん「はい。一気に書くよりステップを分けた方が意図が明確です」
ずんだもん「途中でログを仕込むとデバッグもしやすいよ」
四国めたん「各段階で失敗時のフォールバックも決めておきましょう」
ずんだもん「ステップナローイングで安全な処理を作ろう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: ステップ1 - typeof */
function process(value: unknown) {
  if (typeof value !== "object" || value === null) return null;
  if (!("data" in value)) return null;
  const data = (value as { data: unknown }).data;
  if (!Array.isArray(data)) return null;
  return data;
}

/** Example 2: ログ付き */
function stepwise(value: unknown) {
  if (typeof value !== "string") {
    console.warn("not string", value);
    return null;
  }
  if (value.length === 0) return null;
  return value;
}

/** Example 3: 汎用ヘルパー */
const getArray = (value: unknown): unknown[] | null =>
  Array.isArray(value) ? value : null;
```
