# #920 「配列リテラルの型推論」

四国めたん「要素付きの配列リテラルは要素型から型推論されます。」
ずんだもん「[1, 2, 3]ならnumber[]、["a", "b"]ならstring[]だね。」
四国めたん「はい、混在すると最も広い共通型のUnionになります。」
ずんだもん「as constを付けるとタプルに近いリテラル型になるよ。」
四国めたん「推論結果を理解しておくと予期せぬanyを避けられます。」
ずんだもん「配列リテラルの推論を味方にしよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: number[]推論 */
const nums = [1, 2, 3]; // 型: number[]

/** Example 2: Union */
const mixed = [1, "two"]; // 型: (string | number)[]

/** Example 3: as const */
const tuple = [1, 2, 3] as const; // 型: readonly [1, 2, 3]
```
