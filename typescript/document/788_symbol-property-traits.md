# #788 「シンボルプロパティの特性」

四国めたん「シンボルプロパティはデフォルトで列挙対象から外れます。」
ずんだもん「Object.keysやfor...inには出てこないんだよね。」
四国めたん「はい、ただしReflect.ownKeysなら取得できます。」
ずんだもん「JSON.stringifyでも無視されるから隠し情報に向いてるよ。」
四国めたん「プロパティディスクリプタで属性を調整することも可能です。」
ずんだもん「特性を理解してデータの見せ方をコントロールしよう！」
四国めたん「次の回で列挙動作を詳しく見ます。」
ずんだもん「シンボルプロパティの性質を把握してね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: Object.keysには出ない */
const SECRET = Symbol("secret");
const payload = { id: 1, [SECRET]: "hidden" };
console.log(Object.keys(payload)); // ["id"]

/** Example 2: Reflect.ownKeysは取得 */
console.log(Reflect.ownKeys(payload)); // ["id", Symbol(secret)]

/** Example 3: JSON.stringifyで無視 */
console.log(JSON.stringify(payload)); // {"id":1}
```
