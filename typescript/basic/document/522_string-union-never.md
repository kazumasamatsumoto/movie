# #522 「string | never = string」

四国めたん「string | never = stringは型等式の代表例だよ。」
ずんだもん「numberや独自のMyTypeでも同じように残るんだね。」
四国めたん「Exclude<T, U>は条件でneverを返すから結果から要素が落ちる仕組み。」
ずんだもん「Result1が'b' | 'c'だけになってたのもそのおかげ。」
四国めたん「ReturnTypeFilterは戻り値がvoidならneverを返してフィルタしてた。」
ずんだもん「stringを返す関数だけ残るからAPI設計が楽になるよ。」
四国めたん「Unionにneverを混ぜて不要なものをそぎ落とそう。」
ずんだもん「型レベルの掃除機みたいで気持ちいいのだ。」

---

## 📺 画面表示用コード

```typescript
/** Example 1: string | neverの等式 */
type Test1 = string | never;            // string
type Test2 = number | never;            // number
type Test3 = MyType | never;            // MyType
type Test4 = (string | number) | never; // string | number
```

```typescript
/** Example 2: Excludeの原理 */
type Exclude<T, U> = T extends U ? never : T;

type Result1 = Exclude<"a" | "b" | "c", "a">; // "b" | "c"
type Result2 = Exclude<string | number, string>; // number
```

```typescript
/** Example 3: 戻り値のフィルタ */
type ReturnTypeFilter<T> =
  T extends (...args: any[]) => infer R
    ? R extends void ? never : R
    : never;

type OnlyString = ReturnTypeFilter<() => string>; // string
type RemovedVoid = ReturnTypeFilter<() => void>;  // never
```
