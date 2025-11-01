# #1037 「実践例(1)」

四国めたん「実践例として、アクティブユーザーだけを抽出してみましょう。」
ずんだもん「ユーザー配列からactive===trueだけ残すやつだね。」
四国めたん「filter後にmapでビュー用のデータに変換します。」
ずんだもん「チェーンで読みやすく書けるよ。」
四国めたん「実例を参考に絞り込みロジックを組み立ててください。」
ずんだもん「現場でそのまま使えるね！」

---

## 📺 画面表示用コード

```typescript
interface Account {
  id: string;
  name: string;
  active: boolean;
  lastLogin: string;
}

const accounts: Account[] = [
  { id: "a1", name: "meta", active: true, lastLogin: "2024-03-01" },
  { id: "a2", name: "zunda", active: false, lastLogin: "2024-02-20" },
];

/** Example 1: activeユーザー */
const activeAccounts = accounts.filter((account) => account.active);

/** Example 2: ビュー用 */
const viewModel = activeAccounts.map((account) => ({
  id: account.id,
  name: account.name.toUpperCase(),
}));

/** Example 3: チェーン */
const displayNames = accounts
  .filter((account) => account.active)
  .map((account) => account.name);
```
