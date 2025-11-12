# #395 "Method Definitions"

Shikoku Metan: "Void clarifies the intent of object methods."
Zundamon: "logger.log written with method syntax is easy to read."
Shikoku Metan: "error follows the same side-effect pattern."
Zundamon: "Can arrow-style properties also use void?"
Shikoku Metan: "Yes, utils.log demonstrates that."
Zundamon: "Defining log and warn in a Logger type makes reuse simple!"
Shikoku Metan: "Document the method responsibilities for the whole team."
Zundamon: "Void methods keep side effects isolated!"

---

## 📺 Code for Display

```typescript
/** Example 1: Object literal methods */
const logger = {
  log(message: string): void {
    console.log(`[LOG] ${message}`);
  },
  error(message: string): void {
    console.error(`[ERROR] ${message}`);
  }
};

/** Example 2: Method-style property */
const utils = {
  log: (msg: string): void => {
    console.log(msg);
  }
};

/** Example 3: Type definition */
type Logger = {
  log(message: string): void;
  warn(message: string): void;
};
```
