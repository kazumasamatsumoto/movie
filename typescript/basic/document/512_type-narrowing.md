# #512 「型の絞り込み」

四国めたん「型の絞り込みでUnionを安全に扱おう。」
ずんだもん「Responseのhandle()はstatusで200/404/500を全部さばいてたね。」
四国めたん「最後にconst check: never = res; と書けば完全に絞った証明になる。」
ずんだもん「process()はtypeofでstring/number/booleanごとに返り値を変えてたのだ。」
四国めたん「順番に条件を書くと残りの型が自動的に決まるのが嬉しい。」
ずんだもん「さらにin演算子を使えばオブジェクトのUnionも段階的に扱えるよ。」
四国めたん「narrowLog()ではキーの存在でdata型かerror型かを切り分けていた。」
ずんだもん「丁寧な絞り込みが網羅性チェックにも効いてくるね。」

---

## 📺 画面表示用コード

```typescript
/** Example 1: HTTPレスポンスを絞り込み */
type Response =
  | { status: 200; data: string }
  | { status: 404; error: string }
  | { status: 500; error: string };

function handle(res: Response) {
  if (res.status === 200) {
    console.log(res.data);
  } else if (res.status === 404) {
    console.log(res.error);
  } else if (res.status === 500) {
    console.log(res.error);
  }
  const check: never = res;
  return check;
}

/** Example 2: typeofで段階的に絞る */
function process(value: string | number | boolean) {
  if (typeof value === "string") {
    return value.toUpperCase();
  } else if (typeof value === "number") {
    return value * 2;
  }
  return !value; // 残りはboolean
}

/** Example 3: in演算子で分岐 */
type ApiResult =
  | { ok: true; data: string }
  | { ok: false; error: string };

function narrowLog(result: ApiResult) {
  if ("data" in result) {
    console.log(result.data);
  } else if ("error" in result) {
    console.error(result.error);
  } else {
    const check: never = result;
    throw new Error(`Unhandled: ${check}`);
  }
}
```
