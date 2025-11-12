# #525 「分配法則」

四国めたん「条件付き型はUnionに対して分配されるんだ。」
ずんだもん「ToArray<string | number>がstring[] | number[]になる理由だね。」
四国めたん「Excludeも同じで各メンバーに条件をかけてneverを落としてた。」
ずんだもん「'a'だけ消えて'b' | 'c'が残ってたよ。」
四国めたん「分配を止めたいときはNoDistributeみたいにTをタプルで包む。」
ずんだもん「そうすると(string | number)[]みたいにまとめて扱えるのだ。」
四国めたん「分配するかどうかをコントロールできると型演算の精度が上がる。」
ずんだもん「neverの挙動を理解した上で使い分けよう。」

---

## 📺 画面表示用コード

```typescript
/** Example 1: ToArrayの分配 */
type ToArray<T> = T extends any ? T[] : never;
type Result = ToArray<string | number>; // string[] | number[]
```

```typescript
/** Example 2: Excludeでも分配 */
type Exclude<T, U> = T extends U ? never : T;
type Filtered = Exclude<"a" | "b" | "c", "a">; // "b" | "c"
```

```typescript
/** Example 3: 分配を止める */
type NoDistribute<T> = [T] extends [any] ? T[] : never;

type Result1 = NoDistribute<string | number>; // (string | number)[]
type Result2 = ToArray<string | number>; // string[] | number[]
```
