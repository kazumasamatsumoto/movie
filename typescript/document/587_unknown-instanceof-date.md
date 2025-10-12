# #587 「x instanceof Date」

四国めたん「x instanceof DateでunknownがDateか確認できます」
ずんだもん「APIから日時文字列が来るかもしれないときに便利だね」
四国めたん「Dateインスタンスだけを許して、そのままメソッドを呼べます」
ずんだもん「文字列だったときはパース処理に回せば安心だよ」
四国めたん「時刻計算前にinstanceofで守るのを習慣化しましょう」
ずんだもん「時系列処理のバグを未然に防げるね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: Date確認 */
function formatDate(value: unknown) {
  if (value instanceof Date) {
    return value.toISOString();
  }
  return null;
}

/** Example 2: 文字列 fallback */
function ensureDate(value: unknown): Date {
  if (value instanceof Date) return value;
  if (typeof value === "string") return new Date(value);
  throw new TypeError("invalid date");
}

/** Example 3: 配列フィルタ */
const items: unknown[] = [new Date(), "2024-01-01"];
const dates = items.filter((item): item is Date => item instanceof Date);
```
