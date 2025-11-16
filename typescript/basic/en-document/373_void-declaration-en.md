# #373 "Declaring void"

Shikoku Metan: "Let's learn three common ways to annotate void."
Zundamon: "First is the classic function declaration with : void."
Shikoku Metan: "Exactly—function greet(): void makes the intent explicit."
Zundamon: "Arrow functions can do (msg: string): void => ... too?"
Shikoku Metan: "Of course; assignments keep the same meaning."
Zundamon: "Can we define reusable function types as well?"
Shikoku Metan: "Yes, create aliases like type Callback = (data: string) => void."
Zundamon: "I'll memorize these declaration styles to pick void easily!"

---

## 📺 Code for Display

```typescript
/** Example 1: Function declaration */
function greet(name: string): void {
  console.log(`Hello, ${name}`);
}

/** Example 2: Arrow function */
const log = (msg: string): void => {
  console.log(msg);
};

/** Example 3: Function type alias */
type VoidFunction = () => void;
type Callback = (data: string) => void;
const handler: Callback = (data) => console.log(data);
```
