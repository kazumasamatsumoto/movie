# #517 "Improving Type Safety"

Shikoku Metan: "Never helps boost type safety."
Zundamon: "transition() guarded states with specific events."
Shikoku Metan: "Unhandled events fall through for now, but we could plug never checks later."
Zundamon: "handle() covered click, keypress, and scroll."
Shikoku Metan: "An else branch with const check: never = event; catches new event types."
Zundamon: "navigate() listed /home, /about, /contact explicitly."
Shikoku Metan: "As soon as we add a route, the never guard complains."
Zundamon: "That's how we keep state machines and routing safe."

---

## 📺 Code for Display

```typescript
/** Example 1: State machine */
type State = "idle" | "loading" | "success" | "error";
type Event = "start" | "complete" | "fail" | "reset";

function transition(state: State, event: Event): State {
  if (state === "idle" && event === "start") return "loading";
  if (state === "loading" && event === "complete") return "success";
  if (state === "loading" && event === "fail") return "error";
  if (event === "reset") return "idle";
  return state;
}

/** Example 2: App events */
type AppEvent =
  | { type: "click"; x: number; y: number }
  | { type: "keypress"; key: string }
  | { type: "scroll"; delta: number };

function handle(event: AppEvent): void {
  if (event.type === "click") console.log(event.x, event.y);
  else if (event.type === "keypress") console.log(event.key);
  else if (event.type === "scroll") console.log(event.delta);
  else {
    const check: never = event;
    throw new Error(`Unhandled: ${JSON.stringify(check)}`);
  }
}

/** Example 3: Routing */
type Route = "/home" | "/about" | "/contact";

function navigate(route: Route): void {
  if (route === "/home") loadHome();
  else if (route === "/about") loadAbout();
  else if (route === "/contact") loadContact();
  else {
    const check: never = route;
    throw new Error(`Unknown route: ${check}`);
  }
}
```
