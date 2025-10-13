# #902 「実践例(1)」

四国めたん「実践例として分散IDとAPIレスポンスの組み合わせを見ましょう。」
ずんだもん「サーバーでBigInt IDを生成してJSONで文字列化、クライアントで復元する流れだね。」
四国めたん「はい、TypeScriptで型をつなげて安全に扱います。」
ずんだもん「BigInt Transportユーティリティを挟むと実装が楽になるよ。」
四国めたん「このパターンで精度を保ったままIDを往復できます。」
ずんだもん「実践でBigIntの威力を体験してね！」
四国めたん「API契約と型定義を連携させるのがポイントです。」
ずんだもん「バックエンドとフロントが一致して動くよ！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: サーバー */
const ID_EPOCH = 1_600_000_000_000n;
function createId(timestamp = Date.now()) {
  return ((BigInt(timestamp) - ID_EPOCH) << 12n) | BigInt(Math.floor(Math.random() * 4096));
}

function toJson(id: bigint) {
  return { id: id.toString() };
}

/** Example 2: クライアント */
function parseId(payload: { id: string }) {
  return BigInt(payload.id);
}

/** Example 3: end-to-end */
const response = toJson(createId());
const restored = parseId(response);
```
