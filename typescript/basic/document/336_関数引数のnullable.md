# #336 「関数引数のnullable」

四国めたん「関数引数のnullableについて学びましょう!」
ずんだもん「関数の引数にnullable型を使えるんだね!」
四国めたん「はい。User | null 型の引数で、nullを受け取れる関数を定義できます。」
ずんだもん「オプショナル引数とは違うの?」
四国めたん「その通りです。nullable引数は明示的にnullを渡す必要があります。」
ずんだもん「デフォルト値も組み合わせられるんだね!」
四国めたん「はい。引数にnullのデフォルト値を指定できます。」
ずんだもん「nullable引数で、柔軟な関数を作れるのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: nullable引数 */
function greet(user: User | null): string {
  if (user === null) {
    return "Hello, Guest";
  }
  return `Hello, ${user.name}`;
}

/** Example 2: オプショナルとの違い */
function process1(data: string | null) {
  // nullを明示的に渡す必要あり
}
function process2(data?: string) {
  // 省略可能
}

/** Example 3: デフォルト値との組み合わせ */
function log(message: string | null = null) {
  console.log(message ?? "No message");
}
```
