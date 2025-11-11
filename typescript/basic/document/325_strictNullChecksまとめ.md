# #325 「strictNullChecksまとめ」

四国めたん「strictNullChecksのまとめをしましょう!」
ずんだもん「strictモードで全て有効にするんだね!」
四国めたん「はい。strictをtrueにすればstrictNullChecksも有効になります。」
ずんだもん「型安全なコードを書くことが大切だよね?」
四国めたん「その通りです。nullチェックとデフォルト値で安全に処理します。」
ずんだもん「実践パターンも覚えたんだね!」
四国めたん「はい。オプショナルチェーンとNullish Coalescingを組み合わせます。」
ずんだもん「strictNullChecksでnullセーフなコードを書くのだ!」

---


```typescript
/** Example 1: 必須設定 */
{
  "compilerOptions": {
    "strict": true  // strictNullChecksも有効
  }
}

/** Example 2: 型安全なコード */
function process(value: string | null): string {
  if (value === null) return "default";
  return value.toUpperCase();
}

/** Example 3: 実践パターン */
const user = getUser();
const name = user?.name ?? "Guest";
if (user !== null) {
  console.log(user.email);
}
```
