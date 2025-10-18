# #173 「テーマの実装方法」

## 概要
Angularアプリでテーマ（ライト/ダークやブランドカラー）を切り替える設計をまとめ、CSS変数やSCSS、Material Themeなど複数アプローチを比較します。

## 学習目標
- テーマ切り替えの基本パターンを理解する
- CSS変数とSCSSテーマ、Angular Materialのテーマ機能の選択基準を学ぶ
- テーマ状態をアプリケーションで管理し、再描画へ反映させる流れを習得する

## 技術ポイント
- **CSS変数利用**: `:root`と`.dark-theme`で変数を再定義
- **SCSSテーマ**: `@use`と`@include`を使い、テーマ別のスタイルセットを生成
- **状態管理**: `ThemeService`やSignalsでテーマフラグを保持し、bodyクラスを切り替える

```scss
:root {
  --color-surface: #ffffff;
}
.dark-theme {
  --color-surface: #263238;
}
```

```typescript
renderer.addClass(document.body, 'dark-theme');
```

```scss
@include theme.light-theme;
@include theme.dark-theme;
```

## 💻 詳細実装例（学習用）
```typescript
// theme.service.ts
import { Injectable, Renderer2, RendererFactory2 } from '@angular/core';

@Injectable({ providedIn: 'root' })
export class ThemeService {
  private renderer: Renderer2;
  private isDark = false;

  constructor(rendererFactory: RendererFactory2) {
    this.renderer = rendererFactory.createRenderer(null, null);
  }

  toggle(): void {
    this.isDark = !this.isDark;
    const body = document.body;
    if (this.isDark) {
      this.renderer.addClass(body, 'dark-theme');
    } else {
      this.renderer.removeClass(body, 'dark-theme');
    }
  }
}
```

```scss
/* styles/themes.scss */
:root {
  --color-background: #f5f5f5;
  --color-text: #263238;
}

.dark-theme {
  --color-background: #121212;
  --color-text: #eceff1;
}
```

```scss
/* component.scss */
:host {
  background: var(--color-background);
  color: var(--color-text);
}
```

## ベストプラクティス
- テーマトークンをCSS変数にまとめ、SCSSからインポートする構成にすると切り替えが容易
- Angular Materialを利用する場合は`mat-light-theme` / `mat-dark-theme`構文を活用
- ユーザー設定を`localStorage`に保存し、初期起動時にテーマを復元する

## 注意点
- Shadow DOMを使うコンポーネントは外部テーマが届かないため、CSS変数で値を渡す必要がある
- 多数のテーマがある場合、CSS生成量やパフォーマンスに注意する
- テーマ切り替え時に画像やアイコンも合わせて変更する場合はアセットの切り替え戦略を決める

## 関連技術
- CSSカスタムプロパティ
- Angular MaterialテーマAPI
- Signals/State管理でのテーマフラグ制御
