# #403 「undefinedは「未定義の値」」

四国めたん「undefinedは実際にundefinedという値を返す可能性を示します。」
ずんだもん「findUserは見つからないとundefinedになるんだね。」
四国めたん「はい。呼び出し側でundefinedかどうかチェックします。」
ずんだもん「Config.timeout? みたいなオプショナルもundefinedを返す場合がある?」
四国めたん「その通り。プロパティが無ければundefinedです。」
ずんだもん「voidと違って、値として扱えるんだね。」
四国めたん「edgeケースでもundefinedを明示することで安全になります。」
ずんだもん「未定義の値を扱うときはundefined型を選ぶのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: undefined: 未定義の値 */
function findUser(id: number): User | undefined {
  return users.find(u => u.id === id);
}

/** Example 2: 値としてチェック */
const user = findUser(1);
if (user !== undefined) {
  console.log(user.name);
}

/** Example 3: オプショナルプロパティ */
interface Config {
  timeout?: number;
}
const config: Config = {};
console.log(config.timeout);  // undefined
```
