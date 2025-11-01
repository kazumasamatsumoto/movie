# #685 「anyから適切な型へ」

四国めたん「unknown化の次は具体的な型へ落とし込む段階です」
ずんだもん「ドメインDTOやinterfaceを定義してデータ構造を固定するんだね」
四国めたん「はい。型定義ができればIDE補完とリファクタが一気に楽になります」
ずんだもん「スキーマやテーブル定義から型を生成するのも手だよ」
四国めたん「適切な型に置き換えることで保守性が劇的に向上します」
ずんだもん「ドメイン知識を型に反映させよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: DTO定義 */
interface OrderDto {
  id: string;
  total: number;
  items: Array<{ sku: string; qty: number }>;
}

/** Example 2: 変換 */
function toOrderDto(value: unknown): OrderDto {
  if (typeof value !== "object" || value === null) throw new TypeError("Order expected");
  const record = value as Record<string, unknown>;
  return {
    id: String(record.id),
    total: Number(record.total ?? 0),
    items: Array.isArray(record.items) ? record.items as OrderDto["items"] : [],
  };
}

/** Example 3: 型生成ツール */
// npx openapi-typescript schema.yaml -o src/types/api.d.ts
```
