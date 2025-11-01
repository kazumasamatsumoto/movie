# #937 「安全なアクセスパターン」

四国めたん「配列の安全なアクセスにはいくつかのパターンがあります。」
ずんだもん「lengthチェック、atメソッド、Optionalチェーンなどだね。」
四国めたん「ガード節を使ってundefinedを扱うパターンも重要です。」
ずんだもん「安全なアクセスパターンを使うと実行時エラーを防げるよ。」
四国めたん「ユーティリティ関数にまとめて再利用するのもおすすめです。」
ずんだもん「安全なアクセスを徹底しよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: lengthチェック */
function firstSafe<T>(items: T[]): T | undefined {
  return items.length ? items[0] : undefined;
}

/** Example 2: at */
const first = [1, 2, 3].at(0);

/** Example 3: ユーティリティ */
function getOr<T>(items: T[], index: number, fallback: T): T {
  return items[index] ?? fallback;
}
```
