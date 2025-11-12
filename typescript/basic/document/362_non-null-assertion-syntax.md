# #362 「!演算子の構文」

四国めたん「!演算子の構文をパターン別に確認しましょう。」
ずんだもん「まずは変数value!.lengthの形だね?」
四国めたん「はい。型がstring | nullなら!でstringに絞れます。」
ずんだもん「プロパティにも使えるの?」
四国めたん「user.name!.toUpperCase() のように安全だと確信できるときだけ使います。」
ずんだもん「関数やメソッドチェーンにも連鎖できる?」
四国めたん「document.getElementById("app")! や array.find(...)! でも同じ構文です。」
ずんだもん「構文だけでなく安全性も常に意識するのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 変数への適用 */
let value: string | null = getValue();
const length = value!.length;

/** Example 2: プロパティアクセス */
const user: { name?: string } = getUser();
const name = user.name!.toUpperCase();

/** Example 3: 関数・メソッド呼び出し */
const element = document.getElementById("app")!;
const firstChild = element.firstChild!;
const data = array.find(x => x.id === 1)!;
```
