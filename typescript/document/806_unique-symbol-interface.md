# #806 「インターフェース」

四国めたん「インターフェースにunique symbolキーを含めると拡張ポイントを明示できます。」
ずんだもん「型として公開すると実装側でも同じシンボルを使えるんだね。」
四国めたん「declare constで定義したキーをインターフェースに組み込みます。」
ずんだもん「モジュール間で契約を共有するのに便利だよ。」
四国めたん「extendsで別のインターフェースに統合することも可能です。」
ずんだもん「インターフェースを通じてunique symbolを活用しよう！」
四国めたん「API設計で型を先に整えると運用が楽になります。」
ずんだもん「インターフェースを活かしてチーム開発を円滑に！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: キー宣言 */
declare const SETTINGS_TOKEN: unique symbol;

type SettingsToken = typeof SETTINGS_TOKEN;

/** Example 2: インターフェース定義 */
interface SettingsProvider {
  [SETTINGS_TOKEN]: { baseUrl: string };
}

/** Example 3: 継承 */
interface AppContext extends SettingsProvider {
  user: string;
}

const ctx: AppContext = {
  user: "mzn",
  [SETTINGS_TOKEN]: { baseUrl: "/api" },
};
```
