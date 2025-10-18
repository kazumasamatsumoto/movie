# #172 「CSS カスタムプロパティ」

## 概要
CSSカスタムプロパティ（CSS変数）を活用し、スタイル値を柔軟に再利用・上書きする方法を整理します。Angularコンポーネント内でも通常のCSSと同様に利用できます。

## 学習目標
- CSSカスタムプロパティの定義・参照・フォールバック方法を理解する
- コンポーネント単位で上書きしたり、テーマを切り替える手順を習得する
- TypeScriptからCSS変数を更新する実装パターンを把握する

## 技術ポイント
- **定義**: `--color-primary: #1976d2;`
- **参照**: `color: var(--color-primary, #2196f3);`
- **スコープ**: `:root`や`:host`などスコープごとに再定義可能

```scss
:root {
  --color-primary: #1976d2;
}
```

```scss
:host {
  color: var(--color-primary, #2196f3);
}
```

```typescript
this.renderer.setStyle(document.body, '--color-primary', '#ef5350');
```

## 💻 詳細実装例（学習用）
```scss
/* styles.scss */
:root {
  --color-primary: #1976d2;
  --spacing-md: 16px;
}
```

```scss
/* card.component.scss */
:host {
  display: block;
  padding: var(--spacing-md);
  border: 1px solid var(--color-primary);
}
```

```typescript
// theme.service.ts
import { Injectable, Renderer2, RendererFactory2 } from '@angular/core';

@Injectable({ providedIn: 'root' })
export class ThemeService {
  private renderer: Renderer2;

  constructor(rendererFactory: RendererFactory2) {
    this.renderer = rendererFactory.createRenderer(null, null);
  }

  setPrimary(color: string): void {
    this.renderer.setStyle(document.documentElement, '--color-primary', color);
  }
}
```

## ベストプラクティス
- デザインシステムのトークン（色、間隔、フォント）をCSS変数で定義し、SCSSとの併用で柔軟性を確保する
- コンポーネントごとに必要な変数だけ上書きし、下位コンポーネントへ継承させる
- CSS変数はRuntimeに変更できるので、テーマ切替やアクセシビリティ対応に有効

## 注意点
- CSS変数はIE11など古いブラウザではサポートされないためポリフィルが必要
- フォールバック値を指定しない場合、未定義でレイアウト崩れを起こす可能性がある
- 名前が衝突すると意図せず上書きされるので名前空間を意識する

## 関連技術
- `var()`関数とフォールバック値
- ダークモード/テーマ切り替え
- SCSS `@use` + CSS変数併用パターン
