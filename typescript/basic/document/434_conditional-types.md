# #434 「条件付き型」

四国めたん「条件付き型を使うとvoidかどうかで型を切り替えられます。」
ずんだもん「IsVoid<void> は true、IsVoid<number> は falseだったね。」
四国めたん「はい。戻り値型に応じてResultType<T>を変えることもできます。」
ずんだもん「AsyncResult<T> ではTがvoidかどうかでPromise<void>かPromise<{data:T}>になる?」
四国めたん「その通り。fetch1の例で確認しました。」
ずんだもん「条件付き型でvoid対応を自動化できるんだね。」
四国めたん「複雑なAPIでも型安全を維持できます。」
ずんだもん「void向けの分岐を活用するのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: void判定 */

type IsVoid<T> = T extends void ? true : false;
type Test1 = IsVoid<void>;
type Test2 = IsVoid<number>;

/** Example 2: 戻り値型による分岐 */

type ResultType<T> = T extends void
  ? { success: true }
  : { success: true; data: T };

/** Example 3: 実用例 */

type AsyncResult<T> = T extends void
  ? Promise<void>
  : Promise<{ data: T }>;
async function fetch1(): AsyncResult<void> {
  return;
}
```
