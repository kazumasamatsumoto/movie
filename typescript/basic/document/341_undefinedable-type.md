# #341 「undefinedable型 - T | undefined」

四国めたん「undefinedable型について学びましょう!」
ずんだもん「T | undefined で、undefinedを許容する型を作れるんだね!」
四国めたん「はい。値が存在しないケースを明示的に表現できます。」
ずんだもん「オプショナルプロパティとの関係は?」
四国めたん「その通りです。プロパティ?: Tは、プロパティ: T | undefinedと同じ意味になります。」
ずんだもん「関数の引数でも使えるの?」
四国めたん「はい。undefined チェックを行うことで、安全に値を扱えます。」
ずんだもん「undefinedable型で、値の不在を明示的に扱うのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: undefinedable型の基本 */
type Undefinedable<T> = T | undefined;
let name: string | undefined;
name = "Alice";
name = undefined;

/** Example 2: 関数引数での利用 */
function greet(name: string | undefined) {
  if (name !== undefined) {
    console.log(`Hello, ${name}`);
  }
}

/** Example 3: オプショナルとの関係 */
interface User {
  name: string;
  age: number | undefined;  // 明示的undefinedable
  email?: string;           // オプショナル(= string | undefined)
}
```
