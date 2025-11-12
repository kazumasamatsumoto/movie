# #357 「??の使用例」

四国めたん「?? の実践的な使い方を見てみましょう!」
ずんだもん「環境変数からホストやポートを設定できるんだね?」
四国めたん「はい。env.HOST ?? 'localhost' のように簡潔です。」
ずんだもん「Optional Chainingと合わせると便利?」
四国めたん「ええ。user?.address?.city ?? 'Unknown' で欠損を埋められます。」
ずんだもん「関数引数のageにもデフォルトを入れられる?」
四国めたん「そうです。age ?? 0 でnullishだけ補完できます。」
ずんだもん「?? をパターン化して堅牢な設定を作るのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 設定値のデフォルト処理 */
const config = {
  host: env.HOST ?? "localhost",
  port: env.PORT ?? 8080,
  timeout: env.TIMEOUT ?? 3000,
};

/** Example 2: Optional Chainingとの組み合わせ */
const userName = user?.name ?? "Anonymous";
const city = user?.address?.city ?? "Unknown";
const email = user?.contacts?.[0]?.email ?? "no-email";

/** Example 3: 関数引数での利用 */
function createUser(name: string, age?: number | null) {
  return {
    name,
    age: age ?? 0,
    status: "active",
  };
}
```
