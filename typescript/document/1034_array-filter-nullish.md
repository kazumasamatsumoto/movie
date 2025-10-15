# #1034 「null/undefined除去」

四国めたん「filterはnullやundefinedを除去するのにも便利です。」
ずんだもん「value != nullとかBooleanで絞り込むやつだね。」
四国めたん「はい、NonNullableを使うとより明示的になります。」
ずんだもん「データクレンジングの定番パターンだよ。」
四国めたん「null/undefined除去の書き方を覚えておきましょう。」
ずんだもん「安全な配列を手に入れよう！」

---

## 📺 画面表示用コード

```typescript
const mixed = ["meta", undefined, "zunda", null];

/** Example 1: != null */
const cleaned = mixed.filter((value): value is string => value != null);

/** Example 2: Boolean */
const truthy = mixed.filter(Boolean);

/** Example 3: NonNullable */
const nonNullable = mixed.filter((value): value is NonNullable<typeof value> => value !== null && value !== undefined);
```
