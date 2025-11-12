# #523 「Intersection型」

四国めたん「Intersection型は複数の要件を全部満たす型だよ。」
ずんだもん「{ name } & { age } で両方のプロパティを持つ人になるのだ。」
四国めたん「逆にstring & numberみたいに両立できないとneverになる。」
ずんだもん「テキストxをstringとnumberで同時に満たせないからね。」
四国めたん「neverとのIntersectionはいつもneverになると覚えておこう。」
ずんだもん「object & neverやany & neverも全部消えてた。」
四国めたん「User & { role: 'admin' }のようにUnionをさらに絞る用途も便利。」
ずんだもん「存在しないroleをIntersectするとneverで矛盾を示してくれるんだ。」

---

## 📺 画面表示用コード

```typescript
/** Example 1: Intersectionの基本 */
type WithProfile = { name: string } & { age: number }; // { name: string; age: number }
type Impossible = string & number; // never
type Conflict = { x: string } & { x: number }; // never
```

```typescript
/** Example 2: neverとのIntersection */
type Test1 = string & never; // never
type Test2 = number & never; // never
type Test3 = object & never; // never
type Test4 = any & never;    // never
```

```typescript
/** Example 3: Unionをさらに絞る */
type User = { role: "admin" } | { role: "user" };
type Admin = User & { role: "admin" }; // { role: "admin" }
type InvalidRole = User & { role: "guest" }; // never
```
