# #283 「nullの代入」

四国めたん「nullの代入について学びましょう!」
ずんだもん「string | null型の変数にはnullと文字列の両方を代入できるんだね!」
四国めたん「はい。name = "Alice"でもname = null;でも大丈夫です。」
ずんだもん「strictNullChecksが有効だと制限が厳しくなるんだね!」
四国めたん「その通りです。number型にnullを代入するとエラーになります。」
ずんだもん「number | nullと明示的に宣言する必要があるのだ!」
四国めたん「はい。関数パラメータやオブジェクトのプロパティでもよく使います。」
ずんだもん「User | nullでユーザー情報をクリアできるのだ!」

---

## 📺 画面表示用コード

```typescript
// nullの代入
let name: string | null = null;
name = "Alice";  // OK
name = null;     // OK
```

```typescript
// strictNullChecks有効時
let id: number = null;  // エラー
let id: number | null = null;  // OK
```

```typescript
// 関数パラメータとオブジェクト
function setUser(user: User | null): void {
  currentUser = user;
}
interface Config {
  cache: CacheService | null;
}
```
