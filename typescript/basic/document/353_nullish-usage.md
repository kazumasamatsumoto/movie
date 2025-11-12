# #353 「nullish型の使用例」

四国めたん「nullish型の実用例を確認しましょう!」
ずんだもん「APIレスポンスのdataはnullやundefinedになることがあるよね?」
四国めたん「はい。T | null | undefinedにして安全に判定できます。」
ずんだもん「データベース呼び出しも、例外でundefinedを返せるの?」
四国めたん「そうです。try-catchでundefinedを返せば呼び出し側で区別できます。」
ずんだもん「フォーム入力のemailやphoneも未入力ならnullish?」
四国めたん「ええ。string | null | undefinedにすれば状態を正しく表現できます。」
ずんだもん「現実のデータに合わせてnullish型を活用するのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: APIレスポンスの型定義 */
interface ApiResponse<T> {
  data: T | null | undefined;
  error: string | null | undefined;
  status: number;
}

/** Example 2: データベースクエリ */
async function getUser(id: number): Promise<User | null | undefined> {
  try {
    return await db.users.findById(id);
  } catch {
    return undefined;
  }
}

/** Example 3: フォーム入力の型 */
interface FormData {
  name: string;
  email: string | null | undefined;
  phone: string | null | undefined;
}
```
