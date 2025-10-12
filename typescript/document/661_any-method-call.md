# #661 「anyでのメソッド呼び出し」

四国めたん「anyでメソッドを呼ぶとコンパイルが通ってしまいます」
ずんだもん「存在しないメソッドを呼んでも警告ゼロだもんね」
四国めたん「はい。修正中に名前を変え忘れても気づけません」
ずんだもん「unknownならメソッドを呼ぶ前に型ガードを書く必要があるよ」
四国めたん「メソッド呼び出しはanyと最も相性が悪い操作です」
ずんだもん「安全な呼び出しのためにもanyを排除しよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: anyでメソッド */
const service: any = {};
service.execute(); // 実行時エラー

/** Example 2: unknownで保護 */
const safeService: unknown = {};
if (typeof safeService === "object" && safeService !== null && "execute" in safeService) {
  (safeService as { execute: () => void }).execute();
}

/** Example 3: 型付きインターフェース */
interface Service {
  execute(): void;
}
```
