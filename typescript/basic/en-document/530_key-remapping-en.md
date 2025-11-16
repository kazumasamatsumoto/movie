# #530 "Key Remapping"

Shikoku Metan: "Key remapping makes mapped types even more flexible."
Zundamon: "Getters<T> turned properties into getName/getAge style methods."
Shikoku Metan: "Template literal types plus Capitalize can auto-build APIs."
Zundamon: "OmitByType<T, U> drops keys whose values match U."
Shikoku Metan: "Removing boolean leaves only name and age."
Zundamon: "RemovePrefix<T, '_'> deletes keys starting with a prefix."
Shikoku Metan: "_id and _internal vanished, leaving just name."
Zundamon: "Combine key remapping with never for powerful type transforms."

---

## 📺 Code for Display

```typescript
/** Example 1: Auto-generating getters */
type Getters<T> = {
  [K in keyof T as `get${Capitalize<string & K>}`]: () => T[K];
};

type User = { name: string; age: number };
type UserGetters = Getters<User>; // { getName: () => string; getAge: () => number }
```

```typescript
/** Example 2: Dropping keys by value type */
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
/** Example 3: Removing prefixed keys */
type RemovePrefix<T, Prefix extends string> = {
  [K in keyof T as K extends `${Prefix}${infer _}` ? never : K]: T[K];
};

type Clean = RemovePrefix<{
  _id: string;
  _internal: number;
  name: string;
}, "_">; // { name: string }
```
