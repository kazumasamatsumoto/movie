# #276 "Mistake (1) - Using =="

Shikoku Metan: "Let's learn about the problems with the == operator!"
Zundamon: "Since == does type conversion, it causes unexpected behavior!"
Shikoku Metan: "That's right. With userInput == 0, even '0' or empty strings become true."
Zundamon: "value == null is ambiguous because it doesn't distinguish between null and undefined, right?"
Shikoku Metan: "Exactly. Always use === for strict comparison."
Zundamon: "With userInput === 0, only the numeric 0 becomes true!"
Shikoku Metan: "value === null can strictly check only for null, making it safe."
Zundamon: "To write type-safe code, we must absolutely avoid ==!"

---

## 📺 Code for Display

```typescript
// ❌ Wrong: Using ==
if (userInput == 0) {  // '0' or empty string also true
  // Unexpected behavior
}

if (value == null) {  // Doesn't distinguish null and undefined
  // Ambiguous processing
}
```

```typescript
// ✅ Correct: Using ===
if (userInput === 0) {  // Only numeric 0 is true
  // Intended behavior
}

if (value === null) {  // Only null
  // Clear processing
}
```
