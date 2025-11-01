# #1052 「グループ化」

四国めたん「reduceで配列をグループ化するパターンもよく使います。」
ずんだもん「カテゴリごとに配列をまとめるやつだね。」
四国めたん「アキュムレータにRecordやMapを使って分配します。」
ずんだもん「データを集計するときに役立つよ。」
四国めたん「グループ化の書き方を身につけておきましょう。」
ずんだもん「集計処理の定番テクニックだね！」

---

## 📺 画面表示用コード

```typescript
interface Task {
  id: string;
  status: "todo" | "doing" | "done";
}

const tasks: Task[] = [
  { id: "t1", status: "todo" },
  { id: "t2", status: "doing" },
  { id: "t3", status: "todo" },
];

/** Example 1: Recordでグループ化 */
const grouped = tasks.reduce<Record<Task["status"], Task[]>>((acc, task) => {
  (acc[task.status] ??= []).push(task);
  return acc;
}, { todo: [], doing: [], done: [] });

/** Example 2: Map */
const groupedMap = tasks.reduce<Map<Task["status"], Task[]>>((acc, task) => {
  const list = acc.get(task.status) ?? [];
  list.push(task);
  return acc.set(task.status, list);
}, new Map());

/** Example 3: 情報抽出 */
const counts = Object.fromEntries(
  Object.entries(grouped).map(([status, list]) => [status, list.length])
);
```
