# #883 「Arrayメソッド」

四国めたん「bigint配列でもmapやreduceなどのArrayメソッドは問題なく使えます。」
ずんだもん「ただしMath.maxみたいなnumber専用関数には注意だね。」
四国めたん「はい、reduceで独自ロジックを書く必要があります。」
ずんだもん「filterやfindも通常どおり使えるから便利だよ。」
四国めたん「型推論がbigintを維持するので安全です。」
ずんだもん「ArrayメソッドでBigIntコレクションを扱いこなそう！」
四国めたん「メソッドチェーンで演算する際も型を意識してください。」
ずんだもん「number用に暗黙変換されない点を覚えてね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: map */
const ids = [1n, 2n, 3n].map((v) => v << 1n);

/** Example 2: reduce */
const total = ids.reduce((acc, cur) => acc + cur, 0n);

/** Example 3: filter */
const even = ids.filter((v) => v % 2n === 0n);
```
