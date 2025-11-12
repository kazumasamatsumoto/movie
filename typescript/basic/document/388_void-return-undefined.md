# #388 「return undefined」

四国めたん「void関数ではreturn undefined; が許可されています。」
ずんだもん「log1のように書いてもエラーにならないんだね。」
四国めたん「はい。ただしlog2やlog3のようにreturn; かreturn無しの方が簡潔です。」
ずんだもん「早期リターンでif (!value) return; と書くのも推奨なんだ?」
四国めたん「その通り。validateで見せたように条件分岐を終了させられます。」
ずんだもん「undefinedを返す場合とreturn;を使う場合を使い分けたいね。」
四国めたん「規約に従って選べばどちらも問題ありません。」
ずんだもん「void関数のreturnスタイルを理解するのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: return undefined */
function log1(msg: string): void {
  console.log(msg);
  return undefined;
}

/** Example 2: 推奨スタイル */
function log2(msg: string): void {
  console.log(msg);
  return;
}
function log3(msg: string): void {
  console.log(msg);
}

/** Example 3: 早期リターン */
function validate(value: string): void {
  if (!value) return;
  console.log(value);
}
```
