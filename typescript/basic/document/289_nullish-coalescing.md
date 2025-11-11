# #289 「nullish演算子 - ??」

四国めたん「今日はnullish演算子について学びましょう！」
ずんだもん「??演算子は、nullまたはundefinedの時だけデフォルト値を返すんだね。」
四国めたん「||演算子とは違って、0や空文字は有効な値として扱います。」
ずんだもん「falsyな値の扱いが異なるのがポイントだよ。」
四国めたん「??=代入演算子も便利に使えます。」
ずんだもん「オプショナルチェーンと組み合わせて、安全なコードを書こう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: Nullish Coalescing */
const name = userName ?? "Guest";
const port = config.port ?? 3000;
```

```typescript
/** Example 2: ||演算子との違い */
const count1 = 0 || 10;  // 10 (0はfalsy)
const count2 = 0 ?? 10;  // 0  (0はnullでない)
```

```typescript
/** Example 3: ??=代入演算子とオプショナルチェーン */
config.timeout ??= 5000;
const zip = user?.address?.zipCode ?? "N/A";
```
