# #927 「可読性」

四国めたん「配列型の記法選択は可読性に大きく影響します。」
ずんだもん「teamによってはT[]を原則にしてコードを短く保ってるよね。」
四国めたん「ネストが深くなる場合はArray<T>で括弧を付けた方が読みやすいと感じる人もいます。」
ずんだもん「チームでレビューしてどちらが理解しやすいか相談しよう。」
四国めたん「型が複雑になるほど読みやすさが重要です。」
ずんだもん「可読性を意識して記法を選んでね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: シンプル型 */
const ids: string[] = ["a", "b"];

/** Example 2: 複雑型 */
const config: Array<{ name: string; tags: string[] }> = [];

/** Example 3: コメント併用 */
type Row = [id: string, value: number];
const rows: Row[] = [];
```
