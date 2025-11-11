# #315 「有効にすべき理由」

四国めたん「strictNullChecksを有効にすべき理由について学びましょう!」
ずんだもん「どんなメリットがあるの?」
四国めたん「はい。nullポインタ例外を未然に防ぐことができます。」
ずんだもん「nullチェックを強制されるから、実行時エラーが減るんだね!」
四国めたん「その通りです。エディタの補完も改善され、開発体験が向上します。」
ずんだもん「nullチェック後は型が絞り込まれて補完が効くの?」
四国めたん「はい。バグの早期発見にもつながり、より堅牢なコードを書けます。」
ずんだもん「process(null)のような危険な呼び出しがコンパイルエラーになるのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: nullポインタ例外を防ぐ */
function getLength(str: string | null): number {
  if (str === null) return 0;
  return str.length; // 安全
}

/** Example 2: エディタ補完の改善 */
const user: User | null = getUser();
if (user !== null) {
  user.name; // 補完が効く
}

/** Example 3: バグの早期発見 */
function process(data: string) {
  return data.toUpperCase();
}
process(null); // コンパイルエラー
```
