# #367 「間違い(2) - チェック漏れ」

四国めたん「!を先に書いてしまうとnullチェックを怠りがちです。」
ずんだもん「processUserでfindUser(id)! とすると存在しないIDで落ちるね。」
四国めたん「はい。実行時にnullならプロパティアクセスで例外になります。」
ずんだもん「正しくはnullかどうか判定してから進める?」
四国めたん「if (user === null) return; のように早期リターンで守りましょう。」
ずんだもん「Optional Chainingなら安全に名前を取得できる?」
四国めたん「user?.name ?? "Unknown" なら存在しなくても落ちません。」
ずんだもん「チェックをサボって!に任せないのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: チェック漏れの例 */
function processUser(id: number) {
  const user = findUser(id)!;  // nullの可能性を無視
  console.log(user.name);      // 実行時エラーの可能性
}

/** Example 2: 正しいチェック */
function processUser(id: number) {
  const user = findUser(id);
  if (user === null) {
    console.log("User not found");
    return;
  }
  console.log(user.name);  // 安全
}

/** Example 3: Optional Chainingで対処 */
function processUser(id: number) {
  const user = findUser(id);
  const name = user?.name ?? "Unknown";
  console.log(name);
}
```
