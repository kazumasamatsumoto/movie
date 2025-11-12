# #376 「undefinedとの違い」

四国めたん「voidとundefinedの違いを整理しましょう。」
ずんだもん「voidは戻り値を無視する型で、undefinedは実際の値なんだね?」
四国めたん「はい。logMessageのresult1はvoidで、扱う価値がないことを示します。」
ずんだもん「findItemだとItem | undefinedになって、結果があるかチェックする必要がある?」
四国めたん「その通り。戻り値を使うのでundefinedとのUnionになります。」
ずんだもん「使い分けではLoggerとFinderみたいに役割で区別するんだね。」
四国めたん「副作用中心ならvoid、データ検索ならundefinedを含む戻り値にします。」
ずんだもん「用語を混同せずに意味を意識するのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: void: 戻り値を無視 */
function logMessage(msg: string): void {
  console.log(msg);
}
const result1 = logMessage("Hello");  // void型

/** Example 2: undefined: 値として返す */
function findItem(id: number): Item | undefined {
  return items.find(item => item.id === id);
}
const result2 = findItem(1);  // Item | undefined型

/** Example 3: 使い分け */
type Logger = (msg: string) => void;      // 副作用
type Finder = (id: number) => Item | undefined;  // 検索
```
