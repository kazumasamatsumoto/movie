# #719 「Utility Typesの活用」

四国めたん「TypeScriptのUtility Typesを使えばanyの代替が簡単になります」
ずんだもん「PartialやPickで必要な型だけ組み合わせられるんだよね」
四国めたん「はい。ReadonlyやRecordも型変換を安全に行えます」
ずんだもん「既存型を再利用できるから重複定義も減らせるよ」
四国めたん「Utility Typesを知っておけば柔軟さと安全性を両立できます」
ずんだもん「anyをUtility Typesで置き換えよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: Partial */
type User = { id: string; email: string; name: string };
type UpdateUser = Partial<User>;

/** Example 2: Pick / Omit */
type UserPreview = Pick<User, "id" | "name">;
type UserSecrets = Omit<User, "name">;

/** Example 3: Record */
const permissions: Record<string, boolean> = { read: true, write: false };
```
