# #734 「Symbol()関数」

四国めたん「Symbolはnewではなく関数呼び出しで生成します。」
ずんだもん「コンストラクタっぽい名前だけど、newを付けるとTypeErrorだよね。」
四国めたん「はい、説明用の文字列を渡すとデバッグしやすくなります。」
ずんだもん「でもその説明文は値に影響しないのがポイントだね。」
四国めたん「コールごとに必ず新しいSymbolが返ります。」
ずんだもん「DIトークンもfactoryパターンで気軽に作れるよ。」
四国めたん「型注釈を付ければsymbol型として扱えます。」
ずんだもん「記法をしっかり押さえて安全に使おう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 関数として呼び出す */
const featureFlag: symbol = Symbol("featureFlag");

/** Example 2: 説明文はデバッグ用 */
const sameLabel = Symbol("featureFlag");
console.log(featureFlag === sameLabel); // false, descは識別に使われない

/** Example 3: new Symbol()はエラー */
// const invalid = new (Symbol as any)("oops");
// TypeError: Symbol is not a constructor
```
