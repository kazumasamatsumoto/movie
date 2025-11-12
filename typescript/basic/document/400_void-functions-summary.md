# #400 「関数まとめ」

四国めたん「void関数のポイントを総まとめしましょう。」
ずんだもん「logやhandlerのような副作用関数が基本だね。」
四国めたん「はい。戻り値を使わないと一目で分かります。」
ずんだもん「クラスメソッドにもvoidを付けて責務を示せる!」
四国めたん「Logger.logのように記述しましょう。」
ずんだもん「Promise<void>やCallback型もよく出てきたね。」
四国めたん「saveDataやCallback = (result: string) => void が代表例です。」
ずんだもん「まとめを活かしてvoid関数を設計するのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 基本的な使い方 */
function log(msg: string): void {
  console.log(msg);
}
const handler = (e: Event): void => {
  console.log(e);
};

/** Example 2: クラスメソッド */
class Logger {
  log(msg: string): void {
    console.log(msg);
  }
}

/** Example 3: 実践パターン */
async function saveData(data: Data): Promise<void> {
  await database.save(data);
}
type Callback = (result: string) => void;
```
