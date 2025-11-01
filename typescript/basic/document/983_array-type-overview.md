# #983 「配列型」

四国めたん「配列型はT[]やArray<T>で表現できると学びましたね。」
ずんだもん「ループでも要素型が推論されるから安心だよ。」
四国めたん「ジェネリック関数で配列を受け取るときはT[]を引数に取ります。」
ずんだもん「配列型を理解しておけばループ処理も型安全になるね。」
四国めたん「基礎を押さえて次の話題に進みましょう。」
ずんだもん「配列型の理解を深めてね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: ジェネリック */
function process<T>(items: T[]): void {
  items.forEach((item) => console.log(item));
}

/** Example 2: Array<T> */
const refs: Array<HTMLElement> = [];

/** Example 3: 要素型推論 */
const names = ["meta", "zunda"];
for (const name of names) {
  // name: string
}
```
