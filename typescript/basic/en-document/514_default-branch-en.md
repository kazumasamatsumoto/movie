# #514 "Default Branches"

Shikoku Metan: "Default clauses become the last line of exhaustiveness."
Zundamon: "move() switched over north, south, east, west."
Shikoku Metan: "Throwing const check: never = dir; in default rejects unknown inputs."
Zundamon: "Adding center immediately surfaced as it fell into default."
Shikoku Metan: "Building an exhaustiveCheck() helper is a classic move."
Zundamon: "Sharing that helper across switches keeps things consistent."
Shikoku Metan: "Treat default as a watchdog rather than trash can."
Zundamon: "Never makes new directions far less scary."

---

## 📺 Code for Display

```typescript
/** Example 1: Moving in four directions */
type Direction = "north" | "south" | "east" | "west";

function move(dir: Direction): [number, number] {
  switch (dir) {
    case "north":
      return [0, 1];
    case "south":
      return [0, -1];
    case "east":
      return [1, 0];
    case "west":
      return [-1, 0];
    default:
      const check: never = dir;
      throw new Error(`Unhandled: ${check}`);
  }
}

/** Example 2: Detecting new cases */
type ExtendedDirection = Direction | "center";

function brokenMove(dir: ExtendedDirection) {
  switch (dir) {
    case "north":
      return [0, 1];
    case "south":
      return [0, -1];
    default:
      const check: never = dir; // center lands here
      throw new Error();
  }
}

/** Example 3: Using exhaustiveCheck */
function exhaustiveCheck(value: never): never {
  throw new Error(`Unhandled: ${value}`);
}

function safeMove(dir: Direction) {
  switch (dir) {
    case "north":
      return [0, 1];
    case "south":
      return [0, -1];
    case "east":
      return [1, 0];
    case "west":
      return [-1, 0];
    default:
      return exhaustiveCheck(dir);
  }
}
```
