# #758 「グローバルシンボルの用途」

四国めたん「グローバルシンボルは複数モジュールの橋渡しに向いています。」
ずんだもん「ブラウザ拡張やプラグインが同じページで協調するときに便利だね。」
四国めたん「SSRとCSRで識別子を共有して状態を復元する用途も一般的です。」
ずんだもん「監視コードがアプリの内部状態を読むときもkey衝突を防げるよ。」
四国めたん「ライブラリが公開するプロトコルキーとしても使えます。」
ずんだもん「globalThisにぶら下げるときはSymbol.forが安心だね。」
四国めたん「用途を理解して適材適所で選択しましょう。」
ずんだもん「共有が必要な場面でグローバルシンボルを取り入れよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: SSRデータ共有 */
const STATE_KEY = Symbol.for("app:ssr-state");
(globalThis as any)[STATE_KEY] = { loggedIn: true };

/** Example 2: 監視ツールとの連携 */
const INSPECTOR_KEY = Symbol.for("inspector:hooks");
(globalThis as any)[INSPECTOR_KEY] = () => console.log("inspected");

/** Example 3: プラグインプロトコル */
const EXTENSION_PROTOCOL = Symbol.for("my-extension:protocol");
const extensions = new Map<symbol, unknown>([[EXTENSION_PROTOCOL, { version: 1 }]]);
```
