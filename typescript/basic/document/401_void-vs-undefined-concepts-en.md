# #401 "Conceptual Differences"

Shikoku Metan: "Let's clarify the conceptual difference between void and undefined."
Zundamon: "void means we don't care about the return value, right?"
Shikoku Metan: "Yes, functions like logMessage use it when results are ignored."
Zundamon: "undefined indicates the function might return the actual undefined value?"
Shikoku Metan: "Exactly—findItem yields undefined when nothing is found."
Zundamon: "So the intent differs: Logger is for side effects, Finder for search results."
Shikoku Metan: "Choosing the proper type keeps semantics clear."
Zundamon: "I'll apply each concept appropriately!"

---

## 📺 Code for Display

```typescript
/** Example 1: void: ignore the return */
function logMessage(msg: string): void {
  console.log(msg);
}

/** Example 2: undefined: returns undefined */
function findItem(id: number): Item | undefined {
  return items.find(item => item.id === id);
}

/** Example 3: Different intent */
type Logger = () => void;
type Finder = () => Item | undefined;
```
