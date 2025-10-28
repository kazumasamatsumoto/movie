# #939 「オプショナルチェーン」

四国めたん「Optionalチェーンを使うと配列アクセスの安全性が高まります。」
ずんだもん「arr?.[index] って書くやつだね。」
四国めたん「配列自体がundefinedかもしれない場合に便利です。」
ずんだもん「戻り値は要素型 | undefinedになるからNullish Coalescingと相性がいいよ。」
四国めたん「Optionalチェーンでネストした配列も安全にアクセスしましょう。」
ずんだもん「短く書けて安心だね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 配列がundefinedかも */
const list: string[] | undefined = fetchList();
const first = list?.[0];

/** Example 2: ネスト */
const matrix: number[][] | undefined = loadMatrix();
const cell = matrix?.[1]?.[2];

/** Example 3: 関数 */
function getFirst<T>(items?: T[]): T | undefined {
  return items?.[0];
}
```
