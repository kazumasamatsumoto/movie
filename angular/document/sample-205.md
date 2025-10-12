# #205 「ngTemplateOutlet の活用」

## 概要
`ngTemplateOutlet`ディレクティブを使って、`TemplateRef`を任意の場所・タイミングで描画する方法を学び、動的なテンプレート切り替えをシンプルに実現します。

## 学習目標
- `ngTemplateOutlet`の構文と`ngTemplateOutletContext`の使い方を理解する
- TemplateRefを外部から入力して表示するコンポーネントを実装する
- コンテンツ投影と`ngTemplateOutlet`の使い分けを把握する

## 技術ポイント
- **基本構文**: `<ng-container [ngTemplateOutlet]="template"></ng-container>`
- **contextの設定**: `[ngTemplateOutletContext]="{ $implicit: item }"`
- **複数テンプレート**: 親が`ng-template`を切り替えて渡すことで、表示内容を動的に変更

## 📺 画面表示用コード（動画用）

```html
<ng-container [ngTemplateOutlet]="template" [ngTemplateOutletContext]="context"></ng-container>
```

```html
<ng-template #list let-items>
  <ul>
    <li @for (it of items; track it)>{{ it }}</li>
  </ul>
</ng-template>
```

```html
<app-renderer [template]="list" [context]="{ $implicit: data }"></app-renderer>
```

## 💻 詳細実装例（学習用）
```typescript
// template-renderer.component.ts
import { Component, Input, TemplateRef } from '@angular/core';

@Component({
  selector: 'app-template-renderer',
  standalone: true,
  templateUrl: './template-renderer.component.html',
})
export class TemplateRendererComponent<T = unknown> {
  @Input() template?: TemplateRef<T>;
  @Input() context?: T;
}
```

```html
<!-- template-renderer.component.html -->
<ng-container *ngIf="template" [ngTemplateOutlet]="template" [ngTemplateOutletContext]="context"></ng-container>
```

```html
<!-- parent.component.html -->
<ng-template #list let-items>
  <ul>
    <li @for (item of items; track item)>{{ item }}</li>
  </ul>
</ng-template>

<ng-template #grid let-items>
  <div class="grid">
    <div @for (item of items; track item)>{{ item }}</div>
  </div>
</ng-template>

<button (click)="mode = 'list'">リスト</button>
<button (click)="mode = 'grid'">グリッド</button>

<app-template-renderer [template]="mode === 'list' ? list : grid" [context]="{ $implicit: data }"></app-template-renderer>
```

## ベストプラクティス
- contextを使ってテンプレート内に値を渡し、汎用性の高いテンプレートを設計する
- `ngTemplateOutlet`はDirectiveとして簡潔に利用できるため、ViewContainerRefを直接扱うより読みやすい
- TemplateRefのnullチェックを行い、テンプレート未設定時のフォールバックを用意する

## 注意点
- TemplateRefは`ngAfterViewInit`以降で利用可能。早いタイミングで参照するとundefinedになる
- contextオブジェクトのキー`$implicit`には暗黙の値を渡せるが、命名済みプロパティも併用できる
- 再描画するたびにビューが再生成されるため、重い処理の場合はキャッシュや`trackBy`を検討する

## 関連技術
- `ng-template`とTemplateRef
- `ViewContainerRef.createEmbeddedView`
- コンテンツ投影（`ng-content`）との使い分け


