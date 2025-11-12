# #405 「undefined型の変数に代入」

四国めたん「undefined型の変数にもundefinedしか代入できません。」
ずんだもん「value: undefined に undefined を入れる例があったね。」
四国めたん「はい。nullや数値はエラーになります。」
ずんだもん「string | undefined のユニオンなら値とundefinedを切り替えられる?」
四国めたん「その通り。data変数で表現できます。」
ずんだもん「getValue(): string | undefined みたいな関数もよく見るね。」
四国めたん「undefinedで値が無いことを明示できます。」
ずんだもん「undefined型の扱い方を覚えるのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: undefined型変数 */
let value: undefined;
value = undefined;  // OK

/** Example 2: ユニオン型 */
let data: string | undefined;
data = "hello";
data = undefined;

/** Example 3: 関数の戻り値 */
function getValue(): string | undefined {
  if (Math.random() > 0.5) {
    return "value";
  }
  return undefined;
}
```
