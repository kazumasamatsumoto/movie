# #231 「ng-template + ViewContainerRef」

## 概要
`ng-template`と`ViewContainerRef`を組み合わせて、テンプレートを手動で挿入・削除する方法を学び、構造ディレクティブと同じ仕組みを利用した柔軟な描画制御を実装します。

## 学習目標
- `TemplateRef`と`ViewContainerRef.createEmbeddedView()`の関係を理解する
- `ng-template`を親から受け取り、任意の場所に描画する手順を習得する
- 動的にテンプレートを切り替えたり、再描画する方法を把握する

## 技術ポイント
- **TemplateRef取得**: `@ViewChild('tmpl', { static: true }) template!: TemplateRef<unknown>;`
- **ビュー作成**: `viewContainerRef.createEmbeddedView(template)`
- **クリア**: `viewContainerRef.clear()`で挿入済みビューを削除

## 📺 画面表示用コード（動画用）

```html
<ng-template #tmpl>
  <p>テンプレートから描画されました</p>
</ng-template>
```

```typescript
this.host.createEmbeddedView(this.template);
```

```typescript
this.host.clear();
```

## 💻 詳細実装例（学習用）
```typescript
// template-viewer.component.ts
import { Component, TemplateRef, ViewChild, ViewContainerRef } from '@angular/core';

@Component({
  selector: 'app-template-viewer',
  standalone: true,
  templateUrl: './template-viewer.component.html',
})
export class TemplateViewerComponent {
  @ViewChild('tmpl', { static: true })
  template!: TemplateRef<unknown>;

  @ViewChild('host', { read: ViewContainerRef, static: true })
  host!: ViewContainerRef;

  render(): void {
    this.host.clear();
    this.host.createEmbeddedView(this.template);
  }
}
```

```html
<!-- template-viewer.component.html -->
<button (click)="render()">描画</button>
<ng-template #tmpl>
  <p>ng-template と ViewContainerRef の組み合わせ例です。</p>
</ng-template>
<ng-container #host></ng-container>
```

## ベストプラクティス
- TemplateRefを受け取るコンポーネントやディレクティブを作成し、再利用可能な構造を提供する
- `createEmbeddedView`は一度作成したビューを再利用できるため、必要に応じて参照を保持する
- `ngTemplateOutlet`で表現できる場合はそちらを優先するとコードが簡潔になる

## 注意点
- TemplateRefがnullの場合に備えてnullチェックを行う
- 生成したEmbeddedViewを明示的にdestroyする場合は`EmbeddedViewRef.destroy()`を呼ぶ
- TemplateRefが親から渡される場合、`@ContentChild`を利用する（#204, #205）

## 関連技術
- `ngTemplateOutlet`（#205）
- Dynamic Components（#221〜#225）
- Content ProjectionとTemplateRefの取得（#204, #207）
