# #799 「実践パターン(2)」

四国めたん「別のパターンとしてデータキャッシュにsymbolを使う例を見ます。」
ずんだもん「外部ライブラリが触るオブジェクトに内部キャッシュを載せるんだね。」
四国めたん「WeakMapの代わりにシンボルキーでメモ化する手法です。」
ずんだもん「シリアライズ不要な軽量データに向いているよ。」
四国めたん「型定義しておくとIDE補完も機能します。」
ずんだもん「symbolを使ったキャッシュパターンを覚えてパフォーマンスを上げよう！」
四国めたん「状況に応じてWeakMapと使い分けてください。」
ずんだもん「実装の引き出しを増やしてね！」

---

## 📺 画面表示用コード

```typescript
/** キャッシュキー */
const CACHE_KEY = Symbol("cache");

interface Cacheable {
  [CACHE_KEY]?: Map<string, unknown>;
}

function getCache(target: Cacheable): Map<string, unknown> {
  if (!target[CACHE_KEY]) {
    target[CACHE_KEY] = new Map();
  }
  return target[CACHE_KEY]!;
}

const adapter: Cacheable = {};
getCache(adapter).set("result", 42);
console.log(getCache(adapter).get("result"));
```
