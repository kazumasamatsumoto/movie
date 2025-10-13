# #994 「ベストプラクティス」

四国めたん「配列ループのベストプラクティスを押さえましょう。」
ずんだもん「for...ofで要素型を活かす、filter/map/reduceで抽象化、for...inは避ける、だったね。」
四国めたん「はい、ロジックを関数に抽出して再利用しやすくしましょう。」
ずんだもん「境界チェックや型ガードも忘れずに。」
四国めたん「ベストプラクティスを守って読みやすく安全なループを書いてください。」
ずんだもん「型と実装を両立させよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: for...of */
for (const item of items) {
  console.log(item);
}

/** Example 2: 関数抽出 */
function mapValues<T, U>(values: T[], mapper: (value: T) => U): U[] {
  return values.map(mapper);
}

/** Example 3: 安全アクセス */
function firstOrUndefined<T>(values: T[]): T | undefined {
  return values.length ? values[0] : undefined;
}
```
