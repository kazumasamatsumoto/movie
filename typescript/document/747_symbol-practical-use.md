# #747 「ユースケース」

四国めたん「現場ではプラグイン間の衝突回避にsymbolが多用されます。」
ずんだもん「Nest.jsのGuardsやInterceptorsで専用メタデータを載せるときにも便利だよ。」
四国めたん「イベントハンドラの識別子としてもシンプルです。」
ずんだもん「ReactのContextキーやReduxのシークレットマーカーにも使われているね。」
四国めたん「アプリ設定の隠しプロパティにも向いています。」
ずんだもん「テストダブル識別子にも活用可能だよ。」
四国めたん「symbolは用途が広いのでパターンを覚えておきましょう。」
ずんだもん「実践ユースケースに落とし込んでみてね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: Nest.jsメタデータキー */
export const GUARD_META = Symbol("GUARD_META");
Reflect.defineMetadata(GUARD_META, { level: "admin" }, class AdminGuard {});

/** Example 2: イベントバス */
const EVENT_READY = Symbol("ready");
const listeners = new Map<symbol, () => void>([[EVENT_READY, () => console.log("Ready!")]]);

/** Example 3: テスト用識別子 */
const DOUBLE_MARK = Symbol("double");
const mock = { [DOUBLE_MARK]: true };
console.log(DOUBLE_MARK in mock); // true
```
