# #222 「ViewContainerRef の基本」

## 概要
動的コンポーネントやテンプレートを挿入するためのアンカーである`ViewContainerRef`の仕組みを理解し、ビュー生成・削除を行う基礎を学びます。

## 学習目標
- ViewContainerRefの取得方法と役割を説明できる
- `createComponent`や`createEmbeddedView`でビューを挿入する手順を習得する
- ビューの削除やクリアなど基本操作を把握する

## 技術ポイント
- **取得方法**: `@ViewChild('anchor', { read: ViewContainerRef })`
- **ビュー生成**: `viewContainerRef.createComponent()` / `createEmbeddedView()`
- **管理**: `clear()`, `remove(index)`, `length`でビューを管理

## 📺 画面表示用コード（動画用）

```html
<ng-container #anchor></ng-container>
```

```typescript
@ViewChild('anchor', { read: ViewContainerRef, static: true })
anchor!: ViewContainerRef;
```

```typescript
this.anchor.createComponent(AlertComponent);
```

## 💻 詳細実装例（学習用）
```typescript
// view-container-demo.component.ts
import { Component, TemplateRef, ViewChild, ViewContainerRef } from '@angular/core';

@Component({
  selector: 'app-view-container-demo',
  standalone: true,
  templateUrl: './view-container-demo.component.html',
})
export class ViewContainerDemoComponent {
  @ViewChild('anchor', { read: ViewContainerRef, static: true })
  anchor!: ViewContainerRef;

  @ViewChild('tmpl', { static: true })
  template!: TemplateRef<unknown>;

  addTemplate(): void {
    this.anchor.createEmbeddedView(this.template);
  }

  clear(): void {
    this.anchor.clear();
  }
}
```

```html
<!-- view-container-demo.component.html -->
<button (click)="addTemplate()">テンプレート挿入</button>
<button (click)="clear()">クリア</button>

<ng-template #tmpl>
  <p>ViewContainerRefで生成されたビューです。</p>
</ng-template>

<ng-container #anchor></ng-container>
```

## ベストプラクティス
- ViewContainerRefを扱うディレクティブを作り、使い回せるように設計する
- ビューを追加する前に`clear()`で整理し、不要なビューが残らないようにする
- 複数ビューを管理する場合は`ComponentRef`/`EmbeddedViewRef`を配列に保持し、削除時にdestroyする

## 注意点
- `@ViewChild`で取得するときは`{ read: ViewContainerRef }`を忘れない
- 動的生成したビューはChange Detectionの対象になるため、必要に応じてChangeDetectorRefで制御する
- SSRではDOMアクセスが制限されるため、プラットフォーム判定が必要なケースがある

## 関連技術
- `createComponent()`新API（#224）
- `createEmbeddedView()`と`ng-template`（#231）
- Angular CDK Portal（#246, #247）
