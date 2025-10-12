# #600 「unknown型ガードまとめ」

四国めたん「unknownを守る型ガードを総まとめしましょう」
ずんだもん「typeof、instanceof、in、Array.isArray、カスタムガードが柱だね」
四国めたん「はい。用途に応じて組み合わせればあらゆるデータを安全に扱えます」
ずんだもん「型述語で再利用性を高めるのも忘れずに」
四国めたん「ガードの設計とテストが型安全性を底上げします」
ずんだもん「まとめを実装に落としてunknownを味方につけよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: プリミティブガード */
const isString = (value: unknown): value is string =>
  typeof value === "string";
const isNumber = (value: unknown): value is number =>
  typeof value === "number";

/** Example 2: インスタンスガード */
const isDate = (value: unknown): value is Date => value instanceof Date;
const isError = (value: unknown): value is Error => value instanceof Error;

/** Example 3: in + Array.isArray */
const hasItems = (value: unknown): value is { items: unknown[] } =>
  typeof value === "object"
    && value !== null
    && "items" in value
    && Array.isArray((value as Record<string, unknown>).items);
```
