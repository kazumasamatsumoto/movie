# #601 「any型の基本」

四国めたん「TypeScriptのany型は型チェックをスキップする特別な型です」
ずんだもん「JavaScriptそのものを受け入れる感じだね」
四国めたん「はい。どんな値でも代入でき、操作も自由に許可されます」
ずんだもん「便利だけど型安全性は一気に下がるよ」
四国めたん「使う前に目的とリスクを理解しておくことが大切です」
ずんだもん「まずは特徴を押さえてから安全な代替も考えよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: anyは何でも許可 */
let value: any = "text";
value = 123;
value.nonExist(); // runtimeまで検出されない

/** Example 2: any関数 */
function handle(input: any) {
  return input * 2; // 実行時に不正な型でも通る
}

/** Example 3: 型チェック無し */
const result: number = value; // コンパイルは通る
```
