# #386 「戻り値なし関数」

四国めたん「戻り値がない関数の特徴を整理しましょう。」
ずんだもん「greetはreturn文がなくてvoid扱いなんだね。」
四国めたん「はい。呼び出し結果をresultに代入するとundefinedになります。」
ずんだもん「updateCounterみたいに副作用だけする関数もvoidにするの?」
四国めたん「その通り。状態を更新してrenderするだけなので戻り値は不要です。」
ずんだもん「実行時にundefinedが返るって分かっていれば安心だ!」
四国めたん「コンパイラ上はvoid、ランタイムではundefinedという点を覚えておきましょう。」
ずんだもん「挙動を理解してvoid関数を書き切るのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 戻り値なし関数 */
function greet(name: string): void {
  console.log(`Hello, ${name}`);
}

/** Example 2: 実行時はundefined */
const result = greet("Alice");
console.log(result);  // undefined

/** Example 3: 副作用のための関数 */
function updateCounter(): void {
  counter++;
  render();
}
```
