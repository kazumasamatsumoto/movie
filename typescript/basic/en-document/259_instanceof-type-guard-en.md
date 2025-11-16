# #259 "Instanceof Type Guard"

Shikoku Metan: "Let's learn about instanceof type guards!"
Zundamon: "instanceof checks if something is an instance of a class, right!"
Shikoku Metan: "Yes. It works with built-in classes like Date and Error, as well as custom classes."
Zundamon: "Can we check with value instanceof Date?"
Shikoku Metan: "Exactly. The type is narrowed and Date-specific methods become available."
Zundamon: "Can we check multiple classes too?"
Shikoku Metan: "Yes. Distinguishing between User and Admin classes is a common use case."
Zundamon: "Class-based type checking allows us to write more flexible code!"

---

## 📺 Code for Display

```typescript
/** Example 1: Basic usage */
function processValue(value: Date | string) {
  if (value instanceof Date) {
    console.log(value.getFullYear());
  } else {
    console.log(value.toUpperCase());
  }
}

/** Example 2: Multiple classes */
class User { name: string = ''; }
class Admin { role: string = ''; }

function processEntity(entity: User | Admin) {
  if (entity instanceof Admin) {
    console.log(entity.role);
  } else {
    console.log(entity.name);
  }
}
```
