# #688 「@types定義の活用」

四国めたん「DefinitelyTypedの@typesパッケージを活用するとany排除が加速します」
ずんだもん「npm install --save-dev @types/ライブラリ名で型が入るんだよね」
四国めたん「はい。型定義が更新されるのでライブラリ更新時も追従しやすいです」
ずんだもん「無い場合はissueを建てたりPRを送る選択肢もあるよ」
四国めたん「公式型を取り込むことで社内メンテナンスの負荷を減らせます」
ずんだもん「まずは@types検索から始めよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: インストール */
// pnpm add -D @types/lodash

/** Example 2: 型補完 */
import { debounce } from "lodash";
const handler = debounce(() => {}, 100); // 型付き

/** Example 3: 型がない場合のメモ */
const checklist = [
  "DefinitelyTypedを検索",
  "Issue/PRを検討",
  "暫定d.tsを作成",
] as const;
```
