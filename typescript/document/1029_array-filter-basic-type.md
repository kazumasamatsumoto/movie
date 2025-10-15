# #1029 「基本的な型」

四国めたん「filterの戻り値は元の配列と同じ要素型Tの配列です。」
ずんだもん「number[]をfilterするとnumber[]が返るんだね。」
四国めたん「はい、ただし型述語を使わない限り要素型は変わりません。」
ずんだもん「基本形を覚えておけば挙動が予測しやすいよ。」
四国めたん「基本型を理解した上で型述語に進みましょう。」
ずんだもん「まずは基礎固めから！」

---

## 📺 画面表示用コード

```typescript
const numbers = [1, 2, 3, 4];

/** Example 1: しきい値 */
const large = numbers.filter((value) => value > 2); // number[]

/** Example 2: 偶数 */
const evens = numbers.filter((value) => value % 2 === 0); // number[]

/** Example 3: 文字列配列 */
const tags = ["ts", "js", ""];
const nonEmptyTags = tags.filter((tag) => tag.length > 0); // string[]
```
