# #697 「JavaScript移行期のany許容」

四国めたん「JavaScriptからTypeScriptへ移行する初期段階ではanyを使う場面があります」
ずんだもん「まだ型整備が追いついてない時期に一旦anyで受けるんだよね」
四国めたん「はい。ただしファイル単位でstrictを徐々に有効化する計画を立てます」
ずんだもん「タイムラインを決めて移行を前進させよう」
四国めたん「移行期のanyも期限とスコープを明確にするのが大切です」
ずんだもん「JSからTSへのソフトランディングを狙おう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: ts-checkコメント */
// @ts-check
/**
 * @param {any} data
 */
function handle(data) {
  return data;
}

/** Example 2: gradual tsconfig */
{
  "compilerOptions": { "allowJs": true, "checkJs": false }
}

/** Example 3: 移行ボード */
const migrationBoard = [
  { file: "src/legacy.js", status: "TS化予定" },
] as const;
```
