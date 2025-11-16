# #260 "In Type Guard"

Shikoku Metan: "Let's learn about in type guards!"
Zundamon: "We check for the presence of object properties with in!"
Shikoku Metan: "Yes. We can discriminate types by the existence of specific properties."
Zundamon: "Like using 'bark' in animal?"
Shikoku Metan: "Exactly. If the bark property exists, it's narrowed to Dog type."
Zundamon: "Distinguishing success and failure with success: true is common too!"
Shikoku Metan: "Yes. Patterns that discriminate types with discriminator properties are practical."
Zundamon: "It's useful for complex type discrimination and allows type-safe code!"

---

## 📺 Code for Display

```typescript
/** Example 1: Basic usage */
type Dog = { bark: () => void; };
type Cat = { meow: () => void; };

function makeSound(animal: Dog | Cat) {
  if ('bark' in animal) {
    animal.bark();
  } else {
    animal.meow();
  }
}

/** Example 2: Complex type discrimination */
type Success = { success: true; data: string };
type Error = { success: false; error: string };

function handle(result: Success | Error) {
  if ('data' in result) {
    console.log(result.data);
  }
}
```
