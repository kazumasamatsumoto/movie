# #310 「undefined型まとめ」

四国めたん「undefined型のまとめをしましょう!」
ずんだもん「undefined型は値の不在を表す重要な型なんだね!」
四国めたん「はい。ユニオン型やオプショナルプロパティで頻繁に使われます。」
ずんだもん「undefinedチェックには !== undefined や Null合体演算子??が便利だよね?」
四国めたん「その通りです。型ガードで安全に値を扱えるようになります。」
ずんだもん「Option型パターンで、エラーハンドリングも型安全にできるね!」
四国めたん「void型との違いや、JSON変換の挙動も理解しておくことが大切です。」
ずんだもん「undefined型を正しく使って、バグの少ないコードを書くのだ!」

---


```typescript
/** Example 1: undefined型の基本 */
let value: string | undefined;
interface User {
  name: string;
  age?: number;  // オプショナル
}

/** Example 2: undefinedチェック */
if (value !== undefined) {
  value.toUpperCase(); // string型
}
const name = userName ?? "Guest";

/** Example 3: 実践パターン */
function greet(name?: string): void {
  console.log(name ?? "Guest");
}
type Option<T> = T | undefined;
```
