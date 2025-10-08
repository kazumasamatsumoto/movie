# #080 「Lifecycle での DOM 操作」

## 概要
Lifecycle Hooksを活用してAngularのテンプレート外でDOM操作を行う場合のタイミングとベストプラクティスを学びます。

## 学習目標
- DOMアクセス可能なフック（`ngAfterViewInit`など）を理解する
- Renderer2やElementRefを使った安全な操作を実装する
- 破棄時にDOM操作の副作用を元に戻す

## 技術ポイント
- **ViewChild利用**: `ngAfterViewInit`で初期化し、`ViewChild`参照を使用
- **Renderer2**: 直接DOM操作の代替でSSRにも対応
- **クリーンアップ**: `ngOnDestroy`でクラス削除やリスナー解除を行う

## 📺 画面表示用コード（動画用）
**表示ルール**: 最大3個、各10行以内、動画で見せる部分のみ

```typescript
@ViewChild('panel') panel!: ElementRef<HTMLDivElement>;
```

```typescript
ngAfterViewInit() {
  this.renderer.addClass(this.panel.nativeElement, 'active');
}
```

```typescript
ngOnDestroy() {
  this.renderer.removeClass(this.panel.nativeElement, 'active');
}
```

## 💻 詳細実装例（学習用）
```typescript
import { AfterViewInit, Component, ElementRef, OnDestroy, Renderer2, ViewChild } from '@angular/core';

@Component({
  selector: 'app-dom-controller',
  standalone: true,
  templateUrl: './dom-controller.component.html',
  styleUrls: ['./dom-controller.component.css'],
})
export class DomControllerComponent implements AfterViewInit, OnDestroy {
  @ViewChild('panel') panel?: ElementRef<HTMLDivElement>;
  private removeListener?: () => void;

  constructor(private readonly renderer: Renderer2) {}

  ngAfterViewInit(): void {
    if (!this.panel) {
      return;
    }
    const element = this.panel.nativeElement;
    this.renderer.addClass(element, 'active');
    this.removeListener = this.renderer.listen(element, 'click', () => {
      this.renderer.toggleClass(element, 'highlight', !element.classList.contains('highlight'));
    });
  }

  ngOnDestroy(): void {
    if (!this.panel) {
      return;
    }
    this.removeListener?.();
    this.renderer.removeClass(this.panel.nativeElement, 'active');
    this.renderer.removeClass(this.panel.nativeElement, 'highlight');
  }
}
```

```html
<div #panel class="panel">クリックでハイライト切替</div>
```

## ベストプラクティス
- DOM操作が必要な処理は専用ディレクティブへ切り出し、再利用性を高める
- Renderer2を使うとサーバーレンダリングやWeb Workerでも安全に動作する
- プロパティバインディングや`@HostBinding`で代替できないか常に検討する

## 注意点
- 直接`ElementRef.nativeElement`を操作するとXSSリスクがあるため必ず信頼できるデータだけを扱う
- `ngAfterViewChecked`でDOMを再操作すると描画ループを引き起こす可能性がある
- SSRではDOM APIが利用できないため`isPlatformBrowser`で分岐する

## 関連技術
- Renderer2, RendererFactory2
- `@HostListener`, `@HostBinding`
- Angular CDK OverlayやPortalモジュール
