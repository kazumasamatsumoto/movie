# #761 「名前空間」

四国めたん「グローバルシンボルはキーを名前空間化して衝突を防ぎます。」
ずんだもん「例えば"app:module:token"みたいにコロンで区切るんだね。」
四国めたん「プロジェクト名や組織名を接頭辞にするとより安全です。」
ずんだもん「ユーティリティで名前空間を自動付与すると運用が楽になるよ。」
四国めたん「命名規約をドキュメント化して共有しましょう。」
ずんだもん「名前空間があれば第三者ライブラリとも共存できるね。」
四国めたん「Symbol.forの強みを引き出すための工夫です。」
ずんだもん「名前空間付きキーで管理を整えよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 名前空間付きキー生成 */
const createNamespacedKey = (scope: string, name: string) => Symbol.for(`${scope}:${name}`);
const TOKEN = createNamespacedKey("app.config", "http");

/** Example 2: 組織名を付与 */
const ORG = "example.com";
const DI_KEY = Symbol.for(`${ORG}:nest:Logger`);

/** Example 3: スキーマで正規化 */
function ensureKey(key: string) {
  if (!/^[\w.-]+:[\w.-]+/.test(key)) {
    throw new Error("invalid global symbol key");
  }
  return Symbol.for(key);
}
const validated = ensureKey("app.service:User");
```
