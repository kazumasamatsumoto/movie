# #956 「実例(2)」

四国めたん「もう一つ、APIレスポンスで成功とエラーを混在させる例を見ましょう。」
ずんだもん「SuccessとErrorのUnion配列だね。」
四国めたん「はい、型ガードで成功だけ抽出し、エラーはログに吐き出します。」
ずんだもん「型述語関数を用意しておくと処理が分かりやすいよ。」
四国めたん「実例を参考に混合データを安全に扱ってください。」
ずんだもん「運用で役立つパターンだよ！」

---

## 📺 画面表示用コード

```typescript
interface Success { status: "success"; data: string }
interface Failure { status: "failure"; error: string }

type ApiResult = Success | Failure;

const results: ApiResult[] = [
  { status: "success", data: "ok" },
  { status: "failure", error: "timeout" },
];

function isSuccess(result: ApiResult): result is Success {
  return result.status === "success";
}

/** Example 1: 成功だけ */
const successes = results.filter(isSuccess);

/** Example 2: エラー対応 */
results
  .filter((result): result is Failure => !isSuccess(result))
  .forEach((error) => console.error(error.error));

/** Example 3: map */
const messages = results.map((result) =>
  isSuccess(result) ? result.data : `error:${result.error}`
);
```
