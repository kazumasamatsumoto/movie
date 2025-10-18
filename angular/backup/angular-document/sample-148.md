# #148 「ContentChild 複数投影の参照」

## 概要
複数の投影コンテンツ（ヘッダー・フッターなど）を`@ContentChild`で個別に参照し、柔軟に制御する方法を学びます。

## 学習目標
- 複数のテンプレート参照変数を使ったContentChildの取得を理解する
- `read`オプションで特定の型を取得する方法を習得する
- 投影コンテンツごとのフォールバック処理を実装できるようにする

## 技術ポイント
- **複数参照**: `@ContentChild('header')`, `@ContentChild('footer')`
- **TemplateRef取得**: `{ read: TemplateRef }`でテンプレートを扱う
- **fallback**: 投影されない場合に備えてデフォルトコンテンツを用意

```typescript
@ContentChild('header', { read: TemplateRef })
header?: TemplateRef<unknown>;
```

```typescript
@ContentChild('footer', { read: TemplateRef })
footer?: TemplateRef<unknown>;
```

```html
<ng-template [ngTemplateOutlet]="header ?? defaultHeader"></ng-template>
```

## 💻 詳細実装例（学習用）
```typescript
// panel.component.ts
import { AfterContentInit, Component, ContentChild, TemplateRef } from '@angular/core';

@Component({
  selector: 'app-panel',
  standalone: true,
  templateUrl: './panel.component.html',
})
export class PanelComponent implements AfterContentInit {
  @ContentChild('panelHeader', { read: TemplateRef })
  header?: TemplateRef<unknown>;

  @ContentChild('panelFooter', { read: TemplateRef })
  footer?: TemplateRef<unknown>;

  hasHeader = false;
  hasFooter = false;

  ngAfterContentInit(): void {
    this.hasHeader = !!this.header;
    this.hasFooter = !!this.footer;
  }
}
```

```html
<!-- panel.component.html -->
<article class="panel">
  <header>
    <ng-container
      *ngIf="header; else defaultHeader"
      [ngTemplateOutlet]="header"
    ></ng-container>
  </header>
  <section>
    <ng-content></ng-content>
  </section>
  <footer>
    <ng-container
      *ngIf="footer; else defaultFooter"
      [ngTemplateOutlet]="footer"
    ></ng-container>
  </footer>
</article>

<ng-template #defaultHeader>
  <h3>デフォルトヘッダー</h3>
</ng-template>

<ng-template #defaultFooter>
  <p>デフォルトフッター</p>
</ng-template>
```

```html
<!-- parent.component.html -->
<app-panel>
  <ng-template #panelHeader>
    <h3>カスタムヘッダー</h3>
  </ng-template>
  <p>本文コンテンツ</p>
  <ng-template #panelFooter>
    <small>カスタムフッター</small>
  </ng-template>
</app-panel>
```

## ベストプラクティス
- 親に提供してもらうテンプレート参照名をわかりやすく定義し、APIとして公開する
- `ng-template`を使って明示的にテンプレートを渡すことで、構造を保守しやすくする
- 投影されない可能性を考慮し、デフォルト表示を用意する

## 注意点
- 複数のContentChildを利用する場合、同名の参照変数が衝突しないようにする
- TemplateRefを挿入する際にViewContainerRefを使う場合は`clear()`で重複挿入を防ぐ
- 複雑なコンテンツ構成では`@ContentChildren`を併用し、複数アイテムを扱いやすくする

## 関連技術
- `@ContentChildren`による複数スロットの管理
- `ngTemplateOutlet`ディレクティブ
- Angular Materialのカード/ダイアログにおける投影パターン
