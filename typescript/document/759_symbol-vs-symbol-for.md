# #759 「Symbol()との使い分け」

四国めたん「ローカル専用ならSymbol()、共有したいならSymbol.forを使いましょう。」
ずんだもん「スコープを跨がないメタデータはSymbol()で十分だよね。」
四国めたん「グローバル共有すると管理コストが増えるので必要なときだけにします。」
ずんだもん「外部プラグインに公開する場合はSymbol.forでキーを固定しよう。」
四国めたん「セキュリティと可視性のバランスが重要です。」
ずんだもん「使い分けを意識すると設計がスッキリするよ。」
四国めたん「要件に合わせて適切なAPIを選びましょう。」
ずんだもん「Symbolファミリーの得意分野を活かそう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: ローカルシンボル */
const internalKey = Symbol("internal");
const component = { [internalKey]: "secret" };

/** Example 2: 共有シンボル */
const sharedKey = Symbol.for("plugin:bridge");
(globalThis as any)[sharedKey] = { hook: () => console.log("hook") };

/** Example 3: 選択関数 */
function createKey(shared: boolean, name: string) {
  return shared ? Symbol.for(name) : Symbol(name);
}
const local = createKey(false, "local");
const global = createKey(true, "global");
```
