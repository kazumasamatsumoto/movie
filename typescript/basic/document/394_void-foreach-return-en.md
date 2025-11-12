# #394 "Return Value of forEach"

Shikoku Metan: "forEach returns void and expects void callbacks."
Zundamon: "Assigning result = items.forEach(...) gives undefined."
Shikoku Metan: "Correct; the signature explicitly returns void."
Zundamon: "The callback's return value is ignored entirely?"
Shikoku Metan: "Yes—logging side effects is the norm."
Zundamon: "So the key difference from map is whether a new array is returned."
Shikoku Metan: "map yields data, forEach yields only side effects."
Zundamon: "I'll choose based on whether I need results or not!"

---

## 📺 Code for Display

```typescript
/** Example 1: forEach signature */
const items = [1, 2, 3];
const result = items.forEach(item => console.log(item));
console.log(result);

/** Example 2: Callback return ignored */
items.forEach((item): void => {
  console.log(item * 2);
});

/** Example 3: Difference from map */
const doubled = items.map(x => x * 2);
items.forEach(x => console.log(x * 2));
```
