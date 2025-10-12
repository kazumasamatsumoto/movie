# #652 「暗黙的any型に注意」

四国めたん「暗黙的anyは型を省略したときに自動で付与されるanyです」
ずんだもん「noImplicitAnyがfalseだと勝手にanyになっちゃうんだよね」
四国めたん「はい。意図せず型安全性が失われるので即座に検出しましょう」
ずんだもん「tsconfigでnoImplicitAnyをtrueにするのが最初の防衛線だよ」
四国めたん「暗黙anyは潜在的なバグの温床です」
ずんだもん「プロジェクト全体で撲滅しよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 暗黙any */
function multiply(a, b) {
  return a * b; // a,bが暗黙any
}

/** Example 2: tsconfig */
{
  "compilerOptions": {
    "noImplicitAny": true
  }
}

/** Example 3: 明示型で回避 */
function multiplySafe(a: number, b: number): number {
  return a * b;
}
```
