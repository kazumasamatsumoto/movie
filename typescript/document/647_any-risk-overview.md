# #647 「any型の危険性まとめ」

四国めたん「anyを使うと静的保証が消え、バグが潜り込みます」
ずんだもん「補完も効かないし、リファクタリングも怖くなるよね」
四国めたん「はい。ランタイムエラー、セキュリティ事故、技術的負債など影響は大きいです」
ずんだもん「短期の便利さと長期のコストを天秤にかけて判断しよう」
四国めたん「危険性を理解してunknownや厳密な型への移行を進めましょう」
ずんだもん「anyはリスクの塊だって常に意識しておくよ！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: ランタイム不安定 */
const anything: any = JSON.parse("{\"id\":1}");
anything.nonExist(); // TypeError

/** Example 2: 補完喪失 */
function callService(service: any) {
  service.execude(); // typo
}

/** Example 3: 技術的負債リスト */
const risks = ["ランタイムエラー", "保守性低下", "セキュリティ事故"] as const;
```
