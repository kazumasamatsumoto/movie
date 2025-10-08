# #174 「ダークモード対応」

## 概要
ユーザーやOS設定に応じてライト/ダークテーマを切り替える実装方法を整理し、CSS変数とAngularの状態管理を活用したダークモード対応を学びます。

## 学習目標
- OSの`prefers-color-scheme`メディアクエリを検出する手順を理解する
- Angularでテーマクラスを切り替えるロジックを実装する
- CSS変数を使ってダークモード用のスタイルを管理する

## 技術ポイント
- **初期判定**: `window.matchMedia('(prefers-color-scheme: dark)')`
- **CSS変数**: `.dark-theme { --color-muted: #cfd8dc; }`
- **状態保持**: `localStorage`やSignalsでテーマ選択を記録

## 📺 画面表示用コード（動画用）

```typescript
const prefersDark = matchMedia('(prefers-color-scheme: dark)').matches;
```

```typescript
renderer.addClass(document.body, 'dark-theme');
```

```scss
.dark-theme {
  --color-background: #121212;
}
```

## 💻 詳細実装例（学習用）
```typescript
// dark-mode.service.ts
import { Injectable, Renderer2, RendererFactory2, effect, signal } from '@angular/core';

@Injectable({ providedIn: 'root' })
export class DarkModeService {
  private renderer: Renderer2;
  readonly isDark = signal(this.detectPrefersDark());

  constructor(rendererFactory: RendererFactory2) {
    this.renderer = rendererFactory.createRenderer(null, null);
    effect(() => this.applyTheme(this.isDark()));
  }

  toggle(): void {
    this.isDark.update((value) => !value);
    localStorage.setItem('prefers-dark', String(this.isDark()));
  }

  private applyTheme(dark: boolean): void {
    const body = document.body;
    if (dark) {
      this.renderer.addClass(body, 'dark-theme');
    } else {
      this.renderer.removeClass(body, 'dark-theme');
    }
  }

  private detectPrefersDark(): boolean {
    const stored = localStorage.getItem('prefers-dark');
    if (stored !== null) {
      return stored === 'true';
    }
    return matchMedia('(prefers-color-scheme: dark)').matches;
  }
}
```

```scss
/* styles.scss */
:root {
  --surface: #ffffff;
  --text-primary: #263238;
}

.dark-theme {
  --surface: #121212;
  --text-primary: #eceff1;
}
```

```scss
/* component.scss */
:host {
  display: block;
  background: var(--surface);
  color: var(--text-primary);
}
```

## ベストプラクティス
- OS設定を初期状態として採用し、ユーザーが切り替えられるUIを提供する
- テーマ情報を`localStorage`などへ保存し、次回起動時に復元
- CSS変数を利用してコンポーネント全体で共通スタイルを切り替える

## 注意点
- `matchMedia`はブラウザAPIのためSSR環境では使用時期に注意する
- 外部ライブラリのスタイル（例: Angular Material）もダークテーマに対応させる必要がある
- 画像・アイコンがライト用の場合は、ダークテーマ用のアセットを用意する

## 関連技術
- CSS `prefers-color-scheme`メディアクエリ
- CSSカスタムプロパティ
- Angular Signalsによるテーマ状態管理
