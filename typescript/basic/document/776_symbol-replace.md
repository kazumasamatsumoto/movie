# #776 「Symbol.replace」

四国めたん「Symbol.replaceはString.prototype.replaceの処理を差し替えます。」
ずんだもん「置換ロジックを独自に定義できるんだね。」
四国めたん「(text, replacement) => stringのシグネチャです。」
ずんだもん「テンプレートの変数展開を自力で実装する時に使えそうだよ。」
四国めたん「正規表現以外の置換プラグインを作るときに役立ちます。」
ずんだもん「Symbol.replaceで柔軟な文字列処理を実現しよう！」
四国めたん「副作用を避けて純粋関数的に書くのがコツです。」
ずんだもん「挙動をテストで保証するのも忘れずに！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: カスタムreplace */
const envReplacer = {
  [Symbol.replace](text: string, env: Record<string, string>): string {
    return text.replace(/\$\{(\w+)\}/g, (_, key) => env[key] ?? "");
  },
};

/** Example 2: 使用例 */
const template = "Hello, ${name}!";
console.log(template.replace(envReplacer, { name: "TypeScript" }));

/** Example 3: 型安全なラッパー */
function render(text: string, env: Record<string, string>) {
  return text.replace(envReplacer, env);
}
console.log(render("Deploy ${app}", { app: "api" }));
```
