# #687 「サードパーティライブラリのany対策」

四国めたん「サードパーティライブラリがanyを返す場合はラッパー層を設けましょう」
ずんだもん「AdapterパターンでunknownやDTOに変換するんだね」
四国めたん「はい。ライブラリ更新時の影響範囲を局所化できます」
ずんだもん「型定義が公開されていないなら自作d.tsを用意しよう」
四国めたん「外部境界を管理するのがany排除の肝です」
ずんだもん「安全なラッパーを共有資産にしよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: ラッパー */
declare function legacySdk(method: string): any;
export function callLegacy(method: string): unknown {
  return legacySdk(method);
}

/** Example 2: Adapter */
interface PaymentDto { id: string; amount: number }
export function toPaymentDto(value: unknown): PaymentDto {
  if (typeof value !== "object" || value === null) throw new TypeError("invalid");
  const record = value as Record<string, unknown>;
  return { id: String(record.id), amount: Number(record.amount ?? 0) };
}

/** Example 3: d.tsひな型 */
// types/legacy-sdk.d.ts
// declare module "legacy-sdk" {
//   export function invoke(method: string): unknown;
// }
```
