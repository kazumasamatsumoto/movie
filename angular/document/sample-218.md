# #218 「コンテンツ投影のベストプラクティス」

## 概要
コンテンツ投影を用いたコンポーネント開発でのベストプラクティスをまとめ、使いやすく拡張性の高いAPIを提供するための指針を整理します。

## 学習目標
- スロット設計・命名・フォールバックのベストプラクティスを理解する
- ドキュメントやテストを通じてコンテンツ投影の契約を明確にする
- スタイリング・アクセシビリティ・パフォーマンスを意識した設計手法を身につける

## 技術ポイント
- **スロット命名**: 役割が伝わる属性/クラス名を使用し、ドキュメント化
- **フォールバック**: 未投影時のデフォルトコンテンツと警告表示を用意
- **テスト＆ドキュメント**: ホストコンポーネントを利用したテストとサンプルコードを整備

## 📺 画面表示用コード（動画用）

```html
<ng-content select="[card-header]"></ng-content>
<ng-content></ng-content>
```

```typescript
@ContentChild('cardHeader', { read: TemplateRef }) header?: TemplateRef<unknown>;
```

```html
<p *ngIf="!header" class="hint">card-header を指定してください</p>
```

## 💻 詳細実装例（学習用）
```markdown
### ガイドライン例
- `card-header`, `card-footer`など部位を明示する属性名を採用する
- スロットは最大3〜4個に抑え、必要以上に複雑化しない
- 投影が必須なスロットはドキュメントで必須と明記し、未提供時はフォールバックを表示する
- Storybookやサンプルで典型的な使用例を提供する
```

```typescript
// best-practice-panel.component.ts
import { AfterContentInit, Component, ContentChild, TemplateRef } from '@angular/core';

@Component({
  selector: 'app-best-practice-panel',
  standalone: true,
  templateUrl: './best-practice-panel.component.html',
  styleUrls: ['./best-practice-panel.component.scss'],
})
export class BestPracticePanelComponent implements AfterContentInit {
  @ContentChild('panelHeader', { read: TemplateRef })
  panelHeader?: TemplateRef<unknown>;

  hasHeader = false;

  ngAfterContentInit(): void {
    this.hasHeader = !!this.panelHeader;
  }
}
```

```html
<!-- best-practice-panel.component.html -->
<article class="panel">
  <header class="panel__header">
    <ng-container *ngIf="hasHeader; else hint">
      <ng-content select="[panel-header]"></ng-content>
    </ng-container>
    <ng-template #hint>
      <p class="panel__hint">panel-header を指定するとヘッダーが表示されます。</p>
    </ng-template>
  </header>
  <section class="panel__body">
    <ng-content></ng-content>
  </section>
</article>
```

## ベストプラクティス
- 投影スロットとInputで構成されるAPIをドキュメント化し、利用者に期待する構造を伝える
- Storybookやサンプルアプリで想定パターンを提示し、正しい使い方を保証する
- コンテンツ投影を使いすぎると複雑化するため、Inputや別コンポーネントで代替できないか検討する
- フォールバックUIを用意し、未投影時に空のコンポーネントにならないよう配慮する

## 注意点
- スロット契約変更は破壊的変更になるため、バージョン管理やマイグレーションガイドを準備する
- 投影内容にスタイルやロジックを任せるため、アクセシビリティ方針などを共有する
- 複数レベルの投影が連鎖するとデバッグが難しくなるため、責務を分割する

## 関連技術
- コンテンツ投影の制約事項（#219）
- 投影テスト（#217）
- レイアウト/カード/モーダルでの活用例（#209〜#213）

