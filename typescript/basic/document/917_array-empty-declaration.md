# #917 「空配列の宣言」

四国めたん「空配列を宣言するときは型注釈を付けると安心です。」
ずんだもん「const logs: string[] = []; みたいに書くんだね。」
四国めたん「型を付けないとany[]になる場合があります。」
ずんだもん「あとでpushするときに型が効くようにしておきたいね。」
四国めたん「空配列の型指定は可読性と安全性の両方に役立ちます。」
ずんだもん「最初に型を決めてから要素を追加しよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 空配列 */
const logs: string[] = [];
logs.push("start");

/** Example 2: Array<T> */
const queue: Array<number> = [];

/** Example 3: 状態管理 */
let tasks: string[] = [];
function addTask(task: string) {
  tasks = [...tasks, task];
}
```
