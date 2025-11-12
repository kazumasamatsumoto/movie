# #521 「Union型 - 消える」

四国めたん「Unionにneverを混ぜると自動的に消えるんだ。」
ずんだもん「string | neverがstringだけになるやつだね。」
四国めたん「NonNullable<T>もnull/undefinedをneverに変えてクリーンにしてた。」
ずんだもん「boolean | null | undefinedでも結果はbooleanだけ残るのだ。」
四国めたん「同じUnionにneverを何度足しても最終結果は変わらない。」
ずんだもん「Complex型がstring | number | booleanにまとまってたね。」
四国めたん「こういう性質を知っておくと型演算の結果を読みやすい。」
ずんだもん「不要なneverは自然に消えると覚えておこう。」

---

## 📺 画面表示用コード

```typescript
/** Example 1: neverはUnionから消える */
type A = string | never;        // string
type B = number | never;        // number
type C = boolean | never;       // boolean
type D = string | number | never;  // string | number
```

```typescript
/** Example 2: NonNullableでのフィルタ */
type NonNullable<T> = T extends null | undefined ? never : T;

type CleanString = NonNullable<string | null>;  // string
type CleanNumber = NonNullable<number | undefined>;  // number
type CleanBool = NonNullable<boolean | null | undefined>;  // boolean
```

```typescript
/** Example 3: 複数のneverがあっても同じ */
type Complex =
  | string
  | never
  | number
  | never
  | boolean;  // string | number | boolean
```
