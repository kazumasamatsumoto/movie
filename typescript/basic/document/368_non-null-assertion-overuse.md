# #368 「間違い(3) - !演算子乱用」

四国めたん「!を連打するとコードの意図が見えなくなります。」
ずんだもん「response.data!.users!.find(...)! みたいな鎖は危険だね。」
四国めたん「はい。どこか一つでもnullならすぐエラーです。」
ずんだもん「型ガードを挟めば可読性も安全性も上がる?」
四国めたん「usersが存在するかをifで確認し、profile?.nameをチェックしましょう。」
ずんだもん「Lintルールで禁止する方法もあるの?」
四国めたん「@typescript-eslint/no-non-null-assertion をerrorにすると乱用を防げます。」
ずんだもん「必要なときだけ!を書ける環境を整えるのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 乱用の例 */
const data = response.data!.users!.find(u => u.id === id)!;
const name = data.profile!.name!.toUpperCase();

/** Example 2: 適切な型ガード */
if (response.data?.users) {
  const user = response.data.users.find(u => u.id === id);
  if (user?.profile?.name) {
    const name = user.profile.name.toUpperCase();
  }
}

/** Example 3: ESLintでの制限 */
// .eslintrc.json
{
  "rules": {
    "@typescript-eslint/no-non-null-assertion": "error"
  }
}
```
