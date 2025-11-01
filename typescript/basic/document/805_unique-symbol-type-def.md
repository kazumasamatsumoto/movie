# #805 「型定義」

四国めたん「unique symbolを型定義に組み込むにはdeclare constでリテラル型を作ります。」
ずんだもん「型エイリアスやインターフェースのキーに転用できるんだね。」
四国めたん「typeofを使って参照します。」
ずんだもん「公開型ライブラリでもunique symbolを扱えるように準備しておこう。」
四国めたん「型定義でユニーク性を明示するとコンシューマが安心です。」
ずんだもん「ドキュメントにキーの役割を書き添えるのも大切だよ。」
四国めたん「型定義を整えてunique symbolを共有しましょう。」
ずんだもん「型から設計意図を伝えよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: ambient宣言 */
declare const LOCALE_TOKEN: unique symbol;

/** Example 2: 型エイリアス */
export type LocaleToken = typeof LOCALE_TOKEN;

/** Example 3: インターフェースで利用 */
export interface LocaleProvider {
  [LOCALE_TOKEN]: string;
}
```
