# #626 「型変換パターン」

四国めたん「unknownを目的の型へ変換するパターンを整理しましょう」
ずんだもん「ガード→map、スキーマ→parse、アサーション→fallbackだね」
四国めたん「はい。状況に応じて使い分けることで安全性と可読性が両立します」
ずんだもん「共通ユーティリティを作ると繰り返しが減るよ」
四国めたん「変換パターンをライブラリ化するとプロジェクト全体が恩恵を受けます」
ずんだもん「再利用可能な型変換を整備しよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: ガード→map */
function mapIfString<T>(value: unknown, map: (text: string) => T): T | null {
  return typeof value === "string" ? map(value) : null;
}

/** Example 2: スキーマ→parse */
import { z } from "zod";
const ProductSchema = z.object({ id: z.number(), price: z.number() });
const product = ProductSchema.parse(JSON.parse("{\"id\":1,\"price\":100}"));

/** Example 3: アサーション→fallback */
function coerceNumber(value: unknown, fallback: number): number {
  if (typeof value === "number") return value;
  const parsed = Number(value);
  return Number.isFinite(parsed) ? parsed : fallback;
}
```
