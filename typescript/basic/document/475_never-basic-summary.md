# #475 「基本まとめ」

四国めたん「never型のポイントをまとめましょう。」
ずんだもん「throwか無限ループだけがneverになるんだね。」
四国めたん「fail()のように戻らない関数を定義するときに使います。」
ずんだもん「exhaustiveCheckも忘れちゃいけない!」
四国めたん「基礎を押さえれば応用もスムーズです。」
ずんだもん「neverを怖がらず使いこなすのだ!"

---

## 📺 画面表示用コード

```typescript
/** Example 1: throw */
function throwError(message: string): never {
  throw new Error(message);
}

/** Example 2: 無限ループ */
function serve(): never {
  while (true) handleRequest();
}

/** Example 3: exhaustiveCheck */
function exhaustiveCheck(value: never): never {
  throw new Error(`Unhandled: ${value}`);
}
```
