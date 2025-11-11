# #256 「型ガードとは」

四国めたん「型ガードについて学びましょう!」
ずんだもん「型ガードって何をするもの?」
四国めたん「Union型の値を、特定の型に絞り込むための仕組みです。」
ずんだもん「typeof value === 'string'みたいなチェックのこと?」
四国めたん「その通りです。条件分岐の中では、型が自動的に絞り込まれます。」
ずんだもん「stringの時だけtoUpperCase()が使えるようになるんだね!」
四国めたん「はい。カスタム型ガードを作ることもできます。」
ずんだもん「obj is Userみたいな戻り値の型述語で、型を保証するのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: Union型の例 */
function processValue(value: string | number) {
  if (typeof value === 'string') {
    // この中ではstring型として扱われる
    console.log(value.toUpperCase());
  } else {
    // この中ではnumber型として扱われる
    console.log(value.toFixed(2));
  }
}

/** Example 2: 型ガードの効果 */
type User = { name: string; age: number };
function isUser(obj: unknown): obj is User {
  return typeof obj === 'object' && obj !== null &&
    'name' in obj && 'age' in obj;
}
```
