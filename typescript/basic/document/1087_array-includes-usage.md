# #1087 「使用例」

四国めたん「includesの使用例として、権限チェックをしてみましょう。」
ずんだん「ユーザーの権限配列に"admin"が含まれているか調べるんだね。」
四国めたん「真偽値を返して簡潔に条件分岐できます。」
ずんだん「ロールベースのアクセス制御にぴったりだよ。」
四国めたん「使用例で利用シーンをイメージしてください。」
ずんだん「日常的に使うパターンだね！」

---

## 📺 画面表示用コード

```typescript
const permissions = ["read", "write"];

const isAdmin = permissions.includes("admin");

if (!isAdmin) {
  console.log("no admin rights");
}
```
