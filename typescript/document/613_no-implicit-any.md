# #613 「noImplicitAnyの効果」

四国めたん「noImplicitAnyは暗黙anyを禁止する重要な設定です」
ずんだもん「引数や変数に型が無いとコンパイルが怒るんだよね」
四国めたん「はい。意図しないany混入を初期段階で止められます」
ずんだもん「型注釈を書く習慣が身につくのも良いところだよ」
四国めたん「strictを分解して使う場合も必ず有効化しましょう」
ずんだもん「まずはここからany撲滅を始めよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: tsconfig設定 */
{
  "compilerOptions": {
    "noImplicitAny": true
  }
}

/** Example 2: エラー例 */
function parse(value) {
  return JSON.parse(value); // ❌ 暗黙any
}

/** Example 3: 解決例 */
function parseSafe(value: string): unknown {
  return JSON.parse(value);
}
```
