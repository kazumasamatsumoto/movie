# #822 「BigIntの歴史」

四国めたん「BigIntは2018年にTC39でStage 4となり、ES2020で正式採用されました。」
ずんだもん「TypeScriptはv3.2で型サポートを追加したんだったよね。」
四国めたん「lib.es2020.bigint.d.tsで標準APIが整備されました。」
ずんだもん「Node.jsやモダンブラウザが順次対応して、今では主要環境で使えるよ。」
四国めたん「古い環境ではpolyfillが必要な場合があるのでターゲット設定に注意です。」
ずんだもん「歴史を知ってビルド設定を適切にしよう！」
四国めたん「互換性チェックを忘れず、最新ランタイムでは標準機能として活用できます。」
ずんだもん「BigIntの成り立ちを押さえて導入を進めよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: tsconfigのlib設定 */
const tsconfig = {
  compilerOptions: {
    target: "ES2020",
    lib: ["ES2020", "DOM"],
  },
};

/** Example 2: ランタイムチェック */
if (typeof BigInt === "undefined") {
  throw new Error("BigInt not supported. Consider a polyfill.");
}

/** Example 3: 条件付き利用 */
const maybeBigInt = typeof BigInt !== "undefined" ? BigInt(42) : 42;
```
