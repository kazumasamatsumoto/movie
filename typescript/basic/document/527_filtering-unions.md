# #527 「フィルタリング」

四国めたん「条件付き型でUnionをフィルタリングしよう。」
ずんだもん「StringsOnly<T>はstringだけ残して他はneverにしてたね。」
四国めたん「'a' | 'b' | 123 | true | 'c'から文字列だけが残った。」
ずんだもん「FunctionsOnly<T>なら関数シグネチャだけが生き残るのだ。」
四国めたん「引数や戻り値が違っても関数型ならちゃんとUnionに残る。」
ずんだもん「NonNullableはnull/undefinedをneverにする実践的なフィルタ。」
四国めたん「string | null | number | undefinedがstring | numberに整理できた。」
ずんだもん「フィルタを組み合わせて型のゴミを一気に除こう。」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 文字列だけ残す */
type StringsOnly<T> = T extends string ? T : never;
type Texts = StringsOnly<"a" | "b" | 123 | true | "c">; // "a" | "b" | "c"
```

```typescript
/** Example 2: 関数型だけ残す */
type FunctionsOnly<T> = T extends (...args: any[]) => any ? T : never;

type Functions = FunctionsOnly<
  | string
  | ((x: number) => string)
  | number
  | ((y: string) => number)
>; // ((x: number) => string) | ((y: string) => number)
```

```typescript
/** Example 3: nullableを除去 */
type NonNullable<T> = T extends null | undefined ? never : T;
type Clean = NonNullable<string | null | number | undefined>; // string | number
```
