# #275 「Component の命名戦略」

## 概要
コンポーネントの命名戦略は、役割や階層がひと目で分かる命名規則を定め、チーム全体で一貫した命名を維持するためのガイドである。

## 学習目標
- 命名規則を策定する際の基準を理解する
- ファイル名とクラス名の整合性を取る
- 命名規則をディレクトリ構成と連動させる

## 技術ポイント
- 接尾辞で責務を明示（`Container`, `View`, `Dialog`）
- Feature接頭辞で機能を区別
- 命名規約文書の作成

## 📺 画面表示用コード（動画用）
```typescript
export const COMPONENT_SUFFIXES = ['Container', 'View', 'Dialog'] as const;
```

```typescript
export function toComponentName(feature: string, role: typeof COMPONENT_SUFFIXES[number]) {
  return `${feature}${role}Component`;
}
```

```typescript
const name = toComponentName('Invoice', 'Container');
```

## 💻 詳細実装例（学習用）
```markdown
| 役割 | サフィックス | 例 |
| ---- | ----------- | --- |
| ロジック調停 | Container | `InvoiceContainerComponent` |
| 表示専用 | View | `InvoiceViewComponent` |
| モーダル | Dialog | `InvoiceDialogComponent` |
```

## ベストプラクティス
- 役割を示す接尾辞を統一し、ファイル名とクラス名を揃える
- 命名規則をADRやスタイルガイド化して共有する
- Lintやスキャフォールドで命名規則を自動化する

## 注意点
- 省略形はチーム内で意味が共有できるものに限定する
- 命名規則を変更する際は既存コンポーネントのリネームを計画する
- ディレクトリ階層と命名に矛盾がないか確認する

## 関連技術
- Angular CLIスキャフォールド
- ADR (Architecture Decision Record)
- Lintルール
