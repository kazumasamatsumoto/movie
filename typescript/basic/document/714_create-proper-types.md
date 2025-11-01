# #714 「適切な型定義を作る」

四国めたん「anyをなくすにはドメイン知識を含んだ型定義を作ることが重要です」
ずんだもん「DTOやinterfaceでデータ構造を明示すれば安心なんだよね」
四国めたん「はい。仕様書やAPIスキーマを基に型を整備しましょう」
ずんだもん「型生成ツールを使うと最新仕様とずれにくいよ」
四国めたん「適切な型があればanyに戻る理由はなくなります」
ずんだもん「まずは型定義を資産として整えよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: ドメイン型 */
interface Customer {
  id: string;
  email: string;
  plan: "free" | "pro";
}

/** Example 2: DTO生成 */
type OrderDto = {
  id: string;
  items: Array<{ sku: string; qty: number }>;
};

/** Example 3: 型生成ツール */
// npx openapi-typescript schema.yaml -o src/types/api.d.ts
```
