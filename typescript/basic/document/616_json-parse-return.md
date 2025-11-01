# #616 「JSON.parse()の戻り値」

四国めたん「JSON.parse()の戻り値はanyになるので注意が必要です」
ずんだもん「なんでも入ってくるから安全対策が必須だね」
四国めたん「はい。実際にはunknownとして扱うのが推奨です」
ずんだもん「parseのラッパーを作ればプロジェクト全体で統一できるよ」
四国めたん「型ガードやスキーマで検証してから使いましょう」
ずんだもん「JSONの境界から型安全を始めよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: anyが返る */
const raw: any = JSON.parse("{\"id\":1}");
raw.nonExist(); // runtime error

/** Example 2: ラッパー関数 */
function parseJson(value: string): unknown {
  return JSON.parse(value);
}

/** Example 3: 型ガード */
function isUser(value: unknown): value is { id: number } {
  return typeof value === "object" && value !== null && "id" in value;
}
```
