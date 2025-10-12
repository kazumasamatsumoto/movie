# #581 「typeof型ガードで絞る」

四国めたん「typeof型ガードはunknownを絞る最も基本的な手段です」
ずんだもん「typeof value === \"string\"とか書くやつだね」
四国めたん「はい。プリミティブ型を判定するのに適しています」
ずんだもん「条件の中なら文字列や数値として安心して扱えるよ」
四国めたん「ガードを関数にして再利用するのもおすすめです」
ずんだもん「typeofパターンを押さえればunknownが一気に扱いやすくなるね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: typeofで文字列判定 */
function handle(value: unknown) {
  if (typeof value === "string") {
    console.log(value.trim());
  }
}

/** Example 2: boolean判定 */
function toggle(value: unknown) {
  if (typeof value === "boolean") {
    console.log(value ? "true" : "false");
  }
}

/** Example 3: ヘルパー化 */
const isNumber = (input: unknown): input is number =>
  typeof input === "number";
```
