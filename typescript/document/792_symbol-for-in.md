# #792 「for...in」

四国めたん「for...inは列挙可能な文字列キーだけを対象にします。」
ずんだもん「symbolキーはループに出てこないんだね。」
四国めたん「はい、シンボルプロパティを走査したい場合は別のAPIを使います。」
ずんだもん「Object.getOwnPropertySymbolsを組み合わせればOKだよ。」
四国めたん「Reflect.ownKeysで一括取得してフィルタする方法もあります。」
ずんだもん「for...inの仕様を理解して誤った処理を避けよう！」
四国めたん「列挙用途に応じて正しいループを選択してください。」
ずんだもん「symbolを扱うときはループ戦略が大事だね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: for...inでは見えない */
const SFLAG = Symbol("flag");
const data = { visible: true, [SFLAG]: false };
for (const key in data) {
  console.log(key); // "visible" のみ
}

/** Example 2: symbolを個別走査 */
for (const sym of Object.getOwnPropertySymbols(data)) {
  console.log(sym.description, (data as Record<symbol, unknown>)[sym]);
}

/** Example 3: Reflect.ownKeysとの組み合わせ */
for (const key of Reflect.ownKeys(data)) {
  if (typeof key === "symbol") {
    console.log("symbol", key.description);
  }
}
```
