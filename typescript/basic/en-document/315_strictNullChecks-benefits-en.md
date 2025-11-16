# #315 "Why You Should Enable It"

Shikoku Metan「Let's learn about why you should enable strictNullChecks!」
Zundamon「What benefits does it have?」
Shikoku Metan「Yes. It can prevent null pointer exceptions beforehand.」
Zundamon「Since null checks are enforced, runtime errors decrease!」
Shikoku Metan「Exactly. Editor completion is also improved, enhancing the development experience.」
Zundamon「After a null check, the type is narrowed and completion works?」
Shikoku Metan「Yes. It also leads to early bug detection, allowing you to write more robust code.」
Zundamon「Dangerous calls like process(null) become compile errors!」

---

## 📺 Code for Display

```typescript
/** Example 1: Prevent null pointer exceptions */
function getLength(str: string | null): number {
  if (str === null) return 0;
  return str.length; // Safe
}

/** Example 2: Improved editor completion */
const user: User | null = getUser();
if (user !== null) {
  user.name; // Completion works
}

/** Example 3: Early bug detection */
function process(data: string) {
  return data.toUpperCase();
}
process(null); // Compile error
```
