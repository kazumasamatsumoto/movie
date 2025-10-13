# #810 「unique symbolまとめ」

四国めたん「unique symbolは特定のシンボル値を型で表す仕組みでした。」
ずんだもん「const宣言やconstアサーションで推論を固定するのがコツだよ。」
四国めたん「判別プロパティやブランド型で型安全性が上がります。」
ずんだもん「トークン管理やDIにも欠かせない存在になったね。」
四国めたん「型定義とインターフェースで共有方法を整えましょう。」
ずんだもん「ベストプラクティスを守れば衝突知らずだよ。」
四国めたん「symbol章の集大成として理解を固めてください。」
ずんだもん「次のテーマでも型安全を追求していこう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: トークン */
const TOKENS = {
  CONFIG: Symbol("CONFIG"),
} as const;

/** Example 2: 判別ユニオン */
const RUN = Symbol("run");
const STOP = Symbol("stop");
type Action =
  | { type: typeof RUN }
  | { type: typeof STOP };

/** Example 3: ブランド */
declare const ORDER_ID_BRAND: unique symbol;
type OrderId = string & { readonly [ORDER_ID_BRAND]: true };
```
