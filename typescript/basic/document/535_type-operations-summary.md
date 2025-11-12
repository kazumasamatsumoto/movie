# #535 「型演算まとめ」

四国めたん「never回の総仕上げに型演算を振り返ろう。」
ずんだもん「Law1〜4でUnion/Intersection/Exclude/Extractの基本を押さえたね。」
四国めたん「string | never = string、string & never = neverは鉄板ルール。」
ずんだもん「実践ヘルパーとしてNonNullableやFunctionKeys、PickByTypeも便利だった。」
四国めたん「複合的な型演算ではDeepPartialでネストも柔らかくできる。」
ずんだもん「Result<T, E>みたいな判別Unionはエラーハンドリングに大活躍だよ。」
四国めたん「これらを組み合わせると堅牢な型システムを作れる。」
ずんだもん「neverの性質を理解して型演算を味方につけよう。」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 基本法則 */
type Law1 = string | never;    // string
type Law2 = string & never;    // never
type Law3<T> = Exclude<T, never>; // T
type Law4<T> = Extract<never, T>; // never
```

```typescript
/** Example 2: 実践ヘルパー */
type NonNullable<T> = T extends null | undefined ? never : T;
type FunctionKeys<T> = {
  [K in keyof T]: T[K] extends Function ? K : never
}[keyof T];
type PickByType<T, U> = {
  [K in keyof T as T[K] extends U ? K : never]: T[K]
};
```

```typescript
/** Example 3: 複合的な型演算 */
type DeepPartial<T> = {
  [K in keyof T]?: T[K] extends object ? DeepPartial<T[K]> : T[K];
};

type Result<T, E> =
  | { ok: true; value: T }
  | { ok: false; error: E };
```
