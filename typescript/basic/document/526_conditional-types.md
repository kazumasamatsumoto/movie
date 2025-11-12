# #526 「条件付き型」

四国めたん「条件付き型は型レベルのif文みたいなものだよ。」
ずんだもん「IsString<T>でstringならtrue、それ以外はfalseになってた。」
四国めたん「Filter<T>はstringだけ通して他はneverにするフィルタだね。」
ずんだもん「string | number | booleanからstringだけが残ってたのだ。」
四国めたん「FunctionKeys<T>ではメソッド名だけを抜き出していたよ。」
ずんだもん「getName()だけが抽出されて'useful'な型になってたね。」
四国めたん「条件付き型を使えばUnionの中身を柔軟に操作できる。」
ずんだもん「neverと組み合わせて型をスマートに選別しよう。」

---

## 📺 画面表示用コード

```typescript
/** Example 1: IsStringユーティリティ */
type IsString<T> = T extends string ? true : false;
type A = IsString<string>;  // true
type B = IsString<number>;  // false
type C = IsString<"hello">; // true
```

```typescript
/** Example 2: stringだけ通すFilter */
type Filter<T> = T extends string ? T : never;
type Result = Filter<string | number | boolean>; // string
```

```typescript
/** Example 3: 関数型の抽出 */
type FunctionKeys<T> = {
  [K in keyof T]: T[K] extends Function ? K : never
}[keyof T];

type Methods = FunctionKeys<{
  name: string;
  getName(): string;
  age: number;
}>; // "getName"
```
