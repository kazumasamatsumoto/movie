# #415 「比較まとめ」

四国めたん「voidとundefinedを対比してまとめましょう。」
ずんだもん「logMessageは戻り値を無視する関数で、Logger型も副作用専用だね。」
四国めたん「はい。findItemはundefinedを返す代表です。」
ずんだもん「両方console.logするとundefinedだけど意味は違うんだ?」
四国めたん「その通り。voidは『無視する』、undefinedは『値がない』を表現します。」
ずんだもん「意図を理解して選ぶのが一番だね。」
四国めたん「まとめを活かして迷わず指定しましょう。」
ずんだもん「void/undefinedの比較ポイントを押さえるのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: voidの例 */
function logMessage(msg: string): void {
  console.log(msg);
}
type Logger = (msg: string) => void;

/** Example 2: undefinedの例 */
function findItem(id: number): Item | undefined {
  return items.find(item => item.id === id);
}

/** Example 3: 実行時の違い */
console.log(logMessage("test"));
console.log(findItem(1));
```
