# #397 "Interface Methods"

Shikoku Metan: "Interfaces also describe void methods."
Zundamon: "Lifecycle.init/destroy are textbook examples."
Shikoku Metan: "Component implements them faithfully."
Zundamon: "Event interfaces are mostly void too?"
Shikoku Metan: "handleClick and handleKeyPress don't return anything."
Zundamon: "So the contract explicitly allows side effects only."
Shikoku Metan: "Exactly—declaring void in the interface keeps everyone safe."
Zundamon: "I'll spell out contracts with void methods!"

---

## 📺 Code for Display

```typescript
/** Example 1: Interface */
interface Lifecycle {
  init(): void;
  destroy(): void;
}

/** Example 2: Implementing class */
class Component implements Lifecycle {
  init(): void {
    console.log("Initialized");
  }

  destroy(): void {
    console.log("Destroyed");
  }
}

/** Example 3: Event listener interface */
interface EventListener {
  handleClick(event: MouseEvent): void;
  handleKeyPress(event: KeyboardEvent): void;
}
```
