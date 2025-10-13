# #802 「constアサーション」

四国めたん「オブジェクト内のシンボルをunique symbolとして固定するにはconstアサーションが便利です。」
ずんだもん「as constを付けると各プロパティがreadonlyでunique symbolのまま保持されるんだね。」
四国めたん「はい、推論がsymbolに広がるのを防げます。」
ずんだもん「トークン集約オブジェクトを作るときの定番テクだよ。」
四国めたん「型エイリアスと組み合わせて一覧を生成するのも簡単です。」
ずんだもん「constアサーションでunique symbolを安全に配布しよう！」
四国めたん「オブジェクトリテラルの設計に役立ててください。」
ずんだもん「推論を味方につけてメンテナンスを楽にしよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: constアサーション */
const TOKENS = {
  LOGGER: Symbol("LOGGER"),
  CONFIG: Symbol("CONFIG"),
} as const;

/** Example 2: 型生成 */
type LoggerToken = typeof TOKENS.LOGGER;
function inject(token: LoggerToken) {
  return token === TOKENS.LOGGER;
}

/** Example 3: 値の列挙 */
type TokenMap = typeof TOKENS;
type Tokens = TokenMap[keyof TokenMap];
const list: Tokens[] = [TOKENS.LOGGER, TOKENS.CONFIG];
```
