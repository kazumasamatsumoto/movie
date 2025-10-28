# #790 「Object.keys()」

四国めたん「Object.keysは文字列キーだけを返します。」
ずんだもん「symbolキーはリストに含まれないんだね。」
四国めたん「列挙したい場合はObject.getOwnPropertySymbolsかReflect.ownKeysを使います。」
ずんだもん「Object.valuesやObject.entriesも同じ挙動だよ。」
四国めたん「TypeScriptの型システムでもkeysはstring[]として扱われます。」
ずんだもん「違いを理解して意図したキーだけを処理しよう！」
四国めたん「Object.keysの特性を利用して公開プロパティを絞り込めます。」
ずんだもん「symbolを安全に隠しながらstringキーを操作しよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: Object.keys */
const SECRET = Symbol("secret");
const record = { name: "alpha", [SECRET]: true };
console.log(Object.keys(record)); // ["name"]

/** Example 2: Object.entries */
console.log(Object.entries(record)); // [["name", "alpha"]]

/** Example 3: 公開プロパティのみ処理 */
Object.keys(record).forEach((key) => {
  console.log(`${key}: ${record[key as keyof typeof record]}`);
});
```
