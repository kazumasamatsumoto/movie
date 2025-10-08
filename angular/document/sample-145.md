# #145 「ContentChild - 投影コンテンツ参照」

## 概要
`@ContentChild`を利用して、親コンポーネントから投影されたコンテンツ（`ng-content`）を参照し、内部で制御する方法を学びます。

## 学習目標
- ContentChildの基本的な動作と構文を理解する
- 投影されたテンプレートやコンポーネントにアクセスする手順を習得する
- コンテンツプロジェクションと参照の連携方法を把握する

## 技術ポイント
- **@ContentChild**: 親が渡すテンプレート/コンポーネントを取得
- **テンプレート参照**: 親側で`#header`などの参照名を付ける
- **ライフサイクル**: `ngAfterContentInit`で使用可能

## 📺 画面表示用コード（動画用）

```html
<ng-content select="[header]"></ng-content>
```

```typescript
@ContentChild('header')
headerTemplate?: TemplateRef<unknown>;
```

```typescript
ngAfterContentInit() {
  if (!this.headerTemplate) { ... }
}
```

## 💻 詳細実装例（学習用）
```typescript
// card.component.ts
import { AfterContentInit, Component, ContentChild, TemplateRef, ViewContainerRef } from '@angular/core';

@Component({
  selector: 'app-card',
  standalone: true,
  templateUrl: './card.component.html',
})
export class CardComponent implements AfterContentInit {
  @ContentChild('cardHeader')
  headerTemplate?: TemplateRef<unknown>;

  constructor(private readonly vcr: ViewContainerRef) {}

  ngAfterContentInit(): void {
    if (this.headerTemplate) {
      this.vcr.createEmbeddedView(this.headerTemplate);
    }
  }
}
```

```html
<!-- card.component.html -->
<section class="card">
  <header>
    <ng-container></ng-container>
  </header>
  <main>
    <ng-content></ng-content>
  </main>
</section>
```

```html
<!-- parent.component.html -->
<app-card>
  <ng-template #cardHeader>
    <h3>投影されたヘッダー</h3>
  </ng-template>
  <p>コンテンツ本文</p>
</app-card>
```

## ベストプラクティス
- 親にテンプレート参照変数の命名規則を伝え、APIとして文書化する
- `ngAfterContentInit`でnullチェックを行い、未提供時のフォールバックを用意する
- TemplateRefを挿入する際はViewContainerRefを利用し、描画位置を制御する

## 注意点
- ContentChildは自分のテンプレートには反応しない（投影分のみ）
- 投影側が*ngIfで切り替わると参照が変化するため、`ngAfterContentChecked`で確認する場合がある
- TemplateRefを挿入する際に同じViewContainerRefを再利用するとビューが重複するので注意

## 関連技術
- ContentChildrenで複数投影要素を取得
- `ng-content`とselect属性
- ViewContainerRefでのテンプレート展開
