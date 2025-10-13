# #809 「ベストプラクティス」

四国めたん「unique symbolは単一の定義ファイルで集中管理しましょう。」
ずんだもん「トークンを再定義すると型が一致しなくなるから要注意だね。」
四国めたん「constアサーションで一覧化し、型を再利用するのが王道です。」
ずんだもん「公開APIには型エイリアスを通じて渡すと安全だよ。」
四国めたん「neverを使った網羅チェックで判別ユニオンを検証しましょう。」
ずんだもん「ベストプラクティスを守ってunique symbolを安心運用しよう！」
四国めたん「ドキュメントとテストをセットで準備してください。」
ずんだもん「チーム全体でルール化しようね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: トークン集中管理 */
export const TOKENS = {
  LOGGER: Symbol("LOGGER"),
  METRICS: Symbol("METRICS"),
} as const;
export type Token = typeof TOKENS[keyof typeof TOKENS];

/** Example 2: エクスポート用型 */
export type LoggerToken = typeof TOKENS.LOGGER;

/** Example 3: neverチェック */
type Command = { kind: typeof TOKENS.LOGGER } | { kind: typeof TOKENS.METRICS };
function exhaustivenessCheck(value: never): never {
  throw new Error(`Unhandled case: ${value}`);
}
function handle(command: Command) {
  switch (command.kind) {
    case TOKENS.LOGGER:
      return;
    case TOKENS.METRICS:
      return;
    default:
      exhaustivenessCheck(command);
  }
}
```
