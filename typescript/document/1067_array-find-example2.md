# #1067 「実践例(2)」

四国めたん「もう一つ、ログの中から最新のエラーを探す例を見ましょう。」
ずんだもん「findLastを使って末尾から検索するんだね。」
四国めたん「はい、エラーレベルの条件で検索してメッセージを整形します。」
ずんだん「対応ランタイムであれば簡潔に書けるよ。」
四国めたん「findLastの活用例として覚えておきましょう。」
ずんだもん「最近のエラーをすぐ見つけられるね！」

---

## 📺 画面表示用コード

```typescript
interface Log {
  level: "info" | "warn" | "error";
  message: string;
  timestamp: string;
}

const logs: Log[] = [
  { level: "info", message: "start", timestamp: "2024-03-01T10:00:00Z" },
  { level: "error", message: "timeout", timestamp: "2024-03-01T10:05:00Z" },
  { level: "error", message: "fatal", timestamp: "2024-03-01T10:10:00Z" },
];

const latestError = logs.findLast?.((log) => log.level === "error");

const alertMessage = latestError ? `${latestError.timestamp}:${latestError.message}` : "no error";
```
