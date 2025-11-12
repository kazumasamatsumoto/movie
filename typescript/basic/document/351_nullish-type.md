# #351 「nullish型 - T | null | undefined」

四国めたん「nullish型(T | null | undefined)で値の不在を表現しましょう!」
ずんだもん「nullとundefinedの両方を同じ型で受けられるんだね?」
四国めたん「はい。type Nullish<T> = T | null | undefined のように再利用できます。」
ずんだもん「ユーザーのメールアドレスみたいに未設定かもしれない項目に使えるの?」
四国めたん「その通り。emailやage?のような項目で意図的な未入力を表せます。」
ずんだもん「データ取得関数の戻り値にも便利?」
四国めたん「ええ。User | null | undefinedで見つからない場合や無効なIDを表現できます。」
ずんだもん「nullish型で不確かな値を安全に扱うのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: nullish型の型エイリアス */
type Nullish<T> = T | null | undefined;
let value: string | null | undefined;
value = "hello";
value = null;
value = undefined;

/** Example 2: Userインターフェースでの利用 */
interface User {
  name: string;
  email: string | null | undefined;
  age?: number | null;
}

/** Example 3: nullishを返す関数 */
function findUser(id: number): User | null | undefined {
  if (id < 0) return undefined;  // 無効なID
  const user = database.find(id);
  return user ?? null;           // 見つからない場合
}
```
