# #648 「anyとTypeScript型システム」

四国めたん「TypeScriptの型システムはサブタイプ関係で安全性を提供します」
ずんだもん「でもanyを使うとその仕組みを素通りしちゃうんだよね」
四国めたん「はい。コンパイラの型推論やチェックが働かなくなります」
ずんだもん「型システムのメリットを得るためにはanyを避けることが重要だよ」
四国めたん「anyは型システムを抜ける裏口と理解しましょう」
ずんだもん「型理論に沿った設計を大切にしよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 型システムを活かす */
function greet(name: string) {
  return `Hello ${name}`;
}

/** Example 2: anyで破壊 */
const nameAny: any = 100;
greet(nameAny); // コンパイルOKだが破綻

/** Example 3: unknownなら守れる */
const nameUnknown: unknown = 100;
if (typeof nameUnknown === "string") greet(nameUnknown);
```
