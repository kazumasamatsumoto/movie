# #390 「エラーハンドリング」

四国めたん「void関数でもエラー処理は重要です。」
ずんだもん「validateInputでは条件に応じてthrowしているね。」
四国めたん「はい。入力が無効なら例外を投げ、そうでなければログを残します。」
ずんだもん「processUserではtry-catchでエラーを握りつぶさずにログ出力してる!」
四国めたん「副作用関数でもエラーハンドリングを組み込むと安全です。」
ずんだもん「processではnullならreturn、無効ならthrowと分岐してるんだ。」
四国めたん「正常終了とエラー終了を明確に分けるのが大切です。」
ずんだもん「void関数でもエラー設計を怠らないのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: throw文の使用 */
function validateInput(input: string): void {
  if (input.length === 0) {
    throw new Error("Input is required");
  }
  console.log("Valid input:", input);
}

/** Example 2: try-catchで処理 */
function processUser(user: User): void {
  try {
    validateUser(user);
    saveUser(user);
  } catch (error) {
    console.error("Failed to process user:", error);
  }
}

/** Example 3: returnとthrowの組み合わせ */
function process(data: Data | null): void {
  if (data === null) return;
  if (!data.isValid) throw new Error("Invalid data");
  console.log(data);
}
```
