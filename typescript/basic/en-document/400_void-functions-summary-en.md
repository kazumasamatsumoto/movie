# #400 "Function Summary"

Shikoku Metan: "Let's wrap up the void function topics."
Zundamon: "Side-effect helpers like log or handler are the foundation."
Shikoku Metan: "Yes, they make it obvious no return is needed."
Zundamon: "Class methods can use void to express responsibilities too."
Shikoku Metan: "Logger.log is a good template."
Zundamon: "Promise<void> and Callback types also appeared a lot."
Shikoku Metan: "saveData and Callback = (result: string) => void are key examples."
Zundamon: "I'll apply this summary when designing void functions!"

---

## 📺 Code for Display

```typescript
/** Example 1: Basic usage */
function log(msg: string): void {
  console.log(msg);
}
const handler = (e: Event): void => {
  console.log(e);
};

/** Example 2: Class method */
class Logger {
  log(msg: string): void {
    console.log(msg);
  }
}

/** Example 3: Practical pattern */
async function saveData(data: Data): Promise<void> {
  await database.save(data);
}
type Callback = (result: string) => void;
```
