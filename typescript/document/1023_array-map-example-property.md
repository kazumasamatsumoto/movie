# #1023 「実践例(2) - プロパティ抽出」

四国めたん「mapは特定のプロパティだけを抜き出す処理にも向いています。」
ずんだもん「オブジェクト配列からidだけ取り出すみたいなケースだね。」
四国めたん「はい、型推論で戻り値型も自動的に決まります。」
ずんだもん「プロパティ抽出で配列を軽量化したいときに役立つよ。」
四国めたん「実例を通じて活用イメージを掴んでください。」
ずんだもん「mapの使い所が広がるね！」

---

## 📺 画面表示用コード

```typescript
interface Task {
  id: string;
  title: string;
  done: boolean;
}

const tasks: Task[] = [
  { id: "t1", title: "Design", done: true },
  { id: "t2", title: "Implement", done: false },
];

/** Example 1: idだけ */
const taskIds = tasks.map((task) => task.id);

/** Example 2: タイトル */
const titles = tasks.map((task) => task.title);

/** Example 3: 状態文字列 */
const status = tasks.map((task) => `${task.title}:${task.done ? "done" : "todo"}`);
```
