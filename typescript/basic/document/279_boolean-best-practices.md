# #279 「ベストプラクティス」

四国めたん「boolean型のベストプラクティスについて学びましょう!」
ずんだもん「まずは厳密等価演算子===を必ず使うんだね!」
四国めたん「はい。value === nullのように、型を明確にチェックします。」
ずんだもん「型ガードを使えば、型の安全性をさらに高められるよね?」
四国めたん「その通りです。typeof val === 'string'で型を絞り込めます。」
ずんだもん「const isActive: booleanのように明示的な型注釈も大事だね!」
四国めたん「はい。strictNullChecksとESLintの設定も必須です。」
ずんだもん「"eqeqeq": ["error", "always"]で==を禁止するのだ!」

---

## 📺 画面表示用コード

```typescript
// ✅ 厳密等価演算子の使用
if (value === null) { }

// ✅ 型ガードの活用
function isString(val: unknown): val is string {
  return typeof val === 'string';
}

// ✅ 明示的な型注釈
const isActive: boolean = true;
```

```typescript
// ✅ strictNullChecksの有効化
// tsconfig.json
// "strictNullChecks": true

// ✅ ESLint設定
// "eqeqeq": ["error", "always"]
```
