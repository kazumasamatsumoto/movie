# #585 「instanceof型ガード」

四国めたん「instanceof型ガードはunknownをクラスインスタンスに絞ります」
ずんだもん「ErrorやDateを見分けるときに便利だよね」
四国めたん「はい。プロトタイプチェーンを使って安全に判定できます」
ずんだもん「自作クラスのインスタンス判定にも使えるよ」
四国めたん「クラス境界でunknownを扱うときはinstanceofを活用しましょう」
ずんだもん「オブジェクトの種類を確実に判断できるね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: Error判定 */
function handleError(error: unknown) {
  if (error instanceof Error) {
    console.error(error.message);
  }
}

/** Example 2: Date判定 */
function format(value: unknown) {
  if (value instanceof Date) {
    return value.toISOString();
  }
  return null;
}

/** Example 3: カスタムクラス */
class DomainError extends Error {}
const err: unknown = new DomainError("fail");
if (err instanceof DomainError) {
  console.log(err.name);
}
```
