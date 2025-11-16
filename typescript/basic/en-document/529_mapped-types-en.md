# #529 "Mapped Types"

Shikoku Metan: "Mapped types let us transform properties in bulk."
Zundamon: "Readonly<T> and Partial<T> are the poster children."
Shikoku Metan: "With never we can drop methods via RemoveMethods<T>."
Zundamon: "getName() turned into never so only data fields remained."
Shikoku Metan: "Key remapping enables OmitMethods<T> to delete keys entirely."
Zundamon: "We mapped function keys to never and removed them with the as clause."
Shikoku Metan: "That's how we carve out pure data shapes."
Zundamon: "Treat never as the property delete switch."

---

## 📺 Code for Display

```typescript
/** Example 1: Basic mapped types */
type Readonly<T> = {
  readonly [K in keyof T]: T[K];
};

type Partial<T> = {
  [K in keyof T]?: T[K];
};
```

```typescript
/** Example 2: Turning methods into never */
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
/** Example 3: Key remapping to drop methods */
type OmitMethods<T> = {
  [K in keyof T as T[K] extends Function ? never : K]: T[K];
};

type Clean = OmitMethods<{
  name: string;
  getName(): string;
}>; // { name: string }
```
