# #834 「型階層」

四国めたん「TypeScriptの型階層ではbigintはプリミティブ型の一つです。」
ずんだもん「numberとは互換じゃないんだね。」
四国めたん「bigintはunknownとanyには代入できますがnumberには代入できません。」
ずんだもん「neverはbigintのサブタイプとして扱えるよ。」
四国めたん「Union型でbigint | numberを使う場合は変換ロジックが必要です。」
ずんだもん「階層を知ってコンパイルエラーを防ごう！」
四国めたん「型システムの位置を理解すると設計が楽になります。」
ずんだもん「bigintの型階層を押さえてね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: unknownへの代入 */
const big: bigint = 10n;
const unknownValue: unknown = big; // OK

/** Example 2: numberには代入不可 */
// const num: number = big; // コンパイルエラー

/** Example 3: neverはbigintに代入可能 */
declare const neverValue: never;
const bigValue: bigint = neverValue; // OK
```
