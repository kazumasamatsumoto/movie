# #211 「タブ Component での活用例」

## 概要
コンテンツ投影を利用してタブUIを構築し、各タブのタイトルとコンテンツを柔軟に差し込むコンポーネント設計を学びます。

## 学習目標
- タブ構造に合わせたMulti Slot Projectionの設計を理解する
- タブコンポーネントが投影されたコンテンツを切り替える仕組みを実装する
- タブ題名をInputで受け取り、本文を投影する一般的なパターンを把握する

## 技術ポイント
- **タブアイテム**: `<app-tab title="...">コンテンツ</app-tab>`形式で投影
- **レンダリング**: 子タブコンポーネントが`ng-content`で本文を表示
- **タブ一覧**: `ContentChildren`でタブ要素を取得し、シンプルなループでタブヘッダーを生成

## 📺 画面表示用コード（動画用）

```html
<app-tabs>
  <app-tab title="概要">概要コンテンツ</app-tab>
  <app-tab title="詳細">詳細コンテンツ</app-tab>
</app-tabs>
```

```typescript
@ContentChildren(TabComponent) tabs!: QueryList<TabComponent>;
```

```typescript
activate(tab: TabComponent) { ... }
```

## 💻 詳細実装例（学習用）
```typescript
// tab.component.ts
import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-tab',
  standalone: true,
  template: `<ng-content></ng-content>`,
})
export class TabComponent {
  @Input() title = '';
  active = false;
}
```

```typescript
// tabs.component.ts
import { AfterContentInit, Component, ContentChildren, QueryList } from '@angular/core';
import { TabComponent } from './tab.component';

@Component({
  selector: 'app-tabs',
  standalone: true,
  imports: [TabComponent],
  templateUrl: './tabs.component.html',
  styleUrls: ['./tabs.component.scss'],
})
export class TabsComponent implements AfterContentInit {
  @ContentChildren(TabComponent) tabs!: QueryList<TabComponent>;

  ngAfterContentInit(): void {
    const first = this.tabs.first;
    if (first) {
      this.select(first);
    }
  }

  select(tab: TabComponent): void {
    this.tabs.forEach((t) => (t.active = false));
    tab.active = true;
  }
}
```

```html
<!-- tabs.component.html -->
<nav class="tabs__header">
  <button
    type="button"
    @for (let tab of tabs; track tab.title)
    (click)="select(tab)"
    [class.active]="tab.active"
  >
    {{ tab.title }}
  </button>
</nav>
<section class="tabs__body">
  <ng-container @for (let tab of tabs; track tab.title)">
    <ng-container *ngIf="tab.active">
      <ng-container [ngTemplateOutlet]="tab.template"></ng-container>
    </ng-container>
  </ng-container>
></section>
```

```html
<!-- parent.component.html -->
<app-tabs>
  <app-tab title="概要">
    <p>概要タブの内容です。</p>
  </app-tab>
  <app-tab title="詳細">
    <p>詳細タブの内容です。</p>
  </app-tab>
</app-tabs>
```

## ベストプラクティス
- タブタイトルをInputで受け取り、本文をコンテンツ投影で提供するとAPIが明確になる
- `ContentChildren`のQueryListを`trackBy`や`changes`で監視し、動的なタブ追加にも対応する
- タブ切り替え時のアニメーションやフォーカス制御を組み込み、アクセシビリティを意識する

## 注意点
- QueryListは`ngAfterContentInit`以降に利用可能。動的追加時は`tabs.changes`で再初期化
- タブタイトルが重複するとtrackByに影響するため、識別子を付与する
- モバイルレイアウトでタブが多い場合はスクロールやドロップダウン化を検討する

## 関連技術
- `ContentChildren` / QueryList
- `ngTemplateOutlet`によるタブ内容描画
- Angular Material Tabsとの比較

