# #516 「静的解析」

四国めたん「neverは静的解析とも相性抜群だよ。」
ずんだもん「HttpMethodのvalidate()はGET/POSTだけ許可して残りをconst check: neverで止めてたね。」
四国めたん「静的に未処理のメソッドがわかるからレビューが楽。」
ずんだもん「process()はnullチェック後にtoUpperCase()してたけど解析がnull排除を理解してたのだ。」
四国めたん「greet()もageがundefinedかどうかで戻り値を切り替えてたよ。」
ずんだもん「こういう制御フロー解析を信頼するには型の絞り込みが大事。」
四国めたん「neverを返すヘルパーを置けば静的解析ツールも連動する。」
ずんだもん「型と解析のダブルチェックで安心しよう。」

---

## 📺 画面表示用コード

```typescript
/** Example 1: HTTPメソッド検証 */
type HttpMethod = "GET" | "POST" | "PUT" | "DELETE";

function validate(method: HttpMethod): boolean {
  if (method === "GET") return true;
  if (method === "POST") return true;
  const check: never = method;
  return false;
}

/** Example 2: 制御フロー解析 */
function process(value: string | null): string {
  if (value === null) {
    return "null";
  }
  return value.toUpperCase();
}

/** Example 3: データフロー解析 */
type User = { name: string; age?: number };

function greet(user: User): string {
  if (user.age !== undefined) {
    return `${user.name} (${user.age})`;
  }
  return user.name;
}
```
