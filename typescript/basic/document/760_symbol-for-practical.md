# #760 「実例」

四国めたん「Symbol.forの実例としてロギング拡張を共有するコードを見ましょう。」
ずんだもん「アプリ側がフックを公開して、デバッグツールが同じキーで取得するんだね。」
四国めたん「SSRで埋め込んだデータをクライアントで読む場合にも使えます。」
ずんだもん「キーが一致すれば安全に受け渡しできるよ。」
四国めたん「練習としてState Hydrationパターンを試してみてください。」
ずんだもん「Symbol.forで実践パターンを身につけよう！」
四国めたん「実例を通して使いどころを体感しましょう。」
ずんだもん「共有トークンの便利さがわかるはずだよ！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: ログフック共有 */
const LOG_HOOK = Symbol.for("debug:log");
(globalThis as any)[LOG_HOOK] = (message: string) => console.debug("hook", message);
const hook = (globalThis as any)[Symbol.for("debug:log")];
hook?.("connected");

/** Example 2: SSRハイドレーション */
const HYDRATE_KEY = Symbol.for("hydrate:data");
(globalThis as any)[HYDRATE_KEY] = { user: "kazu" };
const hydrated = (globalThis as any)[Symbol.for("hydrate:data")];

/** Example 3: CLIプラグイン共有 */
const CLI_PLUGIN = Symbol.for("cli:plugin");
const plugins = new Map<symbol, string>([[CLI_PLUGIN, "v1"]]);
console.log(plugins.get(Symbol.for("cli:plugin"))); // "v1"
```
