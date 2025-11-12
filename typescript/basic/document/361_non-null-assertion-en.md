# #361 "What Is the Non-null Assertion - !"

Shikoku Metan: "Let's look at the Non-null Assertion operator (!) and how it suppresses null checks."
Zundamon: "So I just append ! like document.getElementById('app')!?"
Shikoku Metan: "Exactly; when the element is guaranteed to exist we can treat it as an HTMLElement."
Zundamon: "Can I apply it to a User | null return value too?"
Shikoku Metan: "Sure—writing getUser()! lets you access properties as a User."
Zundamon: "Does it work for a string | undefined variable called value?"
Shikoku Metan: "Yes, value!.length removes undefined and narrows to string."
Zundamon: "I'll use Non-null Assertions only when I'm confident about the value!"

---

## 📺 Code for Display

```typescript
/** Example 1: Forcing DOM element access */
const element = document.getElementById("app")!;
// Treated as HTMLElement (ignores null possibility)
element.innerHTML = "Hello";

/** Example 2: Applying it to a nullable return */
function getUser(): User | null {
  return { name: "Alice", age: 30 };
}
const user = getUser()!;  // Treat as User
console.log(user.name);

/** Example 3: Using it on an undefinedable value */
let value: string | undefined = "hello";
const length = value!.length;  // Treated as string
```
