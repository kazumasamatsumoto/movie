# #732 「Symbolの歴史」

四国めたん「SymbolはECMAScript 2015で導入された比較的新しいプリミティブです。」
ずんだもん「TypeScriptは早い段階から型定義を提供してくれたんだよね。」
四国めたん「はい、lib.es2015.symbol.d.tsが入って以降、標準APIが型付きで扱えます。」
ずんだもん「古いブラウザではポリフィルが必要だった時代もあったよ。」
四国めたん「現在はモダンランタイムなら標準サポートが前提です。」
ずんだもん「v5.9でもSymbol関連ユーティリティが充実しているのが嬉しいね。」
四国めたん「歴史を知っていればトランスパイル設定の判断がしやすくなります。」
ずんだもん「互換性を意識してシンボルを導入しよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: サポート判定 */
if (typeof Symbol !== "function") {
  throw new Error("Symbol is not supported in this environment");
}

/** Example 2: ターゲット指定が必要なAPI */
class LegacyCollection {
  static [Symbol.hasInstance](value: unknown): boolean {
    return Array.isArray(value);
  }
}
console.log([] instanceof LegacyCollection); // true when Symbol.hasInstance exists

/** Example 3: tsconfigでlibを有効化 */
const tsconfig = {
  compilerOptions: {
    target: "ES2015",
    lib: ["ES2015", "DOM"],
  },
};
```
