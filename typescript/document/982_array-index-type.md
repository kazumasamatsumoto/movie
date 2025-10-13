# #982 「インデックス型」

四国めたん「配列インデックスはnumber型です。」
ずんだもん「for文のiや配列型のキーもnumberってことだね。」
四国めたん「はい、オブジェクトのキーとして使うと文字列に変換されますが型はnumberです。」
ずんだもん「Record<number, T>のようにインデックス型を指定することもできるよ。」
四国めたん「インデックス型を理解して配列操作に活かしましょう。」
ずんだもん「基本だけど大事だね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: for文 */
const values = ["a", "b"];
for (let index = 0; index < values.length; index++) {
  const value = values[index];
}

/** Example 2: Record */
const map: Record<number, string> = { 0: "zero", 1: "one" };

/** Example 3: keyof */
type Indices = keyof typeof values; // number
```
