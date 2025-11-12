# #414 「コンパイル結果」

四国めたん「TypeScriptのvoidやundefined注釈はコンパイルで消えます。」
ずんだもん「f1(): void も JavaScriptではただの function f1() になるんだね。」
四国めたん「はい。型情報は全て削除されます。」
ずんだもん「f2(): undefined も return undefined; だけが残る?」
四国めたん「その通り。実行時はJavaScriptの挙動に従います。」
ずんだもん「コメントにもTypeScriptの宣言だけが載ってたね。」
四国めたん「コンパイル後のコードを意識すればデバッグしやすくなります。」
ずんだもん「型は設計情報だと理解しておくのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: TypeScript */
function f1(): void {
  console.log("void");
}
function f2(): undefined {
  return undefined;
}

/** Example 2: JavaScript */
function f1() {
  console.log("void");
}
function f2() {
  return undefined;
}

/** Example 3: 型情報は削除 */
// TypeScript: function log(msg: string): void
// JavaScript: function log(msg)
```
