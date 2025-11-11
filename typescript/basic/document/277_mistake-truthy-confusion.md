# #277 「間違い(2) - truthyとの混同」

四国めたん「truthyとの混同による問題について学びましょう!」
ずんだもん「if (count)だと、0もfalsyだから問題が起きるんだね!」
四国めたん「はい。number型で0は有効な値なのに、falseとして扱われてしまいます。」
ずんだもん「count !== null && count !== undefinedなら0も正しく処理されるよね?」
四国めたん「その通りです。明示的なチェックで意図を明確にしましょう。」
ずんだもん「count != nullという書き方もあるけど、これは例外的だね!」
四国めたん「はい。nullとundefinedの両方をチェックする場合のみ使います。」
ずんだもん「0や空文字列が有効な値の場合は、必ず明示的にチェックするのだ!」

---

## 📺 画面表示用コード

```typescript
// ❌ 間違い: truthyとの混同
function process(count: number | null) {
  if (count) {  // 0もfalsyなので問題
    console.log(count);
  }
}
```

```typescript
// ✅ 正しい: 明示的なチェック
function processCorrect(count: number | null) {
  if (count !== null && count !== undefined) {
    console.log(count);  // 0も正しく処理される
  }
}

// または
if (count != null) {
  console.log(count);
}
```
