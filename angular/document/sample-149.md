# #149 「ContentChildren - 複数投影参照」

## 概要
複数の投影コンテンツを`@ContentChildren`で一括して取得し、`QueryList`を通じて管理する方法を学びます。

## 学習目標
- ContentChildrenの基本構文とQueryListの使い方を理解する
- 投影コンテンツを順番に処理したり、変化を監視する手順を習得する
- 複数スロット構成でのアクセス方法を把握する

## 技術ポイント
- **宣言**: `@ContentChildren(ItemDirective) items!: QueryList<ItemDirective>;`
- **配列操作**: QueryList経由でfilterやmapを使用
- **changes**: 投影コンテンツの追加・削除をObservableで監視

## 📺 画面表示用コード（動画用）

```html
<ng-content select="[appTab]"></ng-content>
```

```typescript
@ContentChildren(TabDirective)
tabs!: QueryList<TabDirective>;
```

```typescript
this.tabs.changes.subscribe(() => this.activateFirst());
```

## 💻 詳細実装例（学習用）
```typescript
// tab.directive.ts
import { Directive, Input } from '@angular/core';

@Directive({
  selector: '[appTab]',
  standalone: true,
})
export class TabDirective {
  @Input() title = '';
  active = false;

  activate(): void {
    this.active = true;
  }

  deactivate(): void {
    this.active = false;
  }
}
```

```typescript
// tab-group.component.ts
import { AfterContentInit, Component, ContentChildren, QueryList } from '@angular/core';
import { TabDirective } from './tab.directive';

@Component({
  selector: 'app-tab-group',
  standalone: true,
  templateUrl: './tab-group.component.html',
})
export class TabGroupComponent implements AfterContentInit {
  @ContentChildren(TabDirective)
  tabs!: QueryList<TabDirective>;

  ngAfterContentInit(): void {
    if (this.tabs.length) {
      this.activate(this.tabs.first);
    }
    this.tabs.changes.subscribe(() => {
      if (!this.tabs.some((tab) => tab.active)) {
        const first = this.tabs.first;
        if (first) {
          this.activate(first);
        }
      }
    });
  }

  activate(tab: TabDirective): void {
    this.tabs.forEach((t) => t.deactivate());
    tab.activate();
  }
}
```

```html
<!-- tab-group.component.html -->
<nav class="tab-header">
  <button
    type="button"
    @for (let tab of tabs; track tab.title)
    (click)="activate(tab)"
  >
    {{ tab.title }}
  </button>
</nav>
<section class="tab-body">
  <ng-content></ng-content>
}</section>
```

```html
<!-- parent.component.html -->
<app-tab-group>
  <article appTab title="概要">
    <p>概要コンテンツ</p>
  </article>
  <article appTab title="詳細">
    <p>詳細コンテンツ</p>
  </article>
</app-tab-group>
```

## ベストプラクティス
- QueryListの内容が変わることを想定して`changes`を購読し、UIと同期させる
- 投影コンテンツにディレクティブを付与し、APIとして扱いやすくする
- `@ContentChildren(TabDirective, { descendants: true })`でネストされた要素も取得可能

## 注意点
- ContentChildrenは投影コンテンツが存在する`ngAfterContentInit`まで利用できない
- QueryListを配列に変換した場合、最新状態を反映するには再変換が必要
- 投影コンテンツが動的に入れ替わる場合、subscribe時の購読解除を忘れない

## 関連技術
- `@ViewChildren`との違い
- `QueryList`の`changes`プロパティ
- Angular Material Tabsの実装パターン
