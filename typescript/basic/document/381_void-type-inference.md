# #381 「型推論」

四国めたん「void型は多くの場合、戻り値から自動で推論されます。」
ずんだもん「function log1(msg: string) と書いてもvoidになるの?」
四国めたん「はい。returnが無ければコンパイラがvoidだと判断します。」
ずんだもん「でも明示的に: void と書いた方が意図が伝わる場面もあるよね?」
四国めたん「log2のように公開APIでは型注釈しておくと読み手が安心します。」
ずんだもん「アロー関数でも(e: Event) => { ... } と書くだけで => void を推論してくれる?」
四国めたん「その通り。handlerのように何も返さなければ自動的に(Event) => voidになります。」
ずんだもん「推論と明示を使い分けてvoid型を扱うのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 推論されるvoid */
function log1(msg: string) {
  console.log(msg);
  // 戻り値型: void (推論)
}

/** Example 2: 明示的なvoid */
function log2(msg: string): void {
  console.log(msg);
  // 意図が明確
}

/** Example 3: 推論の活用 */
const handler = (e: Event) => {
  console.log(e);
};  // (e: Event) => void と推論
```
