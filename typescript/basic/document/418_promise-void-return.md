# #418 「return文なし」

四国めたん「Promise<void>ではreturnを書かなくてもOKです。」
ずんだもん「saveUserはreturnなしで完結してたね。」
四国めたん「はい。早期リターンもreturn;で問題ありません。」
ずんだもん「logみたいにreturn undefined; を書くのも許される?」
四国めたん「できますが、基本は省略するのが簡潔です。」
ずんだもん「async関数でもvoidのルールがそのまま適用できるんだね。」
四国めたん「Promise<void> だからといって特別なreturnは不要です。」
ずんだもん「returnスタイルを意識して書くのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: return文なし */
async function saveUser(user: User): Promise<void> {
  await database.save(user);
  console.log("User saved");
}

/** Example 2: 早期リターン */
async function validate(data: Data): Promise<void> {
  if (!data) return;
  await processData(data);
}

/** Example 3: return undefined */
async function log(msg: string): Promise<void> {
  console.log(msg);
  return undefined;
}
```
