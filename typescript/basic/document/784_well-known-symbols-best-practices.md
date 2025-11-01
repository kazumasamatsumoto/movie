# #784 「ベストプラクティス」

四国めたん「Well-known Symbolsは目的を明確にして使いましょう。」
ずんだもん「既存APIと互換を取るとき以外は乱用しない方がいいね。」
四国めたん「定義するときはプロパティを列挙不可にしておくと安全です。」
ずんだもん「型シグネチャを明示するとチームも理解しやすいよ。」
四国めたん「テストで規約どおりの挙動か確認するのも必須です。」
ずんだもん「ベストプラクティスを守って拡張性と保守性を両立しよう！」
四国めたん「Well-known Symbolsは強力なので設計とドキュメントをセットに。」
ずんだもん「活用するときはチームで合意して進めようね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 列挙不可に設定 */
const descriptorTarget = {};
Object.defineProperty(descriptorTarget, Symbol.toStringTag, {
  value: "DescriptorTarget",
  enumerable: false,
});

/** Example 2: 型ドキュメント */
interface IterableLike<T> {
  [Symbol.iterator](): Iterator<T>;
}

/** Example 3: テスト例 */
function assertIterator<T>(iterable: IterableLike<T>) {
  const iterator = iterable[Symbol.iterator]();
  const first = iterator.next();
  if (!("done" in first) || typeof first.done !== "boolean") {
    throw new Error("invalid iterator");
  }
}
```
