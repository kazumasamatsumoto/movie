# #342 「undefinedable型の宣言」

四国めたん「undefinedable型の宣言方法を学びましょう!」
ずんだもん「基本的な宣言は、型 | undefined なんだね!」
四国めたん「はい。変数に直接 T | undefined を指定できます。」
ずんだもん「型エイリアスで再利用できるの?」
四国めたん「その通りです。Undefinedable<T> のようなジェネリック型で共通化できます。」
ずんだもん「インターフェースでも使えるんだね!」
四国めたん「はい。プロパティの型として T | undefined を指定できます。」
ずんだもん「undefinedable型を宣言して、柔軟な型定義をするのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 基本的な宣言 */
let value: string | undefined;
let count: number | undefined = undefined;
let flag: boolean | undefined;

/** Example 2: 型エイリアスでの再利用 */
type Undefinedable<T> = T | undefined;
let name: Undefinedable<string>;
let age: Undefinedable<number>;

/** Example 3: インターフェースでの利用 */
interface Config {
  timeout: number | undefined;
  maxRetries: number | undefined;
  callback: ((data: string) => void) | undefined;
}
```
