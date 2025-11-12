# #470 「void型との違い」

四国めたん「最後にvoidとneverの違いを整理しましょう。」
ずんだもん「voidFunc()は実行後に次の行へ進むんだね。」
四国めたん「neverFunc()は例外で終了するので後続コードは走りません。」
ずんだもん「process内でvoidを呼ぶとその後のconsole.logが実行された!」
四国めたん「fail()を呼ぶとその後は到達不可能になります。」
ずんだもん「制御が戻るかどうかで型を選ぶのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: voidは戻る */
function voidFunc(): void {
  console.log("Done");
}

/** Example 2: neverは戻らない */
function neverFunc(): never {
  throw new Error("Never returns");
}

/** Example 3: 使用例 */
function process(): void {
  voidFunc();
  console.log("After void");
}
function fail(): void {
  neverFunc();
  console.log("Never reached");
}
```
