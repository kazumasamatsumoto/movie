# #671 「anyがパフォーマンスに及ぼす影響」

四国めたん「any自体は性能に直接影響しませんが、バグで無駄な処理が増える原因になります」
ずんだもん「型チェックをスキップした結果、実行時に例外が増えてリトライが発生するんだよね」
四国めたん「はい。フェイルセーフのための余計なガードやリカバリで負荷が上がります」
ずんだもん「unknownや正確な型なら事前にエラーを防げるから無駄な処理が減るよ」
四国めたん「安定したパフォーマンスを保つためにもany排除が重要です」
ずんだもん「型安全性と性能は切り離せないね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: anyで例外多発 */
const handler: any = {};
try {
  handler.process(); // throws
} catch {
  retry();
}

/** Example 2: 型で予防 */
interface Processor { process(): void; }
function execute(processor: Processor) {
  processor.process();
}

/** Example 3: 余計なリトライ削減 */
const metrics = { retries: 10, errors: 5 };
```
