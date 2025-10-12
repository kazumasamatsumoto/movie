# #643 「anyは最後の手段」

四国めたん「anyを使うのは本当に最後の手段に留めましょう」
ずんだもん「型情報が全く手に入らないときだけにするんだよね」
四国めたん「はい。期限付きのTODOを残して速やかにunknownや正確な型へ移行します」
ずんだもん「レビューでも使われた理由と撤去計画を確認したいよ」
四国めたん「運用ルールを定めて安易なanyを防ぎましょう」
ずんだもん「型安全の文化を守る最後の砦だね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: TODO付きany */
// TODO: replace any with ValidPayload by 2024-07-01
let tempPayload: any;

/** Example 2: ラッパーで限定 */
function unsafeCall(fn: (...args: any[]) => any): unknown {
  return fn();
}

/** Example 3: 期限管理 */
const debtRegister = [
  { location: "services/user.ts", reason: "SDK lacks types", due: "2024-07-01" },
] as const;
```
