# #282 「nullの宣言」

四国めたん「nullの宣言方法を学びましょう!」
ずんだもん「let value: null = null;で純粋なnull型を宣言できるんだね!」
四国めたん「はい。string | nullでnullを許容する文字列型も宣言できます。」
ずんだもん「複数の型とnullも組み合わせられるんだね!」
四国めたん「その通りです。string | number | nullのように記述します。」
ずんだもん「配列もstring[] | nullでnullを許容できるのだ!」
四国めたん「はい。tsconfig.jsonでstrictNullChecksを有効にすることが重要です。」
ずんだもん「これでnull安全性を保証できるのだ!」

---

## 📺 画面表示用コード

```typescript
// null型の宣言
let value: null = null;
let name: string | null = null;
let age: number | null = 25;
```

```typescript
// 複数の型とnull
let data: string | number | null = null;
let items: string[] | null = null;
```

```typescript
// tsconfig.json
{
  "compilerOptions": {
    "strictNullChecks": true  // null安全性
  }
}
```
