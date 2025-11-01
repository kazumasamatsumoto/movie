# #611 「anyからunknown移行・実例3」

四国めたん「最後は設定ロード処理のanyをunknownに置き換えます」
ずんだもん「loadConfigの戻り値をunknownにしてスキーマ検証するんだね」
四国めたん「はい。安全なConfig型に変換してから利用します」
ずんだもん「デフォルト値も型安全に適用できるようになるよ」
四国めたん「設定ファイルの破損にも強くなります」
ずんだもん「バリデーション込みでunknown運用を徹底しよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 変更前 */
function loadConfigLegacy(): any {
  return JSON.parse(localStorage.getItem("config") ?? "{}");
}

/** Example 2: unknown化 */
function loadConfig(): unknown {
  return JSON.parse(localStorage.getItem("config") ?? "{}");
}

/** Example 3: 型検証 */
type Config = { theme: "light" | "dark" };
function toConfig(value: unknown): Config {
  if (typeof value === "object" && value !== null && "theme" in value) {
    const theme = (value as Record<string, unknown>).theme;
    if (theme === "light" || theme === "dark") return { theme };
  }
  return { theme: "light" };
}
```
