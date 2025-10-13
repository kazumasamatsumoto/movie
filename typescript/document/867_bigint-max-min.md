# #867 「最大値・最小値」

四国めたん「bigint配列の最大値・最小値を求めるにはreduceを使いましょう。」
ずんだもん「Math.maxはbigintに対応してないんだね。」
四国めたん「はい、独自に比較ロジックを書きます。」
ずんだもん「空配列の処理や初期値設定も忘れずに。」
四国めたん「ユーティリティを作って再利用すると便利です。」
ずんだもん「BigIntの範囲でも安全に extrema を求めよう！」
四国めたん「比較関数を流用するとコードがシンプルになります。」
ずんだもん「最大・最小を丁寧に計算してね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 最大値 */
function maxBigint(values: bigint[]): bigint | null {
  return values.length === 0
    ? null
    : values.reduce((max, cur) => (cur > max ? cur : max));
}

/** Example 2: 最小値 */
function minBigint(values: bigint[]): bigint | null {
  return values.length === 0
    ? null
    : values.reduce((min, cur) => (cur < min ? cur : min));
}

/** Example 3: 使用 */
const sample = [10n, 5n, 20n];
console.log(maxBigint(sample), minBigint(sample));
```
