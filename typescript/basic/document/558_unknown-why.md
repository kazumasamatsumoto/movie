# #558 「unknown導入の理由」

四国めたん「TypeScriptがunknownを導入したのは型安全性向上のためです」
ずんだもん「anyの乱用でバグが混ざるのを防ぎたかったんだね」
四国めたん「そうです。トップ型の柔軟さを保ちながら検証を強制できます」
ずんだもん「プロジェクトでもunknownを標準にすると安心だよ」
四国めたん「型解析ツールもunknown前提で最適化されています」
ずんだもん「型付け文化を守るための仕組みだね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 旧来のany対策 */
type ApiResponse = unknown;
function parseResponse(res: ApiResponse) {
  if (typeof res === "object") console.log(res);
}

/** Example 2: ESLintルール活用 */
// "@typescript-eslint/no-unsafe-assignment": "error"
const config: unknown = loadConfig();
if (typeof config === "object") {}

/** Example 3: ライブラリのSignature */
function deserialize(json: string): unknown {
  return JSON.parse(json);
}
```
