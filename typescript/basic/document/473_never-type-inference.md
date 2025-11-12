# #473 「型推論」

四国めたん「TypeScriptはthrowしかしない関数をneverと推論します。」
ずんだもん「fail(message) がまさにそれ!」
四国めたん「明示的に書きたいときはabort(message): neverと宣言しましょう。」
ずんだもん「条件分岐でカバレッジを満たせば残りのコードはneverになるの?」
四国めたん「はい、到達不可能と判断されます。」
ずんだもん「推論と注釈を状況に応じて使い分けるのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 推論されるnever */
function fail(message: string) {
  throw new Error(message);
}

/** Example 2: 明示的な宣言 */
function abort(message: string): never {
  throw new Error(message);
}

/** Example 3: 条件分岐での推論 */
function process(value: string | number) {
  if (typeof value === "string") {
    return value.length;
  } else {
    return value * 2;
  }
  // unreachable, inferred never
}
```
