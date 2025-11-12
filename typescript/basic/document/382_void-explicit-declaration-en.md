# #382 "Explicit Declaration"

Shikoku Metan: "Let's see when void should be written explicitly."
Zundamon: "Public functions such as initialize benefit from : void annotations, right?"
Shikoku Metan: "Exactly, and interfaces like Logger.log should declare void as well."
Zundamon: "Can smaller internal helpers like logError rely on inference instead?"
Shikoku Metan: "They often do, depending on team guidelines."
Zundamon: "ESLint's explicit-function-return-type rule can enforce annotations!"
Shikoku Metan: "Yes, enable it whenever you need a consistent policy."
Zundamon: "I'll keep clear criteria for when to be explicit!"

---

## 📺 Code for Display

```typescript
/** Example 1: When to annotate */
export function initialize(config: Config): void {
  // Public API
}
interface Logger {
  log(message: string): void;
}

/** Example 2: Acceptable inference */
const logError = (err: Error) => {
  console.error(err);
};

/** Example 3: Enforcing with ESLint */
// .eslintrc.json
{
  "rules": {
    "@typescript-eslint/explicit-function-return-type": "error"
  }
}
```
