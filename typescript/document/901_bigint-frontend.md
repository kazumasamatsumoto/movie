# #901 「フロントエンド使用」

四国めたん「ブラウザでもBigIntは使えるのでフロント側での高精度処理が可能です。」
ずんだもん「ただし古いブラウザではサポートがないからbabel設定やpolyfill確認が必要だね。」
四国めたん「はい、ビルドターゲットをES2020以上にするのが安全です。」
ずんだもん「WebAssemblyやIndexedDBとの連携でもBigIntが活躍するよ。」
四国めたん「UI表示時は文字列にしてIntlでフォーマットしましょう。」
ずんだもん「フロントエンドでもBigIntを活用して精度を守ろう！」
四国めたん「ライトウェイトな処理に留め、重い計算はワーカーで行うのがベストです。」
ずんだもん「ブラウザサイドの活用方法を押さえてね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: tsconfig */
const tsconfig = {
  compilerOptions: {
    target: "ES2020",
  },
};

/** Example 2: Intlフォーマット */
function format(value: bigint) {
  return new Intl.NumberFormat("ja-JP").format(Number(value % 1_000_000_000_000_000n)) + "…";
}

/** Example 3: Web Worker */
const worker = new Worker("./bigint-worker.js");
worker.postMessage({ type: "sum", values: [1n, 2n, 3n].map((v) => v.toString()) });
```
