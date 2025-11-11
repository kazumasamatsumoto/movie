# #270 「型ガードまとめ」

四国めたん「型ガードをまとめて復習しましょう!」
ずんだもん「色々な型ガードの方法があったよね!」
四国めたん「はい。typeofはプリミティブ型、instanceofはクラスで使います。」
ずんだもん「inはオブジェクトのプロパティ、Array.isArrayは配列だね!」
四国めたん「その通りです。それぞれ適切な場面で使い分けることが大切です。」
ずんだもん「型述語関数を使えばカスタム型ガードも作れるんだよね!」
四国めたん「はい。複雑な型チェックには型述語関数が便利です。」
ずんだもん「これで型安全なTypeScriptコードが書けるのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 基本的な型ガード */
// typeof - プリミティブ型
if (typeof value === 'string') { }

// instanceof - クラス
if (value instanceof Date) { }

// in - オブジェクトプロパティ
if ('name' in obj) { }

/** Example 2: 配列と型述語関数 */
// Array.isArray - 配列
if (Array.isArray(value)) { }

// 型述語関数 - カスタム型ガード
function isUser(obj: unknown): obj is User {
  return typeof obj === 'object' && obj !== null && 'name' in obj;
}
```
