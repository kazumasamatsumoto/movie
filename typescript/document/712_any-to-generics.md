# #712 「ジェネリクスへの置き換え」

四国めたん「共通関数でanyを使っているならジェネリクスに置き換えましょう」
ずんだもん「型パラメータで受け取れば呼び出し側の型がそのまま伝わるんだよね」
四国めたん「はい。extends制約を付けると型安全と柔軟性を両立できます」
ずんだもん「インターフェイスやクラスでも同じように活用できるよ」
四国めたん「ジェネリクスでanyを排除すれば再利用性が向上します」
ずんだもん「TypeScriptらしい抽象化を取り戻そう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: anyだった関数 */
function identityAny(value: any) {
  return value;
}

/** Example 2: ジェネリクスで置換 */
function identity<T>(value: T): T {
  return value;
}

/** Example 3: 制約付き */
function pickKey<T extends object, K extends keyof T>(obj: T, key: K): T[K] {
  return obj[key];
}
```
