# #280 「マスターチェック」

四国めたん「boolean型のマスターチェックをしましょう!」
ずんだもん「厳密等価演算子===でvalue === nullをチェックするんだね!」
四国めたん「はい。型ガードでisUser関数を使い、型を安全に絞り込みます。」
ずんだもん「falsy値はfalse、0、空文字列、null、undefined、NaNの6つだよね?」
四国めたん「その通りです。これらを理解して正しく扱うことが重要です。」
ずんだもん「Angular/Nest.jsでは@IsBoolean()デコレータを使うんだね!」
四国めたん「はい。strictNullChecksとESLintを組み合わせるのがベストプラクティスです。」
ずんだもん「これでboolean型を完全にマスターできたのだ!」

---

## 📺 画面表示用コード

```typescript
// ✅ 厳密等価演算子
if (value === null) { }

// ✅ 型ガード
function isUser(obj: unknown): obj is User {
  return typeof obj === 'object' && obj !== null && 'name' in obj;
}

// ✅ falsy値の理解
// false, 0, '', null, undefined, NaN
```

```typescript
// ✅ Angular/Nest.jsでの実践
@IsBoolean() isActive: boolean;

// ✅ ベストプラクティス
// strictNullChecks + ESLint
```
