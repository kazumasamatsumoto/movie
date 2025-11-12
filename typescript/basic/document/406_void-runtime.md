# #406 「実際の戻り値」

四国めたん「voidでも実行時はundefinedが返ります。」
ずんだもん「log("Hello") の結果をconsole.logするとundefinedだった!」
四国めたん「はい。ただし型システムではvoidとして扱います。」
ずんだもん「const value: void = log("Test") のように受け取れるの?」
四国めたん「できますが、stringには代入できません。」
ずんだもん「JavaScriptではfunction f1(): void もトランスパイル後は同じなんだね。」
四国めたん「はい。function f1() {} がundefinedを返します。」
ずんだもん「実行時と型レベルを区別して理解するのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 型はvoid、実行時はundefined */
function log(msg: string): void {
  console.log(msg);
}
const result = log("Hello");
console.log(result);
console.log(typeof result);

/** Example 2: 型システムでの扱い */
const value: void = log("Test");
// const str: string = log("Test");

/** Example 3: JavaScriptレベル */
function f1(): void {}
// Transpiled JavaScript
function f1() {}
```
