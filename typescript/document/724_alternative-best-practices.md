# #724 「代替手段ベストプラクティス」

四国めたん「anyの代替手段を選ぶときのベストプラクティスを整理しましょう」
ずんだもん「まず未知ならunknown、共通ロジックならジェネリクス、選択肢が限られればUnionだね」
四国めたん「はい。計算できるなら条件付き型、再利用ならUtility、最後にアサーションと覚えます」
ずんだもん「パターンごとにチートシートを用意すると迷わないよ」
四国めたん「常に型ガードとテストをセットで考えれば安全です」
ずんだもん「代替手段の引き出しをチームで共有しよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: チートシート */
const cheatsheet = {
  unknown: "外部入力",
  generics: "共通関数",
  union: "限られた選択肢",
  conditional: "型レベル分岐",
  utility: "既存型加工",
} as const;

/** Example 2: 型ガードとの連携 */
const isRecord = (value: unknown): value is Record<string, unknown> =>
  typeof value === "object" && value !== null;

/** Example 3: テスト */
function assertType<T>(_value: T) {}
assertType<{ id: number }>(merge({ id: 1 }, { id: 1 }));
```
