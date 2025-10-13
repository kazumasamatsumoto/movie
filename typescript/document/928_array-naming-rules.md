# #928 「命名規則」

四国めたん「配列変数の命名では複数形やListなどの接尾辞を使うと分かりやすいです。」
ずんだもん「users、taskList、itemsこういう名前だね。」
四国めたん「はい、型だけでなく命名でも集合であることを示しましょう。」
ずんだもん「列挙値はconst配列にしてUpperCaseで書くパターンもあるよ。」
四国めたん「命名規則を決めておくとレビューもスムーズになります。」
ずんだもん「読み手に優しい名前を付けよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 複数形 */
const users: string[] = [];

/** Example 2: List接尾辞 */
const taskList: Array<{ id: string; title: string }> = [];

/** Example 3: 定数 */
const STATUS_OPTIONS = ["open", "closed"] as const;
```
