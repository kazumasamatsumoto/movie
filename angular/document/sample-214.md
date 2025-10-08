# #214 「再利用可能な Component 設計」

## 概要
コンテンツ投影を活用して、再利用性の高いコンポーネントを設計・実装する際のポイントを整理します。スロット構成、API設計、ドキュメント化などを組み合わせた実践的なアプローチを学びます。

## 学習目標
- コンテンツ投影を使った再利用コンポーネントの設計指針を理解する
- Input/Outputと投影を組み合わせたAPI設計を習得する
- ドキュメント化・テストを含めた運用面のベストプラクティスを把握する

## 技術ポイント
- **スロット設計**: 必須/任意スロット、名前付け、フォールバックを設計
- **契約明示**: 投影に必要なクラスや属性などをドキュメント化
- **テスト**: ホストコンポーネントを使って投影契約を保証する

## 📺 画面表示用コード（動画用）

```html
<app-shell>
  <nav shell-sidebar>...</nav>
  <header shell-header>...</header>
  <main>本文</main>
</app-shell>
```

```typescript
@Input() title = '';
```

```html
<ng-content></ng-content>
```

## 💻 詳細実装例（学習用）
```typescript
// shell.component.ts
import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-shell',
  standalone: true,
  templateUrl: './shell.component.html',
  styleUrls: ['./shell.component.scss'],
})
export class ShellComponent {
  @Input() title = '';
}
```

```html
<!-- shell.component.html -->
<div class="shell">
  <header class="shell__header">
    <h1>{{ title }}</h1>
    <ng-content select="[shell-header]"></ng-content>
  </header>
  <aside class="shell__sidebar">
    <ng-content select="[shell-sidebar]"></ng-content>
  </aside>
  <main class="shell__content">
    <ng-content></ng-content>
  </main>
</div>
```

```scss
/* shell.component.scss */
.shell {
  display: grid;
  grid-template-columns: 200px 1fr;
  gap: 24px;
}
```

## ベストプラクティス
- Inputで汎用的な設定（タイトル・テーマ等）を受け取り、詳細なコンテンツは投影に委ねる
- スロット名・使い方・サンプルをドキュメントにまとめて利用者に提供する
- Storybookなどのツールでコンテンツ投影パターンを可視化し、再利用を促進する

## 注意点
- 投影コンテンツが多すぎるとAPIが複雑になるため、責務を分割し必要最小限のスロットに留める
- 投影契約に変更がある場合、バージョニングや互換性に配慮する
- フォールバックを用意し、利用者が必須スロットを省略した際の挙動を明確にする

## 関連技術
- コンテンツ投影ベストプラクティス（#218）
- Storybook / ドキュメント自動生成
- テストでのホストコンポーネント利用（#217）

