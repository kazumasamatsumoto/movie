# #511 「型ガード」

四国めたん「今日は型ガードでUnionを絞り込むよ。」
ずんだもん「Shapeのarea()はkindを見て面積を計算してたね。」
四国めたん「circle/square/rectangleを全部書いてconst check: never = shapeで締めるの。」
ずんだもん「カスタム型ガードisCircle()を作ると読みやすさが上がるのだ。」
四国めたん「process()でisCircle(shape)ならradiusに型が絞られてたよ。」
ずんだもん「残りの型は別の処理に回せるから保守しやすい。」
四国めたん「型ガードを揃えておくと網羅性チェックも楽になる。」
ずんだもん「Unionが増えても安心感が段違いだね。」

---

## 📺 画面表示用コード

```typescript
/** Example 1: kindで面積を計算 */
type Shape =
  | { kind: "circle"; radius: number }
  | { kind: "square"; size: number }
  | { kind: "rectangle"; width: number; height: number };

function area(shape: Shape): number {
  if (shape.kind === "circle") {
    return Math.PI * shape.radius ** 2;
  } else if (shape.kind === "square") {
    return shape.size ** 2;
  } else if (shape.kind === "rectangle") {
    return shape.width * shape.height;
  }
  const check: never = shape;
  throw new Error(`未処理: ${JSON.stringify(check)}`);
}

/** Example 2: カスタム型ガード */
function isCircle(shape: Shape): shape is Extract<Shape, { kind: "circle" }> {
  return shape.kind === "circle";
}

/** Example 3: 型ガードの利用 */
function process(shape: Shape): number {
  if (isCircle(shape)) {
    return shape.radius; // circleに絞り込み
  }
  // ここではsquare/rectangle
  return area(shape);
}
```
