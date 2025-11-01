# #803 「使用場面」

四国めたん「unique symbolはトークンや判別プロパティのような一意識別子に最適です。」
ずんだもん「AngularのInjectionTokenみたいな仕組みを自作するとき便利だね。」
四国めたん「型レベルで同一性が保証されるので安全です。」
ずんだもん「イベント種別や状態マシンの識別子としても使えるよ。」
四国めたん「外部公開したくない内部識別子にも向いています。」
ずんだもん「使用場面を理解して設計に取り入れよう！」
四国めたん「unique symbolで設計の意図を型に落とし込みましょう。」
ずんだもん「ユニークキーで安心なアーキテクチャを作ってね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: DIトークン */
const SERVICE_TOKEN = Symbol("Service");
type ServiceToken = typeof SERVICE_TOKEN;

/** Example 2: 状態マシン */
const STATE_IDLE = Symbol("idle");
const STATE_BUSY = Symbol("busy");
type State = typeof STATE_IDLE | typeof STATE_BUSY;

/** Example 3: イベント種別 */
const EVENT_READY = Symbol("ready");
const EVENT_ERROR = Symbol("error");
type Event = { type: typeof EVENT_READY } | { type: typeof EVENT_ERROR; message: string };
```
