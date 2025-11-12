# #524 「string & never = never」

四国めたん「UnionだけじゃなくIntersectionでもneverの性質が活きるよ。」
ずんだもん「string & neverは必ずneverになる定番パターン。」
四国めたん「numberやboolean、unknownでも同じで矛盾を示せる。」
ずんだもん「型が同時にAとBになれないContradictionもneverだったね。」
四国めたん「逆に矛盾しない { type: 'A' } & { value: number } はそのまま残る。」
ずんだもん「Extract型は欲しい部分だけ残すからneverが自然に消えるのだ。」
四国めたん「Unionからnumberだけ抜くと残りはnumberでスッキリ。」
ずんだもん「neverは矛盾の証明書って覚えておこう。」

---

## 📺 画面表示用コード

```typescript
/** Example 1: string & neverの等式 */
type Test1 = string & never;   // never
type Test2 = number & never;   // never
type Test3 = boolean & never;  // never
type Test4 = unknown & never;  // never
type Test5 = any & never;      // never
```

```typescript
/** Example 2: 矛盾するIntersection */
type Contradiction = { type: "A" } & { type: "B" }; // never
type Valid = { type: "A" } & { value: number }; // { type: "A"; value: number }
```

```typescript
/** Example 3: Extractの原理 */
type Extract<T, U> = T extends U ? T : never;

type OnlyNumber = Extract<string | number, number>; // number
type Keys = Extract<"a" | "b" | "c", "a" | "b">; // "a" | "b"
```
