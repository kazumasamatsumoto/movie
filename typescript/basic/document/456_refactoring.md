# #456 「リファクタリング」

四国めたん「void関数をリファクタリングするときは責務を分割しましょう。」
ずんだもん「calculateとdisplayを分ける例があったね。」
四国めたん「大きな副作用関数を小さなvoid関数のチェーンにするとテストしやすいです。」
ずんだもん「中でreturn値に頼っていないか確認するのも大事!」
四国めたん「責務ごとに命名されたvoid関数は読みやすさを大幅に上げます。」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 責務分割 */
function calculateTotal(items: Item[]): number {
  return items.reduce((sum, item) => sum + item.price, 0);
}
function displayTotal(items: Item[]): void {
  const total = calculateTotal(items);
  console.log(`Total: ${total}`);
}

/** Example 2: 小さなvoid関数 */
function validate(user: User): void {
  // ...
}
function save(user: User): void {
  // ...
}
function processUser(user: User): void {
  validate(user);
  save(user);
}

/** Example 3: return依存を排除 */
function process(): void {
  step1();
  step2();
}
```
