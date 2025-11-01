# #654 「any型の限定ユースケース」

四国めたん「anyを使うなら限定的なユースケースに絞りましょう」
ずんだもん「型が提供されていない外部SDKや一時的なプロトタイプだよね」
四国めたん「はい。ログ収集やメトリクスなど型整備が追いつかない部分も候補です」
ずんだもん「ただし必ずTODOと代替案を添えておくのがマナーだよ」
四国めたん「ユースケースを明文化して乱用を抑えましょう」
ずんだもん「チームで合意した範囲だけに留めよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: SDKラッパー */
declare const legacySdk: any;
export function callLegacy(method: string): unknown {
  return legacySdk.invoke(method);
}

/** Example 2: プロトタイプ段階 */
// TODO: replace tempAnalytics with typed version
let tempAnalytics: any;

/** Example 3: 監査リスト */
const approvedAnyUsage = ["legacySdk", "tempAnalytics"] as const;
```
