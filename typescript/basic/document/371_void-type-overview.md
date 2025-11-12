# #371 「void型とは」

四国めたん「void型は戻り値を気にしない関数を宣言するときに使います!」
ずんだもん「function logMessage(msg: string): void なら、ログを出すだけって伝わるんだね!」
四国めたん「はい。returnを書かなくてもOKで、副作用だけを表現します。」
ずんだもん「undefinedを返す関数とは何が違うの?」
四国めたん「voidは『何も返さない』意図、undefinedは『undefinedという値を返す』意図になります。」
ずんだもん「イベントリスナーのコールバックもvoidで書くの?」
四国めたん「そうです。() => void にして、副作用だけの関数だと示します。」
ずんだもん「void型で戻り値不要な処理を明確にするのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: void型の基本 */
function logMessage(msg: string): void {
  console.log(msg);
  // returnなし、または return; のみ
}

/** Example 2: undefinedとの違い */
function returnsVoid(): void {
  console.log("副作用のみ");
}
function returnsUndefined(): undefined {
  return undefined;  // 明示的にundefinedを返す
}

/** Example 3: 実用例 */
function addEventListener(callback: () => void): void {
  // イベントリスナーの登録
}
```
