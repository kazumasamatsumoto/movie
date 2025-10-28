# #1013 「map<U>(callback: (value: T) => U): U[]」

四国めたん「mapのシグネチャはmap<U>(callback: (value: T, index: number, array: T[]) => U): U[]です。」
ずんだもん「ジェネリックUがコールバックの戻り値型になってるんだね。」
四国めたん「これによって要素の型を自由に変換できます。」
ずんだもん「引数はvalue, index, arrayの3つが用意されているよ。」
四国めたん「シグネチャを理解してコールバックを正しく定義しましょう。」
ずんだもん「型情報を最大限活かしてね！」

---

## 📺 画面表示用コード

```typescript
const values = [10, 20, 30];

/** Example 1: valueだけ利用 */
const strings = values.map((value) => value.toString());

/** Example 2: index利用 */
const labeled = values.map((value, index) => ({ index, value }));

/** Example 3: array参照 */
const ratios = values.map((value, index, array) => value / array.length);
```
