# #660 「any型は伝播する」

四国めたん「anyが一箇所にあると推論を通じて伝播していきます」
ずんだもん「関数の戻り値がanyになると、それを受け取る側もanyになるんだよね」
四国めたん「はい。型安全な境界を越えてバグが広がる可能性があります」
ずんだもん「早いうちにunknownや正確な型に変換しないと被害が拡大するよ」
四国めたん「伝播を防ぐためにany源泉を特定して潰しましょう」
ずんだもん「型負債のスパイラルを止めよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: anyの源泉 */
function getConfig(): any {
  return JSON.parse("{}");
}

/** Example 2: 伝播 */
const config = getConfig();
config.value.trim(); // configがany

/** Example 3: unknownで遮断 */
function getConfigSafe(): unknown {
  return JSON.parse("{}");
}
```
