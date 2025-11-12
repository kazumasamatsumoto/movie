# #517 「型安全性向上」

四国めたん「neverを使えば型安全性がグッと上がるよ。」
ずんだもん「State/Eventのtransition()は条件付きで状態遷移してたね。」
四国めたん「Unhandledイベントは現状stateを返すから、さらに検知したければneverを噛ませてもいい。」
ずんだもん「AppEventのhandle()はclick/keypress/scrollを全部if-elseで処理してたのだ。」
四国めたん「elseでconst check: never = event; を置くとイベント追加時に型が警告してくれる。」
ずんだもん「Routeのnavigate()も/home,/about,/contactを全部書いていたよ。」
四国めたん「ルートが増えた瞬間にneverが異常を知らせてくれる仕組み。」
ずんだもん「こうやって型安全なステートやルーティングを守ろう。」

---

## 📺 画面表示用コード

```typescript
/** Example 1: ステートマシン */
type State = "idle" | "loading" | "success" | "error";
type Event = "start" | "complete" | "fail" | "reset";

function transition(state: State, event: Event): State {
  if (state === "idle" && event === "start") return "loading";
  if (state === "loading" && event === "complete") return "success";
  if (state === "loading" && event === "fail") return "error";
  if (event === "reset") return "idle";
  return state;
}

/** Example 2: アプリイベント */
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

/** Example 3: ルーティング */
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
