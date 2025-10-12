# #201 「条件付きコンテンツ投影」

## 概要
コンテンツ投影に条件分岐を組み込み、投影されたコンテンツが存在する場合としない場合で表示内容を切り替える方法を学びます。

## 学習目標
- `ContentChild`や`ng-template`を利用した条件付き投影の実装方法を理解する
- 親側の状態に応じて投影する/しないを制御する手順を習得する
- フォールバックコンテンツと組み合わせたパターンを把握する

## 技術ポイント
- **投影有無の判定**: `ContentChild`でTemplateRefが存在するかチェック
- **条件付き表示**: `*ngIf`や`ngTemplateOutlet`で表示/非表示を切り替える
- **親制御**: 親が*ngIfで渡す要素を切り替えることで投影状態を制御

## 📺 画面表示用コード（動画用）

```html
<ng-container *ngIf="hasHeader; else defaultHeader">
  <ng-content select="[panel-header]"></ng-content>
></ng-container>
```

```typescript
@ContentChild('panelHeader', { read: TemplateRef })
headerTemplate?: TemplateRef<unknown>;
```

```html
<ng-template #defaultHeader>デフォルトヘッダー</ng-template>
```

## 💻 詳細実装例（学習用）
```typescript
// conditional-panel.component.ts
import { AfterContentInit, Component, ContentChild, TemplateRef } from '@angular/core';

@Component({
  selector: 'app-conditional-panel',
  standalone: true,
  templateUrl: './conditional-panel.component.html',
  styleUrls: ['./conditional-panel.component.scss'],
})
export class ConditionalPanelComponent implements AfterContentInit {
  @ContentChild('panelHeader', { read: TemplateRef })
  panelHeader?: TemplateRef<unknown>;

  hasHeader = false;

  ngAfterContentInit(): void {
    this.hasHeader = !!this.panelHeader;
  }
}
```

```html
<!-- conditional-panel.component.html -->
<article class="panel">
  <header class="panel__header">
    <ng-container *ngIf="hasHeader; else defaultHeader">
      <ng-content select="[panel-header]"></ng-content>
    </ng-container>
    <ng-template #defaultHeader>
      <h3>デフォルトのヘッダー</h3>
    </ng-template>
  </header>
  <section class="panel__body">
    <ng-content></ng-content>
  </section>
</article>
```

```html
<!-- parent.component.html -->
<app-conditional-panel>
  <!-- ヘッダーあり -->
  <div panel-header>
    <h2>カスタムヘッダー</h2>
  </div>
  <p>本文コンテンツ</p>
</app-conditional-panel>

<app-conditional-panel>
  <!-- ヘッダーなしでフォールバック表示 -->
  <p>ヘッダーを投影しない場合</p>
</app-conditional-panel>
```

## ベストプラクティス
- 投影が必須でない場合はフォールバックコンテンツを用意し、表示崩れを防ぐ
- 条件ロジックをコンポーネント側にまとめ、テンプレートにはシンプルな`*ngIf`だけ記述する
- ドキュメントで「投影が不要な場合の挙動」を明記し、利用者に安心感を与える

## 注意点
- `ContentChild`は`ngAfterContentInit`以降で値が確定するため、`ngOnInit`では参照できない
- *ngIfで親から渡す要素を切り替えるとき、DOM再構築が発生するのでパフォーマンスを考慮する
- 複雑な分岐が必要な場合は専用ディレクティブやサービスでロジックを分離する

## 関連技術
- `ngTemplateOutlet`によるテンプレート挿入
- `@ContentChild`とライフサイクル (`ngAfterContentInit`)
- Empty Stateパターン（#200）


