# #344 「オプショナルプロパティの型」

四国めたん「オプショナルプロパティの型について学びましょう!」
ずんだもん「プロパティ?: T は、T | undefined と同じなんだね!」
四国めたん「はい。どちらも同じ型を表現しています。」
ずんだもん「アクセス時はチェックが必要なの?」
四国めたん「その通りです。undefined チェックを行ってから、安全に使用します。」
ずんだもん「Optional Chaining も使えるんだね!」
四国めたん「はい。?. 演算子で、undefinedの場合も安全にアクセスできます。」
ずんだもん「オプショナルプロパティの型を理解して、安全にアクセスするのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: オプショナルとundefinedableの等価性 */
interface User1 {
  age?: number;              // number | undefined
}
interface User2 {
  age: number | undefined;   // 同じ型
}

/** Example 2: アクセス時のチェック */
const user: User1 = { age: 30 };
if (user.age !== undefined) {
  console.log(user.age + 1);
}

/** Example 3: Optional Chainingでの安全なアクセス */
const age = user.age?.toString();
const doubled = user.age ? user.age * 2 : 0;
```
