# #951 「typeof型ガード」

四国めたん「typeofを使った型ガードは混合型配列でよく使います。」
ずんだもん「typeof value === "string"とかだね。」
四国めたん「はい、プリミティブの判定に向いています。」
ずんだもん「switch (typeof value) で分岐させるパターンもあるよ。」
四国めたん「typeof型ガードを使えばUnion型を安全に絞り込めます。」
ずんだもん「簡単で強力なテクニックだね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: if */
const payload: (string | number)[] = ["code", 200];
for (const item of payload) {
  if (typeof item === "string") {
    console.log(item.toUpperCase());
  } else {
    console.log(item.toFixed(0));
  }
}

/** Example 2: switch */
function describe(value: string | number) {
  switch (typeof value) {
    case "string":
      return `text:${value}`;
    case "number":
      return `num:${value}`;
  }
}

/** Example 3: filter */
const strings = payload.filter((item): item is string => typeof item === "string");
```
