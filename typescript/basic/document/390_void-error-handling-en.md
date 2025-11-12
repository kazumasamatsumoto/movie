# #390 "Error Handling"

Shikoku Metan: "Error handling still matters in void functions."
Zundamon: "validateInput throws when the value is invalid."
Shikoku Metan: "Right—it throws for empty input and logs valid cases."
Zundamon: "processUser wraps validation and saving in try-catch to log failures."
Shikoku Metan: "Side-effect functions become safer with proper error handling."
Zundamon: "process returns for null data and throws when data.isValid is false."
Shikoku Metan: "Always distinguish normal completion from error exits."
Zundamon: "I'll design error handling even for void functions!"

---

## 📺 Code for Display

```typescript
/** Example 1: Using throw */
function validateInput(input: string): void {
  if (input.length === 0) {
    throw new Error("Input is required");
  }
  console.log("Valid input:", input);
}

/** Example 2: Handling with try-catch */
function processUser(user: User): void {
  try {
    validateUser(user);
    saveUser(user);
  } catch (error) {
    console.error("Failed to process user:", error);
  }
}

/** Example 3: Combining return and throw */
function process(data: Data | null): void {
  if (data === null) return;
  if (!data.isValid) throw new Error("Invalid data");
  console.log(data);
}
```
