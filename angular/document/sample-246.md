# #246 「Angular Portal の活用」

## 概要
AngularのPortal API（Angular CDK）を利用して、コンポーネントやテンプレートを任意の場所にアタッチする方法を学びます。動的コンポーネント生成をPortalで抽象化すると、表示先を簡単に切り替えられます。

## 学習目標
- Portal概念（Portal, PortalOutlet, ComponentPortal, TemplatePortal）を理解する
- PortalModuleを用いたコンポーネント挿入の基本手順を習得する
- オーバーレイやサイドバーなどにPortalを利用するパターンを把握する

## 技術ポイント
- **ComponentPortal**: コンポーネントをPortal化し、PortalOutletへattach
- **TemplatePortal**: `ng-template`をPortalとして利用
- **PortalOutlet**: `cdkPortalOutlet`ディレクティブで定義

## 📺 画面表示用コード（動画用）

```html
<ng-template cdkPortal #templatePortal>...</ng-template>
```

```typescript
const portal = new ComponentPortal(AlertComponent);
portalOutlet.attachComponentPortal(portal);
```

```html
<ng-template [cdkPortalOutlet]="selectedPortal"></ng-template>
```

## 💻 詳細実装例（学習用）
```typescript
// portal-host.component.ts
import { Component, TemplateRef, ViewChild } from '@angular/core';
import { CdkPortal, ComponentPortal, PortalModule, TemplatePortal } from '@angular/cdk/portal';
import { AlertComponent } from './alert.component';

@Component({
  selector: 'app-portal-host',
  standalone: true,
  imports: [PortalModule, AlertComponent],
  templateUrl: './portal-host.component.html',
})
export class PortalHostComponent {
  @ViewChild(CdkPortal, { static: true })
  templatePortal!: TemplatePortal<any>;

  activePortal: ComponentPortal<AlertComponent> | TemplatePortal<any> | null = null;

  showComponent(): void {
    this.activePortal = new ComponentPortal(AlertComponent);
  }

  showTemplate(): void {
    this.activePortal = this.templatePortal;
  }

  clear(): void {
    this.activePortal = null;
  }
}
```

```html
<!-- portal-host.component.html -->
<button (click)="showComponent()">Component Portal</button>
<button (click)="showTemplate()">Template Portal</button>
<button (click)="clear()">Clear</button>

<ng-template cdkPortal>
  <p>TemplatePortal で挿入されるコンテンツです。</p>
</ng-template>

<section class="portal-surface">
  <ng-template [cdkPortalOutlet]="activePortal"></ng-template>
</section>
```

## ベストプラクティス
- Portalは表示位置を差し替えたい場合に便利。オーバーレイ表示やDock/Sidebarなどで活用する
- ComponentPortalを作成する際にInjectorを指定すると、依存注入を制御できる
- テンプレートをPortalとして再利用したい場合、`TemplatePortal`を使って一箇所に定義する

## 注意点
- PortalOutletが存在しないとattachできないため、テンプレート側で`cdkPortalOutlet`を忘れない
- ComponentPortalを繰り返しattachすると複数生成されるため、必要に応じて`detach`や`dispose`する
- PortalはCDK依存なので、`PortalModule`を忘れずにインポートする

## 関連技術
- CDK Overlay（`Overlay`サービス）との組み合わせ
- ViewContainerRefによる動的生成（#225）
- Dynamic Componentのプラグイン/ウィジェット構築（#239, #240）
