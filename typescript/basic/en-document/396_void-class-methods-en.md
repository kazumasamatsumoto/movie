# #396 "Class Methods"

Shikoku Metan: "Classes often expose void methods."
Zundamon: "Counter.increment only mutates state."
Shikoku Metan: "reset is also side-effect only."
Zundamon: "Component.initialize/destroy simply log lifecycle steps?"
Shikoku Metan: "Exactly—pure lifecycle hooks."
Zundamon: "EventEmitter.emit logs the event name as well!"
Shikoku Metan: "Annotate these methods with void to clarify responsibilities."
Zundamon: "I'll mark state-changing methods with void!"

---

## 📺 Code for Display

```typescript
/** Example 1: Class methods */
class Counter {
  private count = 0;

  increment(): void {
    this.count++;
  }

  reset(): void {
    this.count = 0;
  }
}

/** Example 2: Init and destroy */
class Component {
  initialize(): void {
    console.log("Initializing...");
  }

  destroy(): void {
    console.log("Destroying...");
  }
}

/** Example 3: Event emission */
class EventEmitter {
  emit(event: string): void {
    console.log(`Event: ${event}`);
  }
}
```
