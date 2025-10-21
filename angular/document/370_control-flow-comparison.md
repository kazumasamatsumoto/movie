# #370 「従来構文との違い」

## 概要
従来の`*ngIf`/`*ngFor`/`*ngSwitch`と新しいControl Flow構文を比較すると、可読性・最適化・APIの違いが見えてくる。

## 学習目標
- 新旧構文の差異と互換性を理解する
- プロジェクトでの移行戦略を考える
- 一貫したテンプレートスタイルを選択できるようになる

## 技術ポイント
- 新構文はブロック記法、旧構文は属性ベース
- Control Flow構文はデフォルトでtrack句を推奨し最適化が進む
- 旧構文も引き続きサポートされ、併用が可能

## 📺 画面表示用コード（動画用）
```html
<!-- 従来 -->
<li *ngFor="let item of items">{{ item }}</li>
<!-- 新構文 -->
@for (item of items) { <li>{{ item }}</li> }
```

## 💻 詳細実装例（学習用）
```typescript
@Component({
  selector: 'app-control-flow-compare',
  standalone: true,
  imports: [CommonModule],
  template: `
    <!-- 従来構文 -->
    <ul>
      <li *ngFor="let item of legacy">{{ item }}</li>
    </ul>

    <!-- 新構文 -->
    <ul>
      @for (item of modern; track item) {
        <li>{{ item }}</li>
      }
    </ul>
  `
})
export class ControlFlowCompareComponent {
  protected legacy = ['A', 'B', 'C'];
  protected modern = ['A', 'B', 'C'];
}
```

## ベストプラクティス
- 新構文を採用する場合はガイドラインを作成し、移行計画を明文化する
- 既存テンプレートは段階的に移行し、一括置換によるリスクを避ける
- コンポーネントごとに新旧が混在しないようにレビューで統制する

## 注意点
- 新構文導入時はビルド設定とツールチェーンが対応しているか確認する
- Control Flow構文のtrack句を省略すると警告が出る場合がある
- ドキュメントやチーム教育を通じて新しい記法を周知徹底する

## 関連技術
- Angular Upgrade Guides
- Control Flow RFC
- Team Coding Guidelines
