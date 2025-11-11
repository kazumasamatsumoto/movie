# #345 "Optional Parameters"

Shikoku Metan「Let's learn about optional parameters!」
Zundamon「We add a ? after the parameter name!」
Shikoku Metan「Yes. That makes the parameter optional.」
Zundamon「Can we omit it when calling?」
Shikoku Metan「Exactly. When omitted, the parameter value becomes undefined.」
Zundamon「We can combine it with default values too!」
Shikoku Metan「Yes. When you set a default value, the specified value is used when omitted.」
Zundamon「With optional parameters, we can create flexible functions!」

---

## 📺 Code for Display

```typescript
/** Example 1: Basics of optional parameters */
function greet(name: string, age?: number) {
  if (age !== undefined) {
    console.log(`${name} is ${age} years old`);
  } else {
    console.log(`Hello, ${name}`);
  }
}

/** Example 2: Omitting when calling */
greet("Alice", 30);  // Two arguments
greet("Bob");        // age is omitted

/** Example 3: Combining with default values */
function createUser(name: string, role: string = "user") {
  return { name, role };
}
```
