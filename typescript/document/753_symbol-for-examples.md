# #753 「使用例」

四国めたん「Symbol.forはモジュールを跨いだトークン共有に便利です。」
ずんだもん「ブラウザの複数バンドル間で同じシンボルを使い回せるんだね。」
四国めたん「SSRとクライアントで識別子を一致させたいときにも活躍します。」
ずんだもん「グローバルストアのキーにして競合を防げるよ。」
四国めたん「使用例を把握して設計の選択肢を広げましょう。」
ずんだもん「Symbol.forの共有特性を味方にしてね！」
四国めたん「後でSymbol.keyForで逆引きもできます。」
ずんだもん「使いこなしてグローバルシンボルを活用しよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 共通トークン */
// module-a.ts
export const CONFIG_TOKEN = Symbol.for("app.config");
// module-b.ts
import { CONFIG_TOKEN } from "./module-a";
const container = new Map<symbol, unknown>([[CONFIG_TOKEN, { api: "/v1" }]]);

/** Example 2: SSRとクライアント */
const SSR_KEY = Symbol.for("ssr:data");
(globalThis as any)[SSR_KEY] = { user: "mzn" };

/** Example 3: グローバルストア */
const STORE_KEY = Symbol.for("store:session");
const globalStore = new Map<symbol, unknown>();
globalStore.set(STORE_KEY, { token: "abc" });
```
