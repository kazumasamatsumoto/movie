# #452 「間違い(2) - undefined混同」

四国めたん「voidとundefinedを混同するのもありがちな失敗です。」
ずんだもん「getValue(): void なのにreturn undefined;って書くとおかしくなる?」
四国めたん「はい。undefined値を返したいなら型をItem | undefinedのように定義します。」
ずんだもん「voidは副作用、undefinedは値として扱うって覚えておく!」
四国めたん「用途を分けると呼び出し側のコードが安全になります。」
ずんだもん「混同せずに書くのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 間違い: voidとundefined混同 */
function getValue(): void {
  return undefined;
}
const value = getValue();

/** Example 2: 正しい: undefinedを返す */
function findItem(id: number): Item | undefined {
  return items.find(item => item.id === id);
}
const item = findItem(1);
if (item !== undefined) {
  console.log(item.name);
}

/** Example 3: 正しい: voidは副作用 */
function logMessage(msg: string): void {
  console.log(msg);
}
logMessage("Hello");
```
