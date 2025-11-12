# #528 「Exclude<T, never>」

四国めたん「Exclude<T, never>は何も変えないって知ってた？」
ずんだもん「neverを取り除いても残りは元のTと同じになるんだね。」
四国めたん「stringやnumberを渡してもそのまま返ってきてた。」
ずんだもん「他のExcludeだとちゃんと要素が減るから違いがわかるのだ。」
四国めたん「RemoveNever<T>みたいにneverだけを除去しても最適化で消される。」
ずんだもん「string | number | neverがstring | numberになる例がまさにそれ。」
四国めたん「つまりUnionに無意味なneverがあっても結果は同じ。」
ずんだもん「型演算を読むときはneverを精神的にスキップしよう。」

---

## 📺 画面表示用コード

```typescript
/** Example 1: Exclude<T, never>の挙動 */
type Exclude<T, U> = T extends U ? never : T;
type A = Exclude<string, never>;          // string
type B = Exclude<string | number, never>; // string | number
type C = Exclude<never, never>;           // never
```

```typescript
/** Example 2: 通常のExclude */
type D = Exclude<string | number, string>; // number
type E = Exclude<"a" | "b" | "c", "a">;   // "b" | "c"
type F = Exclude<string | never, never>;   // string
```

```typescript
/** Example 3: RemoveNeverユーティリティ */
type RemoveNever<T> = T extends never ? never : T;

type Original = string | number | never; // string | number
type Filtered = RemoveNever<Original>;   // string | number
```
