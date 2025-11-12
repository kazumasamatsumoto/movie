# #435 「Mapped Types」

四国めたん「Mapped Typesでメソッドだけをvoidに変換できます。」
ずんだもん「VoidMethods<Service> でメソッド戻り値をvoidにしていたね。」
四国めたん「はい。モック用に便利です。」
ずんだもん「ToHandlers<T> でプロパティを (value: T[K]) => void に変換する例もあった!」
四国めたん「ユーザーの各プロパティにハンドラを割り当てられます。」
ずんだもん「Mapped Typesでvoid化を自動処理できるんだね。」
四国めたん「ジェネリクスと組み合わせて柔軟な型変換を実現しましょう。」
ずんだもん「void向けのMapped Typesを活用するのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: すべてのメソッドをvoidに */

type VoidMethods<T> = {
  [K in keyof T]: T[K] extends (...args: any[]) => any
    ? (...args: Parameters<T[K]>) => void
    : T[K];
};

/** Example 2: 実用例 */

interface Service {
  getData(): Promise<Data>;
  saveData(data: Data): Promise<void>;
}
type MockService = VoidMethods<Service>;

/** Example 3: プロパティを関数に変換 */

type ToHandlers<T> = {
  [K in keyof T]: (value: T[K]) => void;
};
type UserHandlers = ToHandlers<User>;
```
