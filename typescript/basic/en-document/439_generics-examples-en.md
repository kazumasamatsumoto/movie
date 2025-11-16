# #439 "Real-World Example"

Shikoku Metan: "Let's review a real-world generic void example."
Zundamon: "We built an EventEmitter<T> class."
Shikoku Metan: "on registers listeners and emit notifies them."
Zundamon: "The string emitter sent "Hello"."
Shikoku Metan: "Leaving T unspecified yields a void emitter."
Zundamon: "Generics let us handle events with any data type."
Shikoku Metan: "Void events simply call emit()."
Zundamon: "I'll master practical void generics!"

---

## 📺 Code for Display

```typescript
/** Example 1: Event emitter */

class EventEmitter<T = void> {
  private listeners: Array<(data: T) => void> = [];

  on(listener: (data: T) => void): void {
    this.listeners.push(listener);
  }

  emit(data: T): void {
    this.listeners.forEach(fn => fn(data));
  }
}

/** Example 2: Usage */

const emitter = new EventEmitter<string>();
emitter.on((msg) => console.log(msg));
emitter.emit("Hello");

/** Example 3: Void emitter */

const voidEmitter = new EventEmitter();
voidEmitter.on(() => console.log("Event"));
voidEmitter.emit();
```
