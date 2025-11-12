# #529 「Mapped Types」

四国めたん「Mapped Typesはプロパティを一括操作できる便利機能だよ。」
ずんだもん「Readonly<T>やPartial<T>が典型的な例だったね。」
四国めたん「neverを使うとメソッドだけ除外するRemoveMethods<T>も書ける。」
ずんだもん「getName()がneverになってデータ部分だけ残ってたのだ。」
四国めたん「Key Remappingを使えばキーごと消してしまうOmitMethods<T>も作れる。」
ずんだもん「関数のキーをneverにマップしてからasで落としてたね。」
四国めたん「これで純粋なデータ型を簡単に作れるんだ。」
ずんだもん「neverはプロパティの削除スイッチとして覚えておこう。」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 基本のMapped Types */
type Readonly<T> = {
  readonly [K in keyof T]: T[K];
};

type Partial<T> = {
  [K in keyof T]?: T[K];
};
```

```typescript
/** Example 2: メソッドをneverにする */
type RemoveMethods<T> = {
  [K in keyof T]: T[K] extends Function ? never : T[K];
};

type Data = RemoveMethods<{
  name: string;
  age: number;
  getName(): string;
}>; // { name: string; age: number; getName: never }
```

```typescript
/** Example 3: Key Remappingで削除 */
type OmitMethods<T> = {
  [K in keyof T as T[K] extends Function ? never : K]: T[K];
};

type Clean = OmitMethods<{
  name: string;
  getName(): string;
}>; // { name: string }
```
