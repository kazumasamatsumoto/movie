# #703 「動的な性質が強いコードでのany」

四国めたん「メタプログラミングやpluginシステムのように動的性質が強いコードではanyを検討することがあります」
ずんだもん「型がランタイムまで決まらないケースだね」
四国めたん「はい。その場合でもunknownに変換して型ガードや型述語を提供できないか検討しましょう」
ずんだもん「どうしても難しいときだけanyを許容する設定をドキュメント化しておきたいよ」
四国めたん「動的コードの自由度と型安全のバランスを見極めるのがポイントです」
ずんだもん「設計段階で型情報を渡せないかも再検討しよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: プラグインマネージャ */
type Plugin = (context: unknown) => unknown;
const registry: Record<string, Plugin> = {};

/** Example 2: どうしてもanyが必要な箇所 */
/* eslint-disable @typescript-eslint/no-explicit-any -- dynamic plugin hooks */
export function register(name: string, plugin: (...args: any[]) => any) {
  registry[name] = (...args) => plugin(...args);
}

/** Example 3: ランタイム検証 */
export function run(name: string, payload: unknown) {
  const plugin = registry[name];
  if (!plugin) throw new Error("plugin not found");
  return plugin(payload);
}
```
