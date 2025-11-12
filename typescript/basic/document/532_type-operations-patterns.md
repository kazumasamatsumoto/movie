# #532 「型演算パターン」

四国めたん「よく使う型演算パターンをまとめておこう。」
ずんだもん「Filter<T, Condition>はUnionから条件に合う型だけ残してたね。」
四国めたん「'a' | 'b' | 1 | 2から文字列だけを抽出できた。」
ずんだもん「MapToArray<T>は各プロパティを配列化するマッピングパターン。」
四国めたん「nameとageがそれぞれstring[]とnumber[]になってたのがポイント。」
ずんだもん「Match<T>は条件分岐でString/Number/Boolean/Unknownを返してた。」
四国めたん「型に応じたラベルを返すことでパターンマッチっぽく書ける。」
ずんだもん「これらを組み合わせると表現力が一気に広がるのだ。」

---

## 📺 画面表示用コード

```typescript
/** Example 1: フィルタリングパターン */
type Filter<T, Condition> =
  T extends Condition ? T : never;

type Strings = Filter<"a" | "b" | 1 | 2, string>; // "a" | "b"
```

```typescript
/** Example 2: プロパティを配列化 */
type MapToArray<T> = {
  [K in keyof T]: T[K][];
};

type Arrays = MapToArray<{ name: string; age: number }>; // { name: string[]; age: number[] }
```

```typescript
/** Example 3: 型ごとのマッチング */
type Match<T> =
  T extends string ? "String"
  : T extends number ? "Number"
  : T extends boolean ? "Boolean"
  : "Unknown";

type M1 = Match<"hello">; // "String"
type M2 = Match<42>;      // "Number"
type M3 = Match<object>;  // "Unknown"
```
