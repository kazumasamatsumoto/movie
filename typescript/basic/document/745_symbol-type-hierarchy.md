# #745 「型階層」

四国めたん「symbolはプリミティブ型の一つで、anyより下、neverより上に位置します。」
ずんだもん「unknownには代入できるけど、stringには直接入らないんだよね。」
四国めたん「symbolは独自の型階層を持ちます。」
ずんだもん「シリアライズできないから文字列型と互換ではないってことだ。」
四国めたん「neverはすべての型のサブタイプなのでsymbolにも代入可能です。」
ずんだもん「階層を意識すると型変換の判断がしやすいね。」
四国めたん「Union型での振る舞いも理解しておきましょう。」
ずんだもん「型階層を把握して安全な設計を目指そう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: unknownとanyの位置 */
const sym = Symbol("id");
const u: unknown = sym; // OK
const a: any = sym; // OK

/** Example 2: stringには代入不可 */
// const str: string = sym; // エラー: symbolはstringに割り当て不可

/** Example 3: neverはsymbolに代入可能 */
declare const neverValue: never;
const s: symbol = neverValue; // OK: neverはすべての型のサブタイプ
```
