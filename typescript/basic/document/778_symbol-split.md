# #778 「Symbol.split」

四国めたん「Symbol.splitはString.prototype.splitをカスタマイズします。」
ずんだもん「配列を返す関数を実装すればいいんだね。」
四国めたん「引数は( text: string, limit?: number )です。」
ずんだもん「YAML風の区切りとか特殊な分割ロジックに使えそうだよ。」
四国めたん「正規表現以外の分割条件を作れるのが強みです。」
ずんだもん「Symbol.splitで柔軟な文字列分解をしよう！」
四国めたん「副作用のない純粋関数にしてテストしやすく保つと良いですね。」
ずんだもん「用途に合わせたSplitを設計しよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: カスタムsplit */
const yamlSplit = {
  [Symbol.split](text: string): string[] {
    return text.split(/\n-\s*/).filter(Boolean);
  },
};

/** Example 2: 使用例 */
const yaml = "- foo\n- bar\n- baz";
console.log(yaml.split(yamlSplit)); // ["foo", "bar", "baz"]

/** Example 3: limit対応 */
const limitedSplit = {
  [Symbol.split](text: string, limit = Infinity): string[] {
    const parts = text.split(/\s+/);
    return parts.slice(0, limit);
  },
};
console.log("a b c d".split(limitedSplit, 2)); // ["a", "b"]
```
