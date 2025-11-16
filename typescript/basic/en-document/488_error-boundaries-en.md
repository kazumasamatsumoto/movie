# #488 "Error Boundaries"

Shikoku Metan: "Wrap never-throwing functions with error boundaries."
Zundamon: "safeExecute caught throw and returned a fallback."
Shikoku Metan: "safeAsync did the same for async code."
Zundamon: "React's ErrorBoundary logged via componentDidCatch."
Shikoku Metan: "Boundaries keep the app resilient."

---

## 📺 Code for Display

```typescript
/** Example 1: Sync boundary */
function safeExecute<T>(fn: () => T, fallback: T): T {
  try {
    return fn();
  } catch (error) {
    console.error("Error caught:", error);
    return fallback;
  }
}

/** Example 2: Async boundary */
async function safeAsync<T>(fn: () => Promise<T>, fallback: T): Promise<T> {
  try {
    return await fn();
  } catch (error) {
    console.error("Async error:", error);
    return fallback;
  }
}

/** Example 3: React boundary */
class ErrorBoundary extends React.Component {
  componentDidCatch(error: Error): void {
    console.error("Component error:", error);
  }
  render() {
    return this.props.children;
  }
}
```
