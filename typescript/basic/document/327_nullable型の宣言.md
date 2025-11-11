# #327 「nullable型の宣言」

四国めたん「nullable型の宣言方法について学びましょう!」
ずんだもん「直接宣言する方法があるんだね!」
四国めたん「はい。string | null のように、ユニオン型として宣言できます。」
ずんだもん「型エイリアスを使うと、再利用できて便利だよね?」
四国めたん「その通りです。Nullable<T> = T | null と定義すれば、汎用的に使えます。」
ずんだもん「インターフェースのプロパティでも使えるんだね!」
四国めたん「はい。ApiResponseのように、data や error をnullableにできます。」
ずんだもん「用途に応じて、適切な宣言方法を選ぶのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 直接宣言 */
let name: string | null = null;
let age: number | null = null;

/** Example 2: 型エイリアス */
type Nullable<T> = T | null;
let user: Nullable<User> = null;
let config: Nullable<Config> = null;

/** Example 3: インターフェース */
interface ApiResponse<T> {
  data: T | null;
  error: string | null;
}
```
