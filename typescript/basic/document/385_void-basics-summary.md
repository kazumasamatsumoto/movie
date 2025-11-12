# #385 「基本まとめ」

四国めたん「void型の基本ポイントをまとめましょう。」
ずんだもん「logのような副作用関数が典型なんだね。」
四国めたん「はい。戻り値を気にせずに処理を終えます。」
ずんだもん「Promise<void>は非同期でも使えると覚えておく!」
四国めたん「saveDataのように完了のみを通知します。」
ずんだもん「Callback = (data: string) => void でハンドラ型を定義するのも定番だね。」
四国めたん「副作用専用の型を用意すると読みやすくなります。」
ずんだもん「基本を押さえてvoidを自在に使いこなすのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: void型の基本 */
function log(msg: string): void {
  console.log(msg);
}

/** Example 2: Promise<void> */
async function saveData(data: Data): Promise<void> {
  await database.save(data);
}

/** Example 3: 実践パターン */
type Callback = (data: string) => void;
const handler: Callback = (data) => {
  console.log(data);
};
```
