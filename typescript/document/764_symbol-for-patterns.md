# #764 「パターン」

四国めたん「Symbol.forの代表的なパターンを確認しましょう。」
ずんだもん「サービスロケータ、プラグインハンドシェイク、SSRハイドレーションだね。」
四国めたん「これらを押さえれば実務で迷いません。」
ずんだもん「キーの命名と共有方法をユーティリティ化するのがコツだよ。」
四国めたん「パターンを応用して自分のプロジェクトに合わせてください。」
ずんだもん「Symbol.forパターンで安全な拡張ポイントを作ろう！」
四国めたん「次はまとめで振り返ります。」
ずんだもん「パターンを引き出しに入れておこう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: サービスロケータ */
const SERVICE = Symbol.for("myapp:service");
const services = new Map<symbol, unknown>([[SERVICE, { ping: () => "pong" }]]);

/** Example 2: プラグインハンドシェイク */
const HANDSHAKE = Symbol.for("myapp:plugin-handshake");
(globalThis as any)[HANDSHAKE] = () => console.log("handshaked");

/** Example 3: SSRハイドレーション */
const HYDRATE = Symbol.for("myapp:hydrate");
(globalThis as any)[HYDRATE] = { theme: "dark" };
const initialState = (globalThis as any)[Symbol.for("myapp:hydrate")];
```
