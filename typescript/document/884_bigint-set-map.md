# #884 「Set/Map」

四国めたん「BigIntはSetやMapのキーとしてそのまま使えます。」
ずんだもん「同じ値のBigIntなら同一キーとして扱われるんだね。」
四国めたん「はい、Mapではnew Map([[1n, "a"]])のように定義できます。」
ずんだもん「JSONシリアライズ時には別途変換が必要だから注意してね。」
四国めたん「Set/Mapを使う場合は型注釈でbigintを明示すると読みやすくなります。」
ずんだもん「大きなIDコレクションも安全に管理できるよ。」
四国めたん「キー比較は===なので同じ値なら一致します。」
ずんだもん「Set/MapでBigIntを効率的に活用しよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: Map */
const registry = new Map<bigint, string>();
registry.set(1n, "alice");

/** Example 2: Set */
const ids = new Set<bigint>([1n, 2n, 1n]);

/** Example 3: JSON変換 */
const serialized = Array.from(registry.entries()).map(([k, v]) => ({ key: k.toString(), value: v }));
```
