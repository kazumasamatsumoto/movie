# #748 「実践例」

四国めたん「シンボルを使ったサービスレジストリを例に見ましょう。」
ずんだもん「モジュールごとに独立したキーで登録すれば衝突しないね。」
四国めたん「状態機械の内部フラグにもsymbolが使えます。」
ずんだもん「Reduxのアクションタイプをシンボルにする手法もあるよ。」
四国めたん「実践例を通してイメージを固めましょう。」
ずんだもん「コードで確認すると使い方がすぐ理解できるね。」
四国めたん「応用の幅を広げてプロジェクトに取り入れてください。」
ずんだもん「symbol活用術を現場で試そう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: サービスレジストリ */
const PAYMENT_SERVICE = Symbol("PAYMENT_SERVICE");
const registry = new Map<symbol, unknown>();
registry.set(PAYMENT_SERVICE, { charge: () => console.log("charge") });

/** Example 2: 状態機械のフラグ */
const STATE_IDLE = Symbol("idle");
const STATE_BUSY = Symbol("busy");
let state = STATE_IDLE;
state = STATE_BUSY;

/** Example 3: Redux風アクション */
const ACTION_LOGIN = Symbol("LOGIN");
type Action = { type: typeof ACTION_LOGIN; payload: string };
const action: Action = { type: ACTION_LOGIN, payload: "user" };
```
