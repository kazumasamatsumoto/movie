# #743 「typeof s」

四国めたん「symbol値にtypeofを使うと実行時は"symbol"が返ります。」
ずんだもん「型位置でtypeofを使えばunique symbol型を参照できるんだよね。」
四国めたん「constで宣言したシンボルをtypeofで型化すれば判別プロパティに使えます。」
ずんだもん「ランタイムのtypeofチェックで安全に分岐できるのも便利だよ。」
四国めたん「型と実行時の両方でtypeofが活躍します。」
ずんだもん「書き分けを意識すると読みやすいコードになるね。」
四国めたん「typeofの挙動を押さえてシンボルを扱いましょう。」
ずんだもん「型安全なガードでエラーを減らそう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 実行時のtypeof */
const token = Symbol("token");
if (typeof token === "symbol") {
  console.log("symbol detected");
}

/** Example 2: 型位置でのtypeof */
const EVENT = Symbol("event");
function handle(eventType: typeof EVENT) {
  console.log(eventType === EVENT);
}
handle(EVENT);

/** Example 3: 型ガード */
function isSymbol(value: unknown): value is symbol {
  return typeof value === "symbol";
}
console.log(isSymbol(Symbol())); // true
```
