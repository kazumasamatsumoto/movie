# #881 「JSON.stringify()」

四国めたん「改めてJSON.stringifyでbigintを扱うときの挙動を確認しましょう。」
ずんだもん「既定ではTypeError、replacerで文字列化すれば回避できたね。」
四国めたん「はい、replacer内でtypeof v === "bigint" をチェックします。」
ずんだもん「リバース時にBigIntへ戻すreviverもセットで用意しよう。」
四国めたん「ライブラリを通す場合は事前に文字列化しておくのが安全です。」
ずんだもん「JSON.stringifyの制限を意識してシリアライズ戦略を立てよう！」
四国めたん「テストで期待どおりに動くか必ず確認してください。」
ずんだもん「replacerとreviverをセットで覚えてね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: replacer */
const json = JSON.stringify({ amount: 99n }, (_, value) =>
  typeof value === "bigint" ? value.toString() : value,
);

/** Example 2: reviver */
const parsed = JSON.parse(json, (_, value) =>
  typeof value === "string" && /^-?\d+$/.test(value) ? BigInt(value) : value,
);

/** Example 3: テスト */
console.log(parsed.amount === 99n);
```
