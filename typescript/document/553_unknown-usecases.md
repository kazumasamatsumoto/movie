# #553 「unknownの使用場面」

四国めたん「unknownは予測できない入力を受ける場面で役立ちます」
ずんだもん「RESTのレスポンスやフォーム入力みたいなところだね」
四国めたん「はい。まずunknownで受けてから型ガードで期待する型へ絞ります」
ずんだもん「外部からのデータをいきなりanyにするより安全だよ」
四国めたん「エラーハンドリングやイベントリスナーでもunknownが効果的です」
ずんだもん「汎用的なハンドラを作れるから保守性も高まるね」

---

## 📺 画面表示用コード

```typescript
/** Example 1: APIレスポンス */
async function fetchUser(): Promise<unknown> {
  const res = await fetch("/api/user");
  return res.json();
}

/** Example 2: フォーム入力の検証 */
function validate(value: unknown) {
  if (typeof value === "string") return value.trim();
  if (Array.isArray(value)) return value.length;
  return null;
}

/** Example 3: DOMイベント */
function onMessage(event: MessageEvent<unknown>) {
  if (typeof event.data === "object" && event.data !== null) {
    console.log("payload", event.data);
  }
}
```
