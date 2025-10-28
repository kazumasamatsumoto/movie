# #789 「列挙不可性」

四国めたん「symbolプロパティは列挙対象から除外されるのが基本です。」
ずんだもん「for...inやObject.keysでは見えないんだよね。」
四国めたん「enumerable属性に関係なく自動的に外れます。」
ずんだもん「ただしReflect.ownKeysかObject.getOwnPropertySymbolsを使えば見えるよ。」
四国めたん「列挙不可性を活かして内部状態を隠しましょう。」
ずんだもん「デバッグ時は意図的に列挙してチェックしてね。」
四国めたん「列挙動作を理解してデータ設計に活かしてください。」
ずんだもん「隠したいけどアクセスしたい情報にぴったりだよ！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: for...in */
const TOKEN = Symbol("token");
const model = { name: "task", [TOKEN]: 123 };
for (const key in model) {
  console.log(key); // "name" のみ
}

/** Example 2: 列挙属性 */
const descriptor = Object.getOwnPropertyDescriptor(model, TOKEN);
console.log(descriptor?.enumerable); // false

/** Example 3: Reflect.ownKeys */
console.log(Reflect.ownKeys(model));
```
