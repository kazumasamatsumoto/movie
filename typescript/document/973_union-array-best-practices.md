# #973 「ベストプラクティス」

四国めたん「配列とUnion型を組み合わせるときのベストプラクティスを整理します。」
ずんだもん「型エイリアスで意図を明確に、型ガードを共通化、推論結果をチェック、だったね。」
四国めたん「はい、テストで境界ケースも検証しましょう。」
ずんだもん「レビューで意図が伝わるようコメントを付けるのも有効だよ。」
四国めたん「ベストプラクティスを守って混合データを安全に扱ってください。」
ずんだもん「型システムを最大限に活用しよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 型エイリアス */
type TokenList = (string | number)[];
type ExclusiveList = string[] | number[];

/** Example 2: 型ガード */
const isNumberArray = (value: ExclusiveList): value is number[] =>
  value.every((item) => typeof item === "number");

/** Example 3: テスト */
function assertNever(value: never): never {
  throw new Error(`Unexpected value: ${value}`);
}
```
