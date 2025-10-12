# #670 「anyで修正コストが膨らんだ例」

四国めたん「3つ目の実例はanyの置き換えに想定以上の工数がかかったケースです」
ずんだもん「1ファイルのanyがサービス全体に広がってて、型定義を総入れ替えしたんだよね」
四国めたん「はい。関係する関数やテストもすべて修正する必要がありました」
ずんだもん「初期の段階でunknownに変えておけばコストは最小で済んだよ」
四国めたん「放置すると後で高額なリファクタリング費用が発生します」
ずんだもん「早期対応が一番の節約策だね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: anyが広がったサービス */
export function process(payload: any) {
  return pipeline.map((step) => step(payload));
}

/** Example 2: 置き換え後シグネチャ */
type EventPayload = { id: string; type: string };
export function processSafe(payload: EventPayload) {
  return pipeline.map((step) => step(payload));
}

/** Example 3: 影響範囲メモ */
const impactedFiles = ["service.ts", "pipeline.ts", "tests/service.spec.ts"] as const;
```
