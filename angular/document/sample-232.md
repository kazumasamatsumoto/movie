# #232 「ComponentRef の活用」

## 概要
`ComponentRef`オブジェクトを通じて、動的に生成されたコンポーネントのインスタンス・ChangeDetectorRef・HostViewを操作する方法を学びます。

## 学習目標
- ComponentRefからアクセスできるプロパティ／メソッドを理解する
- インスタンス経由でInput、メソッド、Change Detectionを制御する手順を習得する
- HostViewを利用した挿入・移動・破棄の方法を把握する

## 技術ポイント
- **インスタンス**: `componentRef.instance`で@Inputやpublicメソッドへアクセス
- **Change Detection**: `componentRef.changeDetectorRef.detectChanges()`で手動更新
- **ビュー操作**: `componentRef.hostView`をViewContainerRefへ`insert`/`remove`可能

## 📺 画面表示用コード（動画用）

```typescript
const ref = this.host.createComponent(AlertComponent);
ref.instance.message = 'Hello';
ref.changeDetectorRef.detectChanges();
```

```typescript
this.anotherHost.insert(ref.hostView);
```

```typescript
ref.destroy();
```

## 💻 詳細実装例（学習用）
```typescript
// component-ref-demo.component.ts
import { Component, ComponentRef, ViewChild, ViewContainerRef } from '@angular/core';
import { AlertComponent } from './alert.component';

@Component({
  selector: 'app-component-ref-demo',
  standalone: true,
  imports: [AlertComponent],
  templateUrl: './component-ref-demo.component.html',
})
export class ComponentRefDemoComponent {
  @ViewChild('primary', { read: ViewContainerRef, static: true })
  primary!: ViewContainerRef;

  @ViewChild('secondary', { read: ViewContainerRef, static: true })
  secondary!: ViewContainerRef;

  alertRef?: ComponentRef<AlertComponent>;

  create(): void {
    this.alertRef = this.primary.createComponent(AlertComponent);
    this.alertRef.instance.message = 'Primary Host';
    this.alertRef.changeDetectorRef.detectChanges();
  }

  move(): void {
    if (!this.alertRef) return;
    this.secondary.insert(this.alertRef.hostView);
    this.alertRef.instance.message = 'Moved to Secondary';
    this.alertRef.changeDetectorRef.detectChanges();
  }

  destroy(): void {
    this.alertRef?.destroy();
    this.alertRef = undefined;
  }
}
```

```html
<!-- component-ref-demo.component.html -->
<button (click)="create()">生成</button>
<button (click)="move()">移動</button>
<button (click)="destroy()">破棄</button>

<section>
  <h3>Primary</h3>
  <ng-container #primary></ng-container>
</section>

<section>
  <h3>Secondary</h3>
  <ng-container #secondary></ng-container>
</section>
```

## ベストプラクティス
- ComponentRefをサービス経由で管理し、コンポーネント破棄やイベント購読解除を集中管理する
- hostViewの移動を行う際は、ViewContainerRef間の整合を保つ（元のコンテナからは自動で除外される）
- Change Detectionの頻度を制御し、必要に応じて`detectChanges()`や`markForCheck()`を呼ぶ

## 注意点
- hostViewを複数のViewContainerRefへ同時に追加することはできない。移動時は`insert`で移す
- destroy後のComponentRefやinstanceにアクセスするとエラーになるため、ガードを行う
- ComponentRefを多数保持する場合、`destroy()`を忘れるとメモリリークの原因となる

## 関連技術
- ViewContainerRef操作（#222, #230）
- 動的コンポーネントの入力・イベント（#226, #227）
- Angular CDK Portal（#246, #247）でのComponentPortal
