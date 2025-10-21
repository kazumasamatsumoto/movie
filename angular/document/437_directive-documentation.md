# #437 「Directive のドキュメント作成」

## 概要
ディレクティブのドキュメントは目的、使い方、Input/Output、注意点を明記し、利用者が即座に導入できる情報を提供する。

## 学習目標
- ドキュメントに含めるべき項目を理解する
- Markdownテンプレートを活用した記述方法を学ぶ
- 更新が必要なタイミングを把握する

## 技術ポイント
- 概要・使用例・API表・注意点・関連リンク
- READMEやStorybook Docsに組み込む
- バージョン管理で変更履歴を追跡

## 📺 画面表示用コード（動画用）
```markdown
## 使用例
```html
<button appLoadingButton [appLoadingButton]="isLoading">保存</button>
```
```

## 💻 詳細実装例（学習用）
```markdown
# app-loading-button Directive

## 概要
ボタンのローディング状態を表示し、クリック無効化とスピナー表示を行います。

## 使用例
```html
<button appLoadingButton [appLoadingButton]="isSaving">保存</button>
```

## API
| 名前 | 型 | デフォルト | 説明 |
| ---- | -- | ---------- | ---- |
| `appLoadingButton` | `boolean` | `false` | ローディング状態 |

## 注意点
- ボタン以外の要素に適用しないでください。
```

## ベストプラクティス
- Markdownテンプレートを用意し、各ディレクティブで統一フォーマットを使用
- Storybook Docsや設計書にも同じ情報を反映
- 変更時はドキュメントも更新し、PRチェックリストに含める

## 注意点
- 情報が古くなると混乱を招くためCIでリンク切れやサンプルコードを検証
- API表はテーブル形式で簡潔にまとめ、過度な説明を避ける
- 利用時の制約や互換性情報を明記する

## 関連技術
- Markdown
- Storybook Docs
- Docusaurus/Docz
