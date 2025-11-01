# #964 「(string | number)[]の要素型」

四国めたん「(string | number)[]の要素を取り出すとstring | numberになります。」
ずんだもん「アクセス時に型ガードを挟む必要があるんだね。」
四国めたん「mapやfilterでも戻り値がUnionになります。」
ずんだもん「操作前にtypeofで絞るのが定番だよ。」
四国めたん「要素型がUnionになる点を理解して安全に扱いましょう。」
ずんだもん「混在に強いパターンだね！」

---

## 📺 画面表示用コード

```typescript
const entries: (string | number)[] = ["ok", 200];

/** Example 1: アクセス */
const first = entries[0]; // string | number

/** Example 2: typeof */
if (typeof first === "string") {
  console.log(first.toUpperCase());
}

/** Example 3: map */
const lengths = entries.map((entry) => entry.toString().length); // number[]
```
