# #612 「strictモードとany」

四国めたん「strictモードを有効にすると暗黙anyが禁止されます」
ずんだもん「tsconfigのstrict: trueをオンにするだけだね」
四国めたん「はい。noImplicitAnyなど複数の安全設定が一括で入ります」
ずんだもん「既存プロジェクトでは段階的にstrictへ移行するのがコツだよ」
四国めたん「strictがany撲滅の土台になります」
ずんだもん「コンパイラに守ってもらって品質を上げよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: tsconfig設定 */
{
  "compilerOptions": {
    "strict": true
  }
}

/** Example 2: 暗黙any検出 */
function sum(a, b) {
  return a + b; // ❌ strictでエラー
}

/** Example 3: 対応策 */
function sumSafe(a: number, b: number): number {
  return a + b;
}
```
