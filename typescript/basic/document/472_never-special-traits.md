# #472 「特殊な性質」

四国めたん「neverはユニオンでもインターセクションでも特殊な振る舞いをします。」
ずんだもん「string | never がstringになるのがまさにそれ!」
四国めたん「string & never は常にneverです。」
ずんだもん「exhaustiveCheck(value: never) で網羅性も確認できるんだ?」
四国めたん「Colorの例で漏れを検出していましたね。」
ずんだもん「特殊性を理解して型安全性を高めるのだ!"

---

## 📺 画面表示用コード

```typescript
/** Example 1: ユニオンとインターセクション */
type Result1 = string | never;
type Result4 = string & never;

/** Example 2: 網羅性チェック用関数 */
function exhaustiveCheck(value: never): never {
  throw new Error(`Unhandled case: ${value}`);
}

/** Example 3: 活用例 */
type Color = "red" | "blue";
function getColor(color: Color): string {
  if (color === "red") return "#ff0000";
  if (color === "blue") return "#0000ff";
  return exhaustiveCheck(color);
}
```
