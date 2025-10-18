# #171 「CSS 変数の活用」

## 概要
CSSカスタムプロパティ（CSS変数）を利用してテーマカラーやスペーシングを管理し、Angularコンポーネントで再利用しやすいスタイル設計を行います。

## 学習目標
- CSS変数の定義と参照方法を理解する
- コンポーネントごとにCSS変数を上書きする手順を習得する
- TypeScriptからCSS変数を動的に変更する方法を把握する

## 技術ポイント
- **定義**: `:root { --color-primary: #1976d2; }`
- **参照**: `color: var(--color-primary);`
- **動的変更**: `element.style.setProperty('--color-primary', '#42a5f5');`

```scss
:root {
  --color-primary: #1976d2;
}
```

```scss
:host {
  background: var(--color-primary);
}
```

```typescript
this.renderer.setStyle(document.documentElement, '--color-primary', '#4caf50');
```

## 💻 詳細実装例（学習用）
```typescript
// theme.service.ts
import { Injectable, Renderer2, RendererFactory2 } from '@angular/core';

@Injectable({ providedIn: 'root' })
export class ThemeService {
  private renderer: Renderer2;

  constructor(rendererFactory: RendererFactory2) {
    this.renderer = rendererFactory.createRenderer(null, null);
  }

  setPrimaryColor(color: string): void {
    this.renderer.setStyle(document.documentElement, '--color-primary', color);
  }
}
```

```scss
/* styles.scss */
:root {
  --color-primary: #1976d2;
  --color-surface: #ffffff;
}
```

```scss
/* button.component.scss */
:host {
  background: var(--color-primary);
  color: var(--color-surface);
}
```

## ベストプラクティス
- 共通トークンは`:root`に定義し、コンポーネントでは必要な変数だけ上書きする
- テーマ切り替えではbodyや:rootにテーマクラスを付与し、その中で変数を再定義する
- SCSS変数と併用する場合は、ビルド時定数（SCSS）とランタイム変更（CSS変数）を使い分ける

## 注意点
- 古いブラウザ（IE11など）ではCSS変数がサポートされないためポリフィルが必要
- `var()`のフォールバック値を指定して、未定義時の挙動を制御する
- 変数の命名規則を決めておかないと用途がわかりにくくなる

## 関連技術
- ダークモード/テーマ切り替え
- SCSS `@use` とCSS変数併用パターン
- Renderer2・Angular CDK Overlayでのテーマ適用
