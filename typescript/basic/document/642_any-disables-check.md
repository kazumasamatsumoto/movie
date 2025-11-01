# #642 「anyで型チェックは無効化される」

四国めたん「anyを使うとTypeScriptの型チェックが無効化されます」
ずんだもん「エディタ補完もなくなるし、実行時までエラーが隠れるんだよね」
四国めたん「はい。型システムの価値を自らオフにするのと同じです」
ずんだもん「静的解析を活かしたいならunknownや正確な型を使おう」
四国めたん「anyはコンパイラの保護を失わせることを忘れないでください」
ずんだもん「安全を手放す選択だって意識しておこう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: anyで警告無し */
const payload: any = JSON.parse("{}");
payload.notExist(); // runtime errorでもコンパイルは通る

/** Example 2: 補完が効かない */
function print(value: any) {
  value.toFix(); // typoでも検出されない
}

/** Example 3: 静的保証を失う */
const strictPayload: unknown = payload; // unknownにすればガードが必要
```
