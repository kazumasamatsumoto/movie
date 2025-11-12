# #459 「ベストプラクティス」

四国めたん「void型の基本ベストプラクティスを押さえましょう。」
ずんだもん「logMessageやsaveDataのように型を明示するんだね。」
四国めたん「副作用と計算を分離し、小さなvoid関数に分割します。」
ずんだもん「processUserみたいに順番に副作用を実行するのもポイント!」
四国めたん「void関数は短く、目的がはっきりするように書きましょう。」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 明示的な型宣言 */
function logMessage(msg: string): void {
  console.log(msg);
}
async function saveData(data: Data): Promise<void> {
  await database.save(data);
}

/** Example 2: 副作用の分離 */
function calculateTotal(items: Item[]): number {
  return items.reduce((sum, item) => sum + item.price, 0);
}
function displayTotal(items: Item[]): void {
  const total = calculateTotal(items);
  console.log(`Total: ${total}`);
}

/** Example 3: 小さな関数 */
function processUser(user: User): void {
  validate(user);
  save(user);
  notify(user);
}
```
