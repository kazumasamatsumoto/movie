# #798 「実践パターン(1)」

四国めたん「シンボルキーを使ったDIレジストリのパターンを紹介します。」
ずんだもん「オブジェクトにシンボルキーで依存性を登録するんだね。」
四国めたん「はい、文字列キーと衝突せずにサービスを保持できます。」
ずんだもん「Angularのプロバイダ表現にも似ていて分かりやすいよ。」
四国めたん「TypeScriptの型でTokenと実装を結び付けるのがポイントです。」
ずんだもん「このパターンでモジュール間の依存を安全に扱おう！」
四国めたん「次回は別の実践パターンを見ていきます。」
ずんだもん「シンボルを活かした設計を体験してね！」

---

## 📺 画面表示用コード

```typescript
/** Token定義 */
const LOGGER_TOKEN = Symbol("Logger");
const CONFIG_TOKEN = Symbol("Config");

type TokenMap = {
  [LOGGER_TOKEN]: Console;
  [CONFIG_TOKEN]: { endpoint: string };
};

/** レジストリ */
const registry: { [K in keyof TokenMap]?: TokenMap[K] } = {
  [LOGGER_TOKEN]: console,
  [CONFIG_TOKEN]: { endpoint: "/api" },
};

/** 解決 */
function resolve<K extends keyof TokenMap>(token: K): TokenMap[K] {
  return registry[token]!;
}
console.log(resolve(LOGGER_TOKEN).log("ready"));
```
