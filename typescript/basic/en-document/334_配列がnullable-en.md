# #334 "Nullable Array"

Shikoku Metan: "Let's learn about when the array itself is nullable!"
Zundamon: "The entire array can be null!"
Shikoku Metan: "Yes. With string[] | null, the array itself can be null or a string array."
Zundamon: "Do we need to check for null before operations?"
Shikoku Metan: "Exactly. We check for null with if (items !== null), then perform operations like forEach."
Zundamon: "We can use Optional Chaining too!"
Shikoku Metan: "Yes. Like items?.length ?? 0 or items?.[0], we can access safely."
Zundamon: "By understanding nullable arrays, we can process them appropriately!"

---

## 📺 Code for Display

```typescript
/** Example 1: Declaring nullable array */
let items: string[] | null = null;
items = ["a", "b", "c"]; // OK

/** Example 2: Operations after null check */
if (items !== null) {
  items.forEach(item => console.log(item));
}

/** Example 3: Safe access with Optional Chaining */
const length = items?.length ?? 0;
const first = items?.[0];
```
