# #659 「型チェック無効化が招く影響」

四国めたん「anyが型チェックを無効化することで静的保証が失われます」
ずんだもん「lintやIDEの警告も消えるから見落としが増えるんだよね」
四国めたん「はい。コンパイルエラーで気付けたはずの問題が本番まで流出します」
ずんだもん「結果としてテストやQAへの負担も大きくなるよ」
四国めたん「型チェックを活かすにはanyを使わないことから始めましょう」
ずんだもん「静的保証を味方にする開発を目指そう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 静的保証なし */
const user: any = {};
user.profile.name.toUpperCase(); // コンパイルOK、実行時エラー

/** Example 2: IDE補完無し */
function sendEmail(client: any) {
  client.sned(); // typo
}

/** Example 3: unknownに変換 */
function ensureUnknown<T>(value: T): unknown {
  return value;
}
```
