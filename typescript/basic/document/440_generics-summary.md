# #440 「ジェネリクスまとめ」

四国めたん「voidとジェネリクスのポイントをまとめましょう。」
ずんだもん「Callback<User> のように型パラメータで副作用関数を作るんだね。」
四国めたん「はい。Handler<T = void> でデフォルトを付けても便利です。」
ずんだもん「EventEmitter<T = void> の例も覚えておきたい!」
四国めたん「ジェネリクスとvoidを組み合わせると拡張性が高まります。」
ずんだもん「まとめを活かして再利用可能なAPIを設計するのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 基本的なジェネリクス */

type Callback<T> = (data: T) => void;
const handler: Callback<User> = (user) => {
  console.log(user.name);
};

/** Example 2: デフォルト型パラメータ */

type Handler<T = void> = (data: T) => void;
const voidHandler: Handler = () => {
  console.log("Done");
};

/** Example 3: 実践例 */

class EventEmitter<T = void> {
  on(listener: (data: T) => void): void {}
}
```
