# #369 「ベストプラクティス」

四国めたん「!を使うならベストプラクティスを守りましょう。」
ずんだもん「まずは型ガードを優先するんだよね?」
四国めたん「はい。element !== null で確認してからDOMを操作します。」
ずんだもん「Optional Chainingも積極的に使う?」
四国めたん「user?.name ?? "Unknown" のようにnullish対策を織り込みます。」
ずんだもん「どうしても必要なときだけコメントで理由を書くの?」
四国めたん「root要素が必ず存在するなど、保証を書き添えると読み手が安心します。」
ずんだもん「指針を決めて!を最小限にするのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 型ガードを優先 */
const element = document.getElementById("app");
if (element !== null) {
  element.innerHTML = "Hello";
}

/** Example 2: Optional Chainingを活用 */
const name = user?.name ?? "Unknown";
const result = data?.process()?.value;

/** Example 3: やむを得ず使うときは理由を書く */
// アプリ起動時に必ず存在することが保証されている
const rootElement = document.getElementById("root")!;
ReactDOM.render(<App />, rootElement);
```
