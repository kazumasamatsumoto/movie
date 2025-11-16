# #329 "Assigning null"

Shikoku Metan: "Let's learn about assigning null!"
Zundamon: "We can assign null to nullable types!"
Shikoku Metan: "Yes. You can assign null to a User | null type variable at any time."
Zundamon: "Using null as an initial value is common too, right?"
Shikoku Metan: "Exactly. It allows us to explicitly express the state of having no value yet."
Zundamon: "We reset values with null during logout!"
Shikoku Metan: "Yes. With currentUser = null, we can clear the user information."
Zundamon: "Assigning null makes state management clearer!"

---

## 📺 Code for Display

```typescript
/** Example 1: Assigning null */
let user: User | null = getUser();
user = null; // OK

/** Example 2: null as initial value */
let cache: Cache | null = null;
function init() {
  cache = new Cache();
}

/** Example 3: null when resetting */
let currentUser: User | null = loginUser;
function logout() {
  currentUser = null;
}
```
