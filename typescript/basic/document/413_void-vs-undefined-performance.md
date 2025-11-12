# #413 「パフォーマンス」

四国めたん「voidとundefinedに性能差はありません。」
ずんだもん「voidFuncとundefFuncのTypeScriptコードがあったね。」
四国めたん「はい。JavaScriptにするとどちらもほぼ同じです。」
ずんだもん「console.log(voidFunc()) も console.log(undefFunc()) もundefinedだった!」
四国めたん「その通り。型はコンパイルで消えるだけです。」
ずんだもん「だから意味の違いだけを気にすればいいんだね。」
四国めたん「はい。性能目的で型を選ぶ必要はありません。」
ずんだもん「意図ベースでvoid/undefinedを選ぶのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: TypeScriptコード */
function voidFunc(): void {
  console.log("void");
}
function undefFunc(): undefined {
  return undefined;
}

/** Example 2: JavaScriptコード */
function voidFunc() {
  console.log("void");
}
function undefFunc() {
  return undefined;
}

/** Example 3: 実行時の動作 */
console.log(voidFunc());
console.log(undefFunc());
```
