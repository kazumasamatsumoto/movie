# #989 「型の絞り込み」

四国めたん「型ガードやfilterを使うと配列要素の型を絞り込めます。」
ずんだもん「Union配列から特定の型だけ取り出すときに便利だね。」
四国めたん「if文やswitchでtypeofを使っても絞り込みが行われます。」
ずんだもん「型の絞り込みを理解して安全に後続処理を書こう。」
四国めたん「TypeScriptの制御フロー解析を活用してください。」
ずんだもん「絞り込みで型安全なコードにしよう！」

---

## 📺 画面表示用コード

```typescript
const payload: (string | number)[] = ["ok", 200];

/** Example 1: if */
for (const item of payload) {
  if (typeof item === "string") {
    console.log(item.toUpperCase());
  } else {
    console.log(item.toFixed(0));
  }
}

/** Example 2: switch */
for (const item of payload) {
  switch (typeof item) {
    case "string":
      console.log(`text:${item}`);
      break;
    case "number":
      console.log(`num:${item}`);
      break;
  }
}

/** Example 3: filter */
const strings = payload.filter((item): item is string => typeof item === "string");
```
