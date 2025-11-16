# #504 "Union Exhaustiveness"

Shikoku Metan: "We also want zero gaps across general union types."
Zundamon: "process() on Value handled every typeof branch."
Shikoku Metan: "Finishing with const exhaustive: never = value ensures coverage."
Zundamon: "Animal unions split Cat and Dog via instanceof."
Shikoku Metan: "Different guards still end with assertNever(animal)."
Zundamon: "Direction literals got an if-chain with every compass point."
Shikoku Metan: "After handling north, south, east, west we call assertNever(direction)."
Zundamon: "No matter the guard style, end union flows with a never check."

---

## 📺 Code for Display

```typescript
/** Example 1: typeof guards */
type Value = string | number | boolean;

function process(value: Value): string {
  if (typeof value === "string") {
    return value.toUpperCase();
  } else if (typeof value === "number") {
    return value.toString();
  } else if (typeof value === "boolean") {
    return value ? "true" : "false";
  }
  const exhaustive: never = value;
  return exhaustive;
}

/** Example 2: Class unions */
class Cat { meow() {} }
class Dog { bark() {} }
type Animal = Cat | Dog;

function assertNever(value: never): never {
  throw new Error(`Unhandled animal: ${value}`);
}

function makeSound(animal: Animal): void {
  if (animal instanceof Cat) {
    animal.meow();
  } else if (animal instanceof Dog) {
    animal.bark();
  } else {
    assertNever(animal);
  }
}

/** Example 3: Direction literals */
type Direction = "north" | "south" | "east" | "west";

function move(direction: Direction): void {
  if (direction === "north") return;
  if (direction === "south") return;
  if (direction === "east") return;
  if (direction === "west") return;
  assertNever(direction);
}
```
