# #391 「throw文」

四国めたん「void関数でもthrow文を使って例外を送出できます。」
ずんだもん「assertで条件を満たさなければthrow new Errorするんだね。」
四国めたん「はい。副作用関数でもエラー時は例外で伝えます。」
ずんだもん「validateAgeのようにif文で複数チェックすると分かりやすい!」
四国めたん「境界を超えたら即throwして処理を止めます。」
ずんだもん「throwErrorはneverを返すからvoid関数から呼んでも問題ない?」
四国めたん「その通り。neverはvoidに代入できるのでprocessでも利用できます。」
ずんだもん「throwの仕組みを理解して安全なvoid関数を書くのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: throw文はvoid関数で使用可能 */
function assert(condition: boolean, message: string): void {
  if (!condition) {
    throw new Error(message);
  }
}

/** Example 2: バリデーション関数 */
function validateAge(age: number): void {
  if (age < 0) throw new Error("Age cannot be negative");
  if (age > 150) throw new Error("Age is too large");
  console.log("Age is valid");
}

/** Example 3: never型との関係 */
function throwError(message: string): never {
  throw new Error(message);
}
function process(): void {
  throwError("Error");
}
```
