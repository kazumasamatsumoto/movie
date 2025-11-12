# #354 「nullishチェック - x != null」

四国めたん「nullishチェックは value != null が便利です!」
ずんだもん「!= でnullとundefinedをまとめて判定できるんだね?」
四国めたん「はい。条件内ではvalueが確実に非nullishになります。」
ずんだもん「=== を二回書くよりずっと短い!」
四国めたん「しかも型ガードとして推論がstringやnumberに絞られます。」
ずんだもん「data != null の後なら安全に演算できるの?」
四国めたん「その通り。doubled = data * 2 のように型エラーが消えます。」
ずんだもん「簡潔なnullishチェックでロジックを守るのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 基本的なnullishチェック */
function process(value: string | null | undefined) {
  if (value != null) {
    // value: string
    console.log(value.toUpperCase());
  }
}

/** Example 2: 厳密等価との違い */
if (value !== null && value !== undefined) {
  // 冗長
}
if (value != null) {
  // 簡潔で推奨
}

/** Example 3: 型ガードとしての利用 */
const data: number | null | undefined = getData();
if (data != null) {
  const doubled = data * 2;  // number型として扱える
}
```
