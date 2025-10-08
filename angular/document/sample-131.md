# #131 「ViewChild - 子要素への参照」

## 概要
Angularの`@ViewChild`デコレータを使い、コンポーネントのテンプレート内にある要素やコンポーネントをクラスから参照する基本概念を学びます。

## 学習目標
- ViewChildでDOM要素やコンポーネントを参照する仕組みを理解する
- テンプレート参照変数を用いた参照方法を把握する
- 取得した参照を安全に扱うためのベストプラクティスを身につける

## 技術ポイント
- **@ViewChild**: テンプレート内の単一要素を取得
- **ElementRef**: DOM要素へのアクセスをラップするクラス
- **Renderer2**: 直接DOM操作を避けるための抽象化API（推奨）

## 📺 画面表示用コード（動画用）
**表示ルール**: 最大3個、各10行以内、動画で見せる部分のみ

```html
<canvas #preview></canvas>
```

```typescript
@ViewChild('preview')
previewCanvas?: ElementRef<HTMLCanvasElement>;
```

```typescript
this.previewCanvas?.nativeElement.getContext('2d');
```

## 💻 詳細実装例（学習用）
```typescript
// preview.component.ts
import { AfterViewInit, Component, ElementRef, ViewChild } from '@angular/core';

@Component({
  selector: 'app-preview',
  standalone: true,
  templateUrl: './preview.component.html',
})
export class PreviewComponent implements AfterViewInit {
  @ViewChild('preview')
  private readonly previewCanvas?: ElementRef<HTMLCanvasElement>;

  ngAfterViewInit(): void {
    const canvas = this.previewCanvas?.nativeElement;
    if (!canvas) {
      return;
    }
    const context = canvas.getContext('2d');
    if (!context) {
      return;
    }
    context.fillStyle = '#7cb342';
    context.fillRect(10, 10, 180, 80);
  }
}
```

```html
<!-- preview.component.html -->
<canvas #preview width="200" height="100"></canvas>
```

```typescript
// parent.component.ts
import { Component } from '@angular/core';
import { PreviewComponent } from './preview.component';

@Component({
  selector: 'app-dashboard',
  standalone: true,
  imports: [PreviewComponent],
  template: `
    <h2>サムネイルプレビュー</h2>
    <app-preview></app-preview>
  `,
})
export class DashboardComponent {}
```

## ベストプラクティス
- DOM操作が必要な場合でも可能ならRenderer2を利用し、プラットフォーム依存コードを避ける
- 参照は`ngAfterViewInit`でアクセスし、`ngOnDestroy`で必要なクリーンアップを行う
- 型注釈を詳細に記述し、`ElementRef<HTMLCanvasElement>`のようにDOM APIを安全に利用する

## 注意点
- SSR（Angular Universal）ではDOMが存在しないため、参照を使う際はブラウザ環境か確認する
- ViewChildは初期描画後に設定されるため、`ngOnInit`内で触るとundefinedになる
- 直接DOMを触るとテストが難しくなるため、責務を最小限に保つ

## 関連技術
- `@ViewChildren`による複数要素の取得
- Renderer2とRendererFactory2
- Angularのプラットフォーム判定 `isPlatformBrowser`
