# #1028 「filter(callback: (value: T) => boolean): T[]」

四国めたん「基本的なfilterのシグネチャはfilter(callback: (value: T) => boolean): T[]です。」
ずんだもん「戻り値がtrueなら残して、falseなら捨てるんだね。」
四国めたん「はい、シンプルな真偽値判定で絞り込む形です。」
ずんだもん「indexやarrayも引数として受け取れるよ。」
四国めたん「まずはこの基本形を意識して使いましょう。」
ずんだもん「シンプルで扱いやすいね！」

---

## 📺 画面表示用コード

```typescript
const values = ["meta", "", "zunda"];

/** Example 1: truthy */
const nonEmpty = values.filter((value) => Boolean(value));

/** Example 2: index利用 */
const evenIndex = values.filter((_, index) => index % 2 === 0);

/** Example 3: array参照 */
const withLength = values.filter((value, index, array) => value.length === array[0].length);
```
