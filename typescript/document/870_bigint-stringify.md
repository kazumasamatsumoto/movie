# #870 「文字列変換」

四国めたん「bigintを文字列化するにはtoStringを使います。」
ずんだもん「toString(16)で16進数にもできるんだね。」
四国めたん「はい、桁区切りは自分で挿入する必要があります。」
ずんだもん「テンプレートリテラルに埋め込むだけでも安全に表示できるよ。」
四国めたん「ロケール対応が必要な場合はIntl.NumberFormatと文字列化を組み合わせます。」
ずんだもん「文字列変換で人間向け表示を整えよう！」
四国めたん「JSONに載せるときも文字列が安全です。」
ずんだもん「BigIntの文字列表現をマスターしてね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 基本toString */
const big = 12345678901234567890n;
console.log(big.toString());

/** Example 2: 基数指定 */
console.log(big.toString(16));

/** Example 3: Intlフォーマット */
const formatted = new Intl.NumberFormat("ja-JP").format(Number(big % 1_000_000_000_000_000n));
```
