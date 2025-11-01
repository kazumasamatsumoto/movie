# #720 「カスタムUtility Typesを作る」

四国めたん「既存のUtility Typesで足りない場合はカスタム型を作りましょう」
ずんだもん「型レベル関数を自作して業務に合わせられるんだよね」
四国めたん「はい。条件付き型やマッピング構文を組み合わせれば強力な型操作ができます」
ずんだもん「anyを使わずに柔軟な型変換が実現できるよ」
四国めたん「プロジェクト共通のUtilityを整備して型文化を強化しましょう」
ずんだもん「再利用可能な型ツールキットを育てよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: DeepReadonly */
type DeepReadonly<T> = {
  readonly [K in keyof T]: T[K] extends object ? DeepReadonly<T[K]> : T[K];
};

/** Example 2: RequireExactlyOne */
type RequireExactlyOne<T, Keys extends keyof T = keyof T> =
  Keys extends keyof T
    ? { [K in Keys]-?: Required<Pick<T, K>> & Partial<Record<Exclude<Keys, K>, never>> }[Keys]
    : never;

/** Example 3: Merge */
type Merge<T, U> = {
  [K in keyof T | keyof U]: K extends keyof U
    ? U[K]
    : K extends keyof T
    ? T[K]
    : never;
};
```
