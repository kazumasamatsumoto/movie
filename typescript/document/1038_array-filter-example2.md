# #1038 「実践例(2)」

四国めたん「別の実践例として、エラーログだけを抽出するケースを見ましょう。」
ずんだもん「statusが500以上のものだけ残す感じだね。」
四国めたん「filterで絞ったあとにmapでメッセージを整形します。」
ずんだもん「通知用のデータ作りにも使えるよ。」
四国めたん「filterの応用パターンとして覚えてください。」
ずんだもん「ログ解析に役立つね！」

---

## 📺 画面表示用コード

```typescript
interface LogEntry {
  id: string;
  status: number;
  message: string;
}

const logs: LogEntry[] = [
  { id: "l1", status: 200, message: "ok" },
  { id: "l2", status: 503, message: "service unavailable" },
  { id: "l3", status: 500, message: "fatal" },
];

/** Example 1: エラー抽出 */
const errors = logs.filter((log) => log.status >= 500);

/** Example 2: メッセージ整形 */
const errorMessages = errors.map((log) => `${log.id}:${log.message}`);

/** Example 3: チェーン */
const alerts = logs
  .filter((log) => log.status >= 500)
  .map((log) => ({ id: log.id, message: log.message.toUpperCase() }));
```
