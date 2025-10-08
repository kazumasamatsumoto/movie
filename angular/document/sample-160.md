# #160 「DOM 参照のベストプラクティス」

## 概要
ViewChild/ViewChildrenやElementRef、Renderer2などを組み合わせてDOM参照を扱う際のベストプラクティスをまとめ、安全で保守しやすいコードを書く指針を整理します。

## 学習目標
- DOM参照を扱う際の全体的なガイドラインを理解する
- ElementRefやRenderer2を適材適所で使い分ける
- テストやSSRにも対応できる防御的な実装方針を身につける

## 技術ポイント
- **取得タイミング**: ViewChildは`ngAfterViewInit`、ContentChildは`ngAfterContentInit`
- **安全な操作**: ElementRefよりRenderer2、必要に応じてDomSanitizer
- **参照管理**: QueryListの`changes`で動的な要素変化を追跡

## 📺 画面表示用コード（動画用）

```typescript
@ViewChild('panel') panel?: ElementRef<HTMLDivElement>;
```

```typescript
this.renderer.addClass(this.panel?.nativeElement, 'active');
```

```typescript
this.viewChildren.changes.subscribe(() => this.syncRefs());
```

## 💻 詳細実装例（学習用）
```typescript
// dom-manager.component.ts
import {
  AfterContentInit,
  AfterViewInit,
  Component,
  ContentChild,
  ElementRef,
  QueryList,
  Renderer2,
  ViewChild,
  ViewChildren,
} from '@angular/core';
import { ChildDirective } from './child.directive';

@Component({
  selector: 'app-dom-manager',
  standalone: true,
  imports: [ChildDirective],
  templateUrl: './dom-manager.component.html',
})
export class DomManagerComponent implements AfterViewInit, AfterContentInit {
  @ViewChild('panel') panel?: ElementRef<HTMLDivElement>;
  @ViewChildren(ChildDirective) childDirectives!: QueryList<ChildDirective>;
  @ContentChild('footer') footerTemplate?: TemplateRef<unknown>;

  constructor(private readonly renderer: Renderer2) {}

  ngAfterViewInit(): void {
    if (this.panel) {
      this.renderer.addClass(this.panel.nativeElement, 'mounted');
    }
    this.childDirectives.changes.subscribe(() => this.updateChildren());
    this.updateChildren();
  }

  ngAfterContentInit(): void {
    if (!this.footerTemplate) {
      console.warn('フッターが投影されていません');
    }
  }

  private updateChildren(): void {
    this.childDirectives.forEach((directive, index) =>
      directive.setIndex(index),
    );
  }
}
```

```typescript
// child.directive.ts
import { Directive, ElementRef, Renderer2 } from '@angular/core';

@Directive({
  selector: '[appChild]',
  standalone: true,
})
export class ChildDirective {
  constructor(
    private readonly elementRef: ElementRef<HTMLElement>,
    private readonly renderer: Renderer2,
  ) {}

  setIndex(index: number): void {
    this.renderer.setAttribute(
      this.elementRef.nativeElement,
      'data-index',
      String(index),
    );
  }
}
```

```html
<!-- dom-manager.component.html -->
<section #panel class="panel">
  <div appChild>子要素1</div>
  <div appChild>子要素2</div>
</section>
<footer>
  <ng-container
    *ngIf="footerTemplate"
    [ngTemplateOutlet]="footerTemplate"
  ></ng-container>
</footer>
```

## ベストプラクティス
- DOM参照は責務ごとにディレクティブ化し、コンポーネントをシンプルに保つ
- Renderer2やAngular CDKを利用し、直接DOM操作を避ける
- 可能な場合はViewChildを減らし、プロパティバインディングや@Outputで状態更新を行う

## 注意点
- 過剰にDOM参照へ依存するとテストが難しくなるため、ロジックを抽象化する
- SSRを考慮しないと`nativeElement`アクセスで例外が発生する
- QueryListの`changes`は頻繁に発火するため、購読解除や処理の軽量化を意識する

## 関連技術
- Angular CDK Overlay/Portal
- SignalsとViewChildの組み合わせ
- Angular Universal（SSR）でのDOM操作ガイド
