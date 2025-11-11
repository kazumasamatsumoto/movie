# #262 「null/undefinedチェック」

四国めたん「null/undefinedチェックについて学びましょう!」
ずんだもん「厳密にチェックする方法を知りたいな!」
四国めたん「はい。===を使って個別にチェックするのが基本です。」
ずんだもん「nullとundefinedを別々に判定するんだね!」
四国めたん「その通りです。それぞれ異なる意味を持つので区別が重要です。」
ずんだもん「両方をまとめてチェックする方法もある?」
四国めたん「はい。!= nullを使えば、nullとundefinedの両方を除外できます。」
ずんだもん「状況に応じて使い分けるのが大事なのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 厳密なチェック */
function process(value: string | null | undefined) {
  if (value === null) {
    console.log('null');
  } else if (value === undefined) {
    console.log('undefined');
  } else {
    console.log(value.toUpperCase());
  }
}

/** Example 2: 両方をチェック */
function handle(value: string | null | undefined) {
  if (value != null) {
    // nullでもundefinedでもない
    console.log(value.toUpperCase());
  }
}
```
