# #779 「Symbol.unscopables」

四国めたん「Symbol.unscopablesはwith文で除外したいプロパティを指定します。」
ずんだもん「strict modeではwithが使えないから出番は限られるね。」
四国めたん「互換性のために存在していますが、用途を知っておくと安心です。」
ずんだもん「対象プロパティをtrueに設定するとスコープに入らなくなるんだ。」
四国めたん「TypeScriptではRecord<string, boolean>として扱われます。」
ずんだもん「モダンコードではほとんど使わないけど仕様理解として押さえよう。」
四国めたん「既存ライブラリの動作調査で出会うことがあります。」
ずんだもん「覚えておくとレガシーコード解析が楽になるよ！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: unscopablesの設定 */
const collection = {
  values: () => [1, 2, 3],
  keys: () => ["a", "b", "c"],
  [Symbol.unscopables]: {
    values: true,
  },
};

/** Example 2: 解除 */
collection[Symbol.unscopables]!.values = false;

/** Example 3: 対象プロパティ一覧 */
console.log(collection[Symbol.unscopables]); // { values: false }
```
