# #621 「動的データの扱い方」

四国めたん「動的に生成されるデータもunknownを起点にすると安全です」
ずんだもん「例えばeval結果やCMSのコンテンツとかだね」
四国めたん「はい。ランタイムで構造が変わるものこそ型ガードで守ります」
ずんだもん「安全なドメイン型にマッピングするパターンを用意しよう」
四国めたん「動的データに対しても型システムを味方につけられます」
ずんだもん「未知のデータを怖がらず安全に扱おう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 動的データ取得 */
function fetchDynamic(): unknown {
  return window["CMS_DATA"];
}

/** Example 2: 型パターン */
type Content = { title: string; body: string };
const isContent = (value: unknown): value is Content =>
  typeof value === "object" && value !== null
  && typeof (value as Record<string, unknown>).title === "string"
  && typeof (value as Record<string, unknown>).body === "string";

/** Example 3: マッピング */
const payload = fetchDynamic();
if (isContent(payload)) render(payload);
```
