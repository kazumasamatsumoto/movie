# #377 「void型変数」

四国めたん「void型の変数についても触れておきましょう。」
ずんだもん「let value: void; と書けるけど、実用性は低いんだよね?」
四国めたん「はい。代入できるのはundefinedだけで、strictNullChecksならnullも禁じられます。」
ずんだもん「でもexecute(): void を呼んだ結果をvoidとして受け取ることはできる?」
四国めたん「できます。const result: void = execute(); と書けば型が一致します。」
ずんだもん「配列でvoidコールバックを管理するのは便利そう!」
四国めたん「VoidCallback[] にpushしておけば、副作用だけの処理群をまとめられます。」
ずんだもん「仕組みを知っておけば型システムで迷わないのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: void型変数 */
let value: void;
value = undefined;  // OK
// value = null;    // strictNullChecks有効時はエラー

/** Example 2: 戻り値として扱う */
function execute(): void {
  console.log("Executed");
}
const result: void = execute();

/** Example 3: 実用的なコールバック */
type VoidCallback = () => void;
const callbacks: VoidCallback[] = [];
callbacks.push(() => console.log("Done"));
```
