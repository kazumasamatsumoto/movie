# #167 「:host-context セレクタ - 祖先条件」

## 概要
`:host-context`擬似クラスを利用して、ホスト要素の祖先に特定のクラスや条件がある場合のみスタイルを適用する方法を学びます。

## 学習目標
- `:host-context`の役割と構文を理解する
- テーマ切り替えなど祖先条件によるスタイル変更を実装できる
- `:host`との使い分けを把握する

## 技術ポイント
- **基本構文**: `:host-context(.dark-theme) { ... }`
- **複合条件**: `.dark-theme body :host { ... }` のようにセレクタ連結可能
- **用途**: グローバルクラスやレイアウトコンテキストに応じた調整

## 📺 画面表示用コード（動画用）

```scss
:host-context(.dark-theme) {
  background: #263238;
  color: #eceff1;
}
```

```typescript
renderer.addClass(document.body, 'dark-theme');
```

```scss
:host-context(.compact) {
  padding: 8px;
}
```

## 💻 詳細実装例（学習用）
```typescript
// theme-service.ts
import { Injectable, Renderer2, RendererFactory2 } from '@angular/core';

@Injectable({ providedIn: 'root' })
export class ThemeService {
  private renderer: Renderer2;

  constructor(rendererFactory: RendererFactory2) {
    this.renderer = rendererFactory.createRenderer(null, null);
  }

  enableDark(): void {
    this.renderer.addClass(document.body, 'dark-theme');
  }

  disableDark(): void {
    this.renderer.removeClass(document.body, 'dark-theme');
  }
}
```

```typescript
// themed-card.component.ts
import { Component } from '@angular/core';

@Component({
  selector: 'app-themed-card',
  standalone: true,
  templateUrl: './themed-card.component.html',
  styleUrls: ['./themed-card.component.scss'],
})
export class ThemedCardComponent {}
```

```scss
/* themed-card.component.scss */
:host {
  display: block;
  padding: 16px;
  border-radius: 12px;
  background: #fafafa;
}

:host-context(.dark-theme) {
  background: #263238;
  color: #eceff1;
}
```

## ベストプラクティス
- テーマクラスやレイアウトモードなど、祖先要素で切り替わる条件に使用する
- クラス名や条件はグローバル設計と一致させ、ドキュメントに明記する
- `:host-context`は祖先全体を探索するため、頻発する場合はパフォーマンスに注意

## 注意点
- 条件マッチはコンポーネントの祖先全体に対して行われるため、深いツリーでも影響する
- `ViewEncapsulation.None`でも`:host-context`は機能するが、適用範囲が広がる
- 祖先のクラス切り替えはRenderer2やAngular CDK Overlayなどで安全に行う

## 関連技術
- ダークモード切り替え
- CSSカスタムプロパティとテーマ制御
- Renderer2 / CDK Layout
