# #547 「間違い(2) - 到達可能コード」

四国めたん「neverチェックは順番を間違えるとエラーになるよ。」
ずんだもん「bad()ではstringだけ処理して残りをconst check: never = value; にしてた。」
四国めたん「numberやbooleanが残っているのにneverに代入しようとして型エラーだね。」
ずんだもん「good()はstringとnumberの両方を処理した後にneverチェックしてた。」
四国めたん「Unionの全てを網羅して初めてneverが成立する。」
ずんだもん「return check; で到達不可能を明示すればコンパイラも安心。」
四国めたん「順番を間違えないように気を付けよう。」
ずんだもん「neverは最後の番人なんだね。」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 間違った実装 */
function bad(value: string | number): string {
  if (typeof value === "string") return value;
  const check: never = value; // numberが残っている
  return "default";
}
```

```typescript
/** Example 2: 正しい実装 */
function good(value: string | number): string {
  if (typeof value === "string") return value;
  if (typeof value === "number") return value.toString();
  const check: never = value;
  return check;
}
```
