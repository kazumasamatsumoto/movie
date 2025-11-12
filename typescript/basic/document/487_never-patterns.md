# #487 「パターン」

四国めたん「neverの典型パターンを覚えましょう。」
ずんだもん「網羅性チェック、アサーション、notImplementedの3つが紹介されてたね。」
四国めたん「どれも副作用だけで終わる処理です。」
ずんだもん「使い方をテンプレ化すると再利用しやすい!」
四国めたん「必要に応じてカスタマイズしましょう。」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 網羅性チェック */
function assertNever(value: never): never {
  throw new Error(`Unhandled case: ${value}`);
}

/** Example 2: アサーション */
function assert(condition: boolean, message: string): asserts condition {
  if (!condition) throw new Error(message);
}

/** Example 3: notImplemented */
function notImplemented(feature: string): never {
  throw new Error(`${feature} is not implemented`);
}
```
