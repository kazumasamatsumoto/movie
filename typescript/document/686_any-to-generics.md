# #686 「anyからジェネリクスへ」

四国めたん「共通処理でanyを使っていたらジェネリクスに置き換えましょう」
ずんだもん「型パラメータで受けると呼び出し側の型がそのまま伝わるんだよね」
四国めたん「はい。extends制約を付ければ型安全な抽象化ができます」
ずんだもん「utility関数の品質が一気に上がるよ」
四国めたん「ジェネリクスは再利用性と安全性の両立手段です」
ずんだもん「anyに頼らない抽象化を目指そう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: anyを使った悪例 */
function identityAny(value: any) {
  return value;
}

/** Example 2: ジェネリクスで改善 */
function identity<T>(value: T): T {
  return value;
}

/** Example 3: 制約付き */
function mergeArrays<T extends unknown[]>(target: T, extra: T): T {
  return [...target, ...extra] as T;
}
```
