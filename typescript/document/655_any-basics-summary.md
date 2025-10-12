# #655 「any型の基本まとめ」

四国めたん「any型の基本ポイントを整理しましょう」
ずんだもん「型チェック無効、何でも代入OK、最後の手段、この三点だね」
四国めたん「はい。暗黙的anyを防ぐ設定と限定ユースケース管理もセットです」
ずんだもん「unknownや厳密な型を優先するのがベースラインだよ」
四国めたん「基本を押さえて安全なTypeScriptを維持しましょう」
ずんだもん「anyとの付き合い方をここで固めよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: ポイント整理 */
const basics = {
  disablesCheck: true,
  acceptsAll: true,
  lastResort: true,
} as const;

/** Example 2: 設定 */
const tsconfigSnippet = `"noImplicitAny": true`;

/** Example 3: 代替 */
const preferUnknown = (value: any): unknown => value;
```
