# #1019 「this引数」

四国めたん「mapには第二引数でthisを指定できます。」
ずんだもん「map(callback, thisArg)って書くやつだね。」
四国めたん「はい、コールバック内でthisを使う場合に便利ですが、アロー関数では無視されます。」
ずんだもん「クラスメソッドをバインドするときに役立つよ。」
四国めたん「this引数の使い方も押さえておきましょう。」
ずんだもん「状況に応じて使い分けてね！」

---

## 📺 画面表示用コード

```typescript
const values = [1, 2, 3];

const helper = {
  base: 10,
  toLabel(value: number) {
    return `${this.base + value}`;
  },
};

/** Example 1: thisArg */
const labels = values.map(function (value) {
  return this.toLabel(value);
}, helper);

/** Example 2: アロー関数はthisArg無視 */
const ignored = values.map((value) => value + helper.base, { base: 100 });

/** Example 3: bind代替 */
const labelsWithBind = values.map(helper.toLabel.bind(helper));
```
