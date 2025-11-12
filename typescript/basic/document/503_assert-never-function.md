# #503 「exhaustive check関数」

四国めたん「網羅性関数そのものも作っておこう。」
ずんだもん「assertNever(value: never)はUnexpected valueを投げてたね。」
四国めたん「Shape型のgetArea()でdefault: return assertNever(shape); が決め手。」
ずんだもん「circleやsquareを追加したら自動で未実装がわかるのだ。」
四国めたん「メッセージを差し替えたいときはexhaustiveCheck()を用意できる。」
ずんだもん「JSON.stringify(value)で情報量を増やしてくれてたよ。」
四国めたん「ユーティリティ化するとどのUnionでも同じ書き味。」
ずんだもん「早めに土台を作れば後のリファクタが楽ちん。」

---

## 📺 画面表示用コード

```typescript
/** Example 1: assertNeverの定義 */
function assertNever(value: never): never {
  throw new Error(`Unexpected value: ${value}`);
}

/** Example 2: Shapeの面積計算 */
type Shape = "circle" | "square" | "triangle";

function getArea(shape: Shape): number {
  switch (shape) {
    case "circle":
      return Math.PI;
    case "square":
      return 1;
    case "triangle":
      return 0.5;
    default:
      return assertNever(shape);
  }
}

/** Example 3: カスタムメッセージ */
function exhaustiveCheck(value: never, message?: string): never {
  throw new Error(message || `Unhandled discriminated union member: ${JSON.stringify(value)}`);
}
```
