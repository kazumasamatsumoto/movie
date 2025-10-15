# #1083 「戻り値 - boolean」

四国めたん「includesの戻り値は常にbooleanです。」
ずんだん「存在チェックにそのまま使えるんだね。」
四国めたん「はい、trueかfalseだけでシンプルに判定できます。」
ずんだん「if文やガード節で活躍するよ。」
四国めたん「戻り値型を意識してロジックを組み立ててください。」
ずんだん「わかりやすいAPIだね！」

---

## 📺 画面表示用コード

```typescript
const permissions = ["read", "write"];

const canWrite = permissions.includes("write");
if (canWrite) {
  console.log("user can write");
}
```
