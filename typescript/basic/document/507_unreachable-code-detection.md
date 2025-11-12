# #507 「到達不可能コード検出」

四国めたん「never型は到達不可能コードの検出にも役立つよ。」
ずんだもん「process()でstringとnumberを返した後のelseは実行されないはず。」
四国めたん「そこにvalue;って書くと型がneverになって警告してくれる。」
ずんだもん「handle()でもStatusがsuccessかerrorだけだからconsole.log(status)は到達不能。」
四国めたん「IDEがグレーアウトしてくれるのもありがたいよね。」
ずんだもん「neverReturn()みたいに絶対例外を投げる関数も同じ扱い。」
四国めたん「呼び出し後のconsole.log('到達不可能')はエラーとして検出される。」
ずんだもん「neverを意識するとデッドコードを早期に消せるのだ。」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 型ガード後のelse */
function process(value: string | number) {
  if (typeof value === "string") return value.toUpperCase();
  else if (typeof value === "number") return value * 2;
  else {
    value; // never型
    return 0; // 到達しない
  }
}

/** Example 2: Unionの残りを検出 */
type Status = "success" | "error";

function handle(status: Status) {
  if (status === "success") return "OK";
  if (status === "error") return "NG";
  console.log(status); // 到達不能
}

/** Example 3: 例外で止まる関数 */
function neverReturn(): never {
  throw new Error("Error");
}

function example() {
  neverReturn();
  console.log("到達不可能");
}
```
