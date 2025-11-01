# #582 「typeof x === "string"」

四国めたん「typeof x === "string"はunknownを文字列に絞る定番です」
ずんだもん「trimやtoUpperCaseが安心して呼べるようになるね」
四国めたん「はい。条件内ではstring型として型推論されます」
ずんだもん「複数の条件と組み合わせて段階的に絞り込めるよ」
四国めたん「必ずブロック内のみで操作するのがポイントです」
ずんだもん「文字列ガードをうまく使いこなそう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: stringガード */
function normalize(value: unknown) {
  if (typeof value === "string") {
    return value.trim().toLowerCase();
  }
  return null;
}

/** Example 2: 共通ユーティリティ */
const isString = (input: unknown): input is string =>
  typeof input === "string";

/** Example 3: 配列をフィルタ */
const mixed: unknown[] = ["A", 1, "B"];
const strings = mixed.filter((item): item is string => typeof item === "string");
```
