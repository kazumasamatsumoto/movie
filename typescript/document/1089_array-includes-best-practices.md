# #1089 「ベストプラクティス」

四国めたん「includesを使うときのベストプラクティスをまとめましょう。」
ずんだもん「boolean戻り値を変数に格納して意味づけする、NaNを含むか確認するときに活用、位置が必要ならindexOfを検討、だったね。」
四国めたん「はい、配列が大きい場合はSetへの変換も検討します。」
ずんだもん「読みやすさと性能を意識して使い分けよう。」
四国めたん「ベストプラクティスを守って存在チェックを安全に行ってください。」
ずんだもん「意図が伝わるコードにしよう！」

---

## 📺 画面表示用コード

```typescript
const values = ["meta", "zunda"];

const hasMeta = values.includes("meta");
const hasLegacy = values.includes("legacy");

const message = hasLegacy ? "legacy found" : "clean";

const valuesSet = new Set(values);
const hasFastLookup = valuesSet.has("zunda");
```
