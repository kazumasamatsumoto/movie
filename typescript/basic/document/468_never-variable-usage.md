# #468 「変数宣言」

四国めたん「never型の変数には何も代入できません。」
ずんだもん「neverValue = 1; が全部エラーになってた!」
四国めたん「条件付き型でnullやundefinedを除外するときにneverを活用します。」
ずんだもん「NonNullableやExcludeの実装例がまさにそれだね。」
四国めたん「ユニオンから不必要なケースを削るときもneverを使います。」

---

## 📺 画面表示用コード

```typescript
/** Example 1: never型変数 */
let neverValue: never;

/** Example 2: NonNullable */
type NonNullable<T> = T extends null | undefined ? never : T;
type Result = NonNullable<string | null>;

/** Example 3: Exclude */
type Exclude<T, U> = T extends U ? never : T;
type Numbers = Exclude<string | number, string>;
```
