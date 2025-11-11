# #345 「オプショナル引数」

四国めたん「オプショナル引数について学びましょう!」
ずんだもん「引数名の後に ? を付けるんだね!」
四国めたん「はい。その引数を省略可能にできます。」
ずんだもん「呼び出し時に省略できるの?」
四国めたん「その通りです。省略した場合、引数の値は undefined になります。」
ずんだもん「デフォルト値とも組み合わせられるんだね!」
四国めたん「はい。デフォルト値を設定すると、省略時に指定した値が使われます。」
ずんだもん「オプショナル引数で、柔軟な関数を作るのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: オプショナル引数の基本 */
function greet(name: string, age?: number) {
  if (age !== undefined) {
    console.log(`${name} is ${age} years old`);
  } else {
    console.log(`Hello, ${name}`);
  }
}

/** Example 2: 呼び出し時の省略 */
greet("Alice", 30);  // 引数2つ
greet("Bob");        // ageは省略

/** Example 3: デフォルト値との組み合わせ */
function createUser(name: string, role: string = "user") {
  return { name, role };
}
```
