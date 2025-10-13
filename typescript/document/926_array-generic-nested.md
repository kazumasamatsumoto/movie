# #926 「Array<Array<number>>」

四国めたん「Array<Array<number>>はジェネリクス版の二次元配列です。」
ずんだもん「number[][]と同じ意味だけど、<>で包んでいるんだね。」
四国めたん「はい、ジェネリックを多用するコードベースでは統一感があります。」
ずんだもん「型ツリーを見たときに構造が明瞭になるのも利点だよ。」
四国めたん「どちらの記法でも同じ型として扱われるので好みで選びましょう。」
ずんだもん「Array<Array<number>>の読み方も慣れておこう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 宣言 */
const board: Array<Array<number>> = [[0, 1], [2, 3]];

/** Example 2: map */
const doubled = board.map((row) => row.map((cell) => cell * 2));

/** Example 3: 関数引数 */
function printGrid(grid: Array<Array<number>>) {
  grid.forEach((row) => console.log(row.join(",")));
}
```
