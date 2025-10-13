# #808 「ブランド型」

四国めたん「unique symbolはブランド型のタグに最適です。」
ずんだもん「string & { readonly __brand: unique symbol }みたいに使うんだね。」
四国めたん「はい、ブランド付きの値だけが関数に渡せます。」
ずんだもん「型変換用のファクトリ関数を用意すると安全だよ。」
四国めたん「ブランドが付いていない生の値は代入できません。」
ずんだもん「ブランド型でドメインルールを型に閉じ込めよう！」
四国めたん「unique symbolがコンパイラレベルの識別子になります。」
ずんだもん「安全なID管理に必須のテクニックだよ！」

---

## 📺 画面表示用コード

```typescript
/** ブランド用シンボル */
declare const USER_ID_BRAND: unique symbol;

type UserId = string & { readonly [USER_ID_BRAND]: true };

/** ファクトリ */
function makeUserId(raw: string): UserId {
  if (!/^usr_[0-9a-f]{8}$/.test(raw)) {
    throw new Error("invalid user id");
  }
  return raw as UserId;
}

/** 使用 */
function loadUser(id: UserId) {
  console.log("load", id);
}
const id = makeUserId("usr_1234abcd");
loadUser(id);
```
