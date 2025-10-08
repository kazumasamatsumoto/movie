# #202 「動的コンテンツ投影」

## 概要
テンプレートを動的に切り替えて投影する方法を学び、親コンポーネントが複数の`ng-template`を状況に応じて差し込む実装パターンを理解します。

## 学習目標
- `ng-template`と`TemplateRef`で動的な投影を実装する
- `ngTemplateOutlet`や`ViewContainerRef`を使った描画制御を習得する
- 親コンポーネントでテンプレートを切り替えるUXパターンを把握する

## 技術ポイント
- **TemplateRefの受け渡し**: `@Input() content?: TemplateRef<unknown>;`
- **描画**: `<ng-container [ngTemplateOutlet]="content || defaultTpl"></ng-container>`
- **動的切り替え**: 親側で`*ngIf`やボタン操作に応じて別テンプレートを渡す

## 📺 画面表示用コード（動画用）

```html
<ng-container [ngTemplateOutlet]="template"></ng-container>
```

```typescript
@Input() template?: TemplateRef<unknown>;
```

```html
<app-dynamic [template]="activeTpl"></app-dynamic>
```

## 💻 詳細実装例（学習用）
```typescript
// dynamic-container.component.ts
import { Component, Input, TemplateRef } from '@angular/core';

@Component({
  selector: 'app-dynamic-container',
  standalone: true,
  templateUrl: './dynamic-container.component.html',
})
export class DynamicContainerComponent {
  @Input() template?: TemplateRef<unknown>;
}
```

```html
<!-- dynamic-container.component.html -->
<ng-container *ngIf="template; else defaultTpl" [ngTemplateOutlet]="template"></ng-container>
<ng-template #defaultTpl>
  <p>デフォルトテンプレートが表示されます。</p>
></ng-template>
```

```html
<!-- parent.component.html -->
<ng-template #listTpl>
  <ul>
    <li>テンプレートA</li>
    <li>テンプレートAのアイテム</li>
  </ul>
</ng-template>

<ng-template #gridTpl>
  <div class="grid">
    <div>テンプレートB-1</div>
    <div>テンプレートB-2</div>
  </div>
</ng-template>

<button (click)="active = 'list'">リスト表示</button>
<button (click)="active = 'grid'">グリッド表示</button>

<app-dynamic-container [template]="active === 'list' ? listTpl : gridTpl"></app-dynamic-container>
```

## ベストプラクティス
- 親でテンプレート参照を管理し、子は描画だけ担当することで責務を分離する
- `ngTemplateOutletContext`でテンプレートに値を渡すとさらに柔軟性が上がる
- デフォルトテンプレートを用意し、テンプレート未設定時の挙動を明確にする

## 注意点
- TemplateRefはライフサイクルによって変化するため、`ngAfterViewInit`以降に参照が安定する
- 大量に切り替える場合は描画コストを測定し、必要に応じてキャッシュを検討する
- `ngTemplateOutlet`は影響するChange Detectionを意識し、不要な再描画を避ける

## 関連技術
- `ngTemplateOutlet`詳細（#205）
- `ContentChild`でTemplateRefを取得
- `ViewContainerRef.createEmbeddedView`

