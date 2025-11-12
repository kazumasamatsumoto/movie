# #455 "Debugging (2)"

Shikoku Metan: "Instrumentation helps monitor void functions."
Zundamon: "timer logged before/after to measure duration."
Shikoku Metan: "try-catch captured failures as well."
Zundamon: "So we trace via logs/metrics instead of return values."
Shikoku Metan: "Exactly; keep observability around side effects."

---

## 📺 Code for Display

```typescript
/** Example 1: Timing logs */
function timer(task: () => void): void {
  console.log('start');
  task();
  console.log('end');
}

/** Example 2: try-catch logging */
function safeProcess(): void {
  try {
    risky();
  } catch (error) {
    console.error('Failed:', error);
  }
}

/** Example 3: Send metrics */
function process(): void {
  metrics.increment('process.start');
  work();
  metrics.increment('process.end');
}
```
