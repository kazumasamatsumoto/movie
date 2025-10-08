# #183 「CSS Modules の活用」

## 概要
Angular標準のスタイルカプセル化（ViewEncapsulation）とは別に、CSS Modulesを導入する際の考え方と実現方法を整理します。CLI標準ではサポートされないため、カスタマイズ時の注意点を確認します。

## 学習目標
- CSS Modulesの概要とAngularで採用するメリット・デメリットを理解する
- Webpack設定をカスタマイズしてCSS Modulesを導入する手順を把握する
- Angular標準機能との比較から採用可否を判断できるようになる

## 技術ポイント
- **CSS Modules**: クラス名をコンパイル時にユニーク化する仕組み
- **Angular CLI制限**: デフォルト設定ではCSS Modules非対応
- **代替手段**: ViewEncapsulation.EmulatedやTailwind/SCSS、Scoped CSSを活用

## 📺 画面表示用コード（動画用）

```scss
.button {
  composes: base from './base.module.scss';
  color: #fff;
}
```

```typescript
import styles from './button.module.scss';
```

```html
<button [class]="styles.button">Button</button>
```

## 💻 詳細実装例（学習用）
```typescript
// button.component.ts (常用には非推奨: 自前Webpack前提)
import { Component } from '@angular/core';
import styles from './button.module.scss';

@Component({
  selector: 'app-button',
  standalone: true,
  template: `<button [class]="styles.button"><ng-content></ng-content></button>`,
  // CSS Modulesを使う場合はstyleUrlsではなくimportする
  styles: [],
})
export class ButtonComponent {
  readonly styles = styles;
}
```

```scss
/* button.module.scss */
.button {
  padding: 8px 16px;
  border-radius: 999px;
  background: #1976d2;
  color: #fff;
}
```

## ベストプラクティス
- ViewEncapsulation.Emulatedで十分な場合はCSS Modulesを導入しない（メンテナンスが複雑化するため）
- 既存のReactベースCSS Modules資産を流用するなど明確な理由がある場合のみ検討する
- カスタムWebpack構成を採用する際は、Angular CLI更新による互換性問題を想定する

## 注意点
- Standalone Componentsでも`styleUrls`と併用できず、importとバインディングで対応する必要がある
- CLIの`ng build`/`ng test`が標準設定では動作しないため、Builderを差し替える必要がある
- チームメンバー全員がCSS Modules構文やツールチェーンを理解しているか確認する

## 関連技術
- ViewEncapsulation
- Angular CLI Builders / カスタムWebpack
- Tailwind CSSやSCSSといった代替スタイル戦略
