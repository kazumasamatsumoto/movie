# #698 「プロトタイピング中のany」

四国めたん「プロトタイピングでは開発速度優先でanyを仮利用することがあります」
ずんだもん「機能検証が目的だからスピードを優先するんだね」
四国めたん「はい。ただしプロト終了時に必ず型整備タスクを起こします」
ずんだもん「experimentalフォルダに隔離して本番コードに混ざらないようにしたいよ」
四国めたん「anyを使った期間や理由を記録しておきましょう」
ずんだもん「検証が終わったら速やかに型安全化しよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: プロトフォルダ */
// src/proto/featureX.ts
let sketchData: any;

/** Example 2: TODO管理 */
const todo = { item: "型整備", due: "Sprint 42" };

/** Example 3: ガード付きwrapper */
export const finalize = (value: any): unknown => value;
```
