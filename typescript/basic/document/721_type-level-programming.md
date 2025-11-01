# #721 「型レベルプログラミングで置き換える」

四国めたん「型レベルプログラミングを使えば複雑なanyも安全に置き換えられます」
ずんだもん「条件付き型やテンプレートリテラルで型を計算するんだね」
四国めたん「はい。実行時ロジックを型に反映させれば補完と検証が両立します」
ずんだもん「難しいけど型負債を減らす強力な手段だよ」
四国めたん「型レベルの抽象化でanyから脱却しましょう」
ずんだもん「理論と実践を結びつけて型の力を引き出そう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: テンプレートリテラル型 */
type EventName<T extends string> = `app:${T}`;
type UserEvent = EventName<"login" | "logout">; // "app:login" | "app:logout"

/** Example 2: 型レベルフィルタ */
type ExtractKeysByValueType<T, Value> = {
  [K in keyof T]: T[K] extends Value ? K : never;
}[keyof T];

/** Example 3: Schema解析 */
type Schema = { type: "string"; maxLength?: number } | { type: "number"; min?: number };
type InferSchema<T> = T extends { type: "string" }
  ? string
  : T extends { type: "number" }
  ? number
  : never;
```
