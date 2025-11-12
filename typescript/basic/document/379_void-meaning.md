# #379 「void型の意味」

四国めたん「void型は『副作用のための関数』という意味づけを与えます。」
ずんだもん「updateUIのようにDOMを更新する処理が典型だね。」
四国めたん「はい。戻り値を使わないのでvoidで十分です。」
ずんだもん「forEachのコールバックも戻り値を期待しないからvoid?」
四国めたん「その通り。callback: (item: T) => void として副作用を許可しています。」
ずんだもん「イベントハンドラ型もvoidを付けておくと読みやすいね。」
四国めたん「EventHandler = (event: Event) => void と書けば、『結果は使わない』と明示できます。」
ずんだもん「意味を伝えるためにvoidを積極的に使うのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 副作用のための関数 */
function updateUI(data: Data): void {
  document.getElementById("app")!.innerHTML = data.html;
}

/** Example 2: コールバック関数 */
function forEach<T>(
  array: T[],
  callback: (item: T) => void
): void {
  for (const item of array) {
    callback(item);
  }
}

/** Example 3: 戻り値を無視するハンドラ */
type EventHandler = (event: Event) => void;
element.addEventListener("click", (e): void => {
  console.log("Clicked", e);
});
```
