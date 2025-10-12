# #646 「anyはどこへでも代入できる」

四国めたん「anyの値は任意の型の変数へ代入できます」
ずんだもん「numberにもstringにも関数にも自由に入れられるんだよね」
四国めたん「はい。型チェックがスキップされるためコンパイルが通ってしまいます」
ずんだもん「結果的にランタイムで予期せぬエラーが出る可能性が高いよ」
四国めたん「代入先が広がるほど危険性も増すと意識しましょう」
ずんだもん「型を守るならunknownや明示的な変換を使おう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 任意の代入先 */
const anything: any = { id: 1 };
const num: number = anything;
const str: string = anything;
const fn: () => void = anything;

/** Example 2: ランタイムエラー例 */
fn(); // 実行時に存在しない場合エラー

/** Example 3: 明示的変換 */
function toRecord(value: unknown): Record<string, unknown> {
  if (typeof value === "object" && value !== null) return value as Record<string, unknown>;
  throw new TypeError("expected object");
}
```
