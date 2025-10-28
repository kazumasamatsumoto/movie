# #954 「型述語フィルタリング」

四国めたん「型述語関数を使ってfilterすると型がきれいに絞り込めます。」
ずんだもん「isStringとかisErrorみたいな関数を定義するんだね。」
四国めたん「配列操作から重複する型判定ロジックを切り出せます。」
ずんだもん「複数箇所で同じUnionを扱うときに便利だよ。」
四国めたん「型述語をうまく使って読みやすさと再利用性を高めましょう。」
ずんだもん「型述語フィルタリングを取り入れてね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 型述語 */
interface ErrorResult { error: string }
interface SuccessResult { data: string }

type Result = ErrorResult | SuccessResult;

const results: Result[] = [
  { error: "timeout" },
  { data: "ok" },
];

function isSuccess(result: Result): result is SuccessResult {
  return "data" in result;
}

/** Example 2: filter */
const successOnly = results.filter(isSuccess); // SuccessResult[]

/** Example 3: map */
const dataList = successOnly.map((res) => res.data);
```
