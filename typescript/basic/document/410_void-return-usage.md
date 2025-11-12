# #410 「戻り値を使用」

四国めたん「void戻り値は使ってはいけません。」
ずんだもん「log("Hello") をstringに代入しようとすると怒られるね。」
四国めたん「はい。voidValue: void に代入するならOKです。」
ずんだもん「実行時にはundefinedが返るけど型チェックで防げる?」
四国めたん「process()の結果はundefinedですが、型はvoidなので他の型には代入できません。」
ずんだもん「voidの意図を守って戻り値を無視するのだ!」
四国めたん「その通り。副作用だけに集中しましょう。」

---

## 📺 画面表示用コード

```typescript
/** Example 1: void戻り値は使用不可 */
function log(msg: string): void {
  console.log(msg);
}
const result: string = log("Hello");

/** Example 2: void型変数には代入可 */
const voidValue: void = log("Test");

/** Example 3: 実行時はundefined */
function process(): void {
  return;
}
const value = process();
console.log(value);
```
