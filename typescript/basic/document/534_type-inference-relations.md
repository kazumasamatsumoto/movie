# #534 「型推論の関係」

四国めたん「neverは型推論と密接に関わっているよ。」
ずんだもん「process()ではstring/numberを判定した後にvalueがneverになるって話だったね。」
四国めたん「型ガードでShapeを判定すると残りのBranchも自動で推論される。」
ずんだもん「circleを処理したらelse側はsquareって分かるのだ。」
四国めたん「InferReturnType<T>みたいに条件付き型で戻り値を抽出するテクも便利。」
ずんだもん「関数型なら推論されて、文字列みたいな型ならneverに落ちる。」
四国めたん「推論とneverを組み合わせるとIDEの補完も強力になるよ。」
ずんだもん「コードの意図を型が語ってくれるのは安心だね。」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 制御フロー推論 */
function process(value: string | number) {
  if (typeof value === "string") {
    return value.toUpperCase();
  } else if (typeof value === "number") {
    return value * 2;
  }
  const check: never = value;
}
```

```typescript
/** Example 2: 型ガード */
type Shape = { kind: "circle" } | { kind: "square" };

function handle(shape: Shape) {
  if (shape.kind === "circle") {
    // shapeはcircle
  } else {
    // shapeはsquare
  }
}
```

```typescript
/** Example 3: InferReturnType */
type InferReturnType<T> =
  T extends (...args: any[]) => infer R ? R : never;

type R1 = InferReturnType<() => string>; // string
type R2 = InferReturnType<string>;       // never
```
