# #393 「イベントハンドラ」

四国めたん「イベントハンドラも典型的なvoid関数です。」
ずんだもん「button?.addEventListenerで位置をログに出す例があったね。」
四国めたん「はい。クリック座標を表示するだけで戻り値は不要です。」
ずんだもん「EventHandler = (event: Event) => void という型を用意してもよい?」
四国めたん「もちろん。preventDefaultのような副作用を書くときにも便利です。」
ずんだもん「ReactのhandleClickも(e: React.MouseEvent): void で宣言するんだね。」
四国めたん「JSXのonClick属性にもそのまま渡せます。」
ずんだもん「フレームワーク問わずvoidハンドラを統一して扱うのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: DOMイベント */
const button = document.getElementById("btn");
button?.addEventListener("click", (e: MouseEvent): void => {
  console.log("Clicked at:", e.clientX, e.clientY);
});

/** Example 2: 型定義 */
type EventHandler = (event: Event) => void;
const handler: EventHandler = (e) => {
  e.preventDefault();
  console.log("Event handled");
};

/** Example 3: Reactイベント */
const handleClick = (e: React.MouseEvent): void => {
  console.log("Button clicked");
};
<button onClick={handleClick}>Click</button>
```
