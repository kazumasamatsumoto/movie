# #912 「Array<T>記法」

四国めたん「配列型はArray<T>というジェネリクス記法で表せます。」
ずんだもん「Array<number>みたいに書くやつだね。」
四国めたん「ReactのJSXと衝突しないので.tsxでも安心です。」
ずんだもん「ジェネリクスに慣れている人には読みやすい記法だよ。」
四国めたん「ネストした配列でもArray<Array<number>>のように書けます。」
ずんだもん「Array<T>記法を押さえておこう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: Array<number> */
const values: Array<number> = [1, 2, 3];

/** Example 2: Array<string> */
const routes: Array<string> = ["/", "/dashboard"]; // JSXと衝突しない

/** Example 3: ネスト */
const matrix: Array<Array<number>> = [[1, 2], [3, 4]];
```
