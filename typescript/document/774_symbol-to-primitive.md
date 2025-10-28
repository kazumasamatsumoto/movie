# #774 「Symbol.toPrimitive」

四国めたん「Symbol.toPrimitiveは値をプリミティブに変換するときの挙動を定義します。」
ずんだもん「numberやstring、defaultといったヒントが渡されるんだよね。」
四国めたん「ヒントに応じて返却値を切り替えられます。」
ずんだもん「通貨オブジェクトの表示や演算で便利だよ。」
四国めたん「TypeScriptでは(hint) => {...}のシグネチャを実装します。」
ずんだもん「暗黙変換を制御して安全にデバッグしよう！」
四国めたん「Symbol.toPrimitiveで直感的なAPIを構築できます。」
ずんだもん「実装例を見て使い所を掴もう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: ヒントごとの振る舞い */
const amount = {
  value: 1200,
  currency: "JPY",
  [Symbol.toPrimitive](hint: "number" | "string" | "default") {
    if (hint === "number") return this.value;
    if (hint === "string") return `${this.value} ${this.currency}`;
    return this.value;
  },
};

/** Example 2: 数値演算 */
console.log(+amount); // 1200
console.log(amount + 300); // 1500 (default -> number)

/** Example 3: 文字列変換 */
console.log(`${amount}`); // "1200 JPY"
```
