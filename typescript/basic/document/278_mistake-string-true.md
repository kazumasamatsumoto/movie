# #278 「間違い(3) - 文字列"true"」

四国めたん「文字列"true"の扱いについて学びましょう!」
ずんだもん「APIから文字列"true"を取得しても、booleanとは別物なんだね!」
四国めたん「はい。value === trueは、文字列とbooleanの比較なのでfalseです。」
ずんだもん「if (value)はtrueになるけど、これは意図しない挙動だよね?」
四国めたん「その通りです。文字列はtruthyなので、"false"でもtrueになってしまいます。」
ずんだもん「const boolValue = value === "true"で明示的に変換するんだね!」
四国めたん「はい。これでbooleanとして正しく動作するようになります。」
ずんだもん「APIの文字列値は必ず型変換してから使うのが大事なのだ!」

---

## 📺 画面表示用コード

```typescript
// ❌ 間違い: 文字列"true"の扱い
const value = "true";  // APIから取得
if (value === true) {  // false
  console.log('実行されない');
}

// ❌ truthyとして扱う（意図しない挙動）
if (value) {  // true（文字列はtruthy）
  console.log('実行される');
}
```

```typescript
// ✅ 正しい: 明示的な変換
const boolValue = value === "true";
if (boolValue === true) {  // 正しく動作
  console.log('実行される');
}
```
