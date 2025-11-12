# #530 「Key Remapping」

四国めたん「Key RemappingはMapped Typesをさらに柔軟にしてくれるよ。」
ずんだもん「Getters<T>はキー名からgetName/getAgeを生成してたね。」
四国めたん「template literal型とCapitalizeでAPIを自動生成できる。」
ずんだもん「OmitByType<T, U>では値の型がUならキーをneverにして削除してた。」
四国めたん「booleanだけ落として{name, age}を残すのが分かりやすい例。」
ずんだもん「RemovePrefix<T, '_'>はキー名がプレフィックスで始まるかで除外してた。」
四国めたん「_idや_internalを消してnameだけ残るクリーンな型だよ。」
ずんだもん「Key Remappingとneverの合わせ技で柔軟な型操作を楽しもう。」

---

## 📺 画面表示用コード

```typescript
/** Example 1: Gettersの自動生成 */
type Getters<T> = {
  [K in keyof T as `get${Capitalize<string & K>}`]: () => T[K];
};

type User = { name: string; age: number };
type UserGetters = Getters<User>; // { getName: () => string; getAge: () => number }
```

```typescript
/** Example 2: 型でキーを削除 */
type OmitByType<T, U> = {
  [K in keyof T as T[K] extends U ? never : K]: T[K];
};

type Data = OmitByType<{
  name: string;
  age: number;
  active: boolean;
}, boolean>; // { name: string; age: number }
```

```typescript
/** Example 3: プレフィックスで除外 */
type RemovePrefix<T, Prefix extends string> = {
  [K in keyof T as K extends `${Prefix}${infer _}` ? never : K]: T[K];
};

type Clean = RemovePrefix<{
  _id: string;
  _internal: number;
  name: string;
}, "_">; // { name: string }
```
