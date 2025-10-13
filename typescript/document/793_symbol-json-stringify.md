# #793 「JSON.stringify()」

四国めたん「JSON.stringifyはsymbolプロパティをシリアライズしません。」
ずんだもん「文字列キーだけがJSONに出力されるんだね。」
四国めたん「はい、シンボルは仕様上無視されます。」
ずんだもん「replacer関数を使ってもsymbolキーは渡されないから気をつけてね。」
四国めたん「必要なら事前に文字列化したエントリを追加しましょう。」
ずんだもん「シリアライズ要件を決めてから設計することが大事だよ。」
四国めたん「JSON出力に含めたくない情報を隠す用途に便利です。」
ずんだもん「挙動を理解して安全にデータ交換しよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: シンボルは無視 */
const META = Symbol("meta");
const response = { id: 10, [META]: { internal: true } };
console.log(JSON.stringify(response)); // {"id":10}

/** Example 2: replacerでも触れない */
const json = JSON.stringify(response, (key, value) => {
  console.log("replacer", key); // symbolキーは出力されない
  return value;
});
console.log(json);

/** Example 3: 文字列化して含める */
const serializable = {
  ...response,
  meta: (response as Record<symbol, unknown>)[META],
};
console.log(JSON.stringify(serializable));
```
