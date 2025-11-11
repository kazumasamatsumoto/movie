# #350 「undefinedable型まとめ」

四国めたん「undefinedable型のまとめをしましょう!」
ずんだもん「T | undefined で、undefinedを許容する型が作れるんだね!」
四国めたん「はい。オプショナルプロパティは自動的にundefinedableになります。」
ずんだもん「安全なアクセス方法がいくつかあるの?」
四国めたん「その通りです。Optional Chainingや、Nullish Coalescing演算子が使えます。」
ずんだもん「実践パターンではどう使うの?」
四国めたん「はい。options?.port ?? 8080 のように、デフォルト値と組み合わせると便利です。」
ずんだもん「undefinedable型をマスターして、堅牢なコードを書くのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: undefinedable型の基本 */
type Undefinedable<T> = T | undefined;
interface User {
  name: string;
  age?: number;  // オプショナル
}

/** Example 2: 安全なアクセス */
function greet(user?: User) {
  const name = user?.name ?? "Guest";
  console.log(`Hello, ${name}`);
}

/** Example 3: 実践パターン */
const config: Config = {
  host: "localhost",
  port: options?.port ?? 8080,
  timeout: options?.timeout ?? 3000,
};
```
