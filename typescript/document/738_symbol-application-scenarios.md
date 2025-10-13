# #738 「使用場面」

四国めたん「Symbolはフレームワーク内部のメタデータ管理に向いています。」
ずんだもん「AngularのDIトークンやNest.jsのカスタムキーでも活躍するよ。」
四国めたん「オブジェクトに隠しプロパティを追加するときも便利です。」
ずんだもん「ユニークイベント名を作ったり、プラグイン間の衝突を避けたりできるね。」
四国めたん「ロギング用の識別子としても安全に扱えます。」
ずんだもん「分散チームでモジュール拡張するときの衝突対策にちょうどいいよ。」
四国めたん「ユースケースを把握して設計に組み込みましょう。」
ずんだもん「シンボルで安全な拡張ポイントを用意しよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 隠しメタデータ */
const metaKey = Symbol("meta");
const service = { name: "PaymentService", [metaKey]: { retry: 3 } };
console.log(Object.keys(service)); // ["name"]: メタデータは列挙されない

/** Example 2: イベントレジストリ */
const onConnect = Symbol("onConnect");
const onDisconnect = Symbol("onDisconnect");
const handlers: Record<symbol, () => void> = {
  [onConnect]: () => console.log("connect"),
  [onDisconnect]: () => console.log("disconnect"),
};

/** Example 3: DIトークン */
const LOGGER_TOKEN = Symbol("LOGGER");
const container = new Map<symbol, unknown>([[LOGGER_TOKEN, console]]);
const logger = container.get(LOGGER_TOKEN) as Console;
logger.log("resolved");
```
