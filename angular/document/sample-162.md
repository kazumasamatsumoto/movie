# #162 「ViewEncapsulation - カプセル化戦略」

## 概要
Angularの`ViewEncapsulation`設定を活用し、コンポーネントスタイルのスコープ範囲を制御する方法を比較・整理します。

## 学習目標
- `ViewEncapsulation`の目的と設定方法を理解する
- `Emulated` / `None` / `ShadowDom` の違いを説明できる
- プロジェクト要件に応じた戦略の選び方を学ぶ

## 技術ポイント
- **Emulated（デフォルト）**: 擬似的に属性を付与してスタイルをコンポーネント内へ限定
- **None**: グローバルCSSとして適用、他コンポーネントへ波及
- **ShadowDom**: ブラウザのShadow DOMを利用した完全カプセル化

## 📺 画面表示用コード（動画用）

```typescript
@Component({
  selector: 'app-panel',
  standalone: true,
  templateUrl: './panel.component.html',
  styleUrls: ['./panel.component.scss'],
  encapsulation: ViewEncapsulation.Emulated,
})
```

```typescript
encapsulation: ViewEncapsulation.None
```

```typescript
encapsulation: ViewEncapsulation.ShadowDom
```

## 💻 詳細実装例（学習用）
```typescript
// panel.component.ts
import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'app-panel',
  standalone: true,
  templateUrl: './panel.component.html',
  styleUrls: ['./panel.component.scss'],
  encapsulation: ViewEncapsulation.Emulated,
})
export class PanelComponent {
  title = 'Encapsulation Demo';
}
```

```html
<!-- panel.component.html -->
<section class="panel">
  <h2>{{ title }}</h2>
  <ng-content></ng-content>
</section>
```

```scss
/* panel.component.scss */
.panel {
  border: 1px solid #e0e0e0;
  border-radius: 12px;
  padding: 16px;
}
```

```typescript
// none-panel.component.ts
@Component({
  selector: 'app-global-panel',
  standalone: true,
  templateUrl: './panel.component.html',
  styleUrls: ['./panel.component.scss'],
  encapsulation: ViewEncapsulation.None,
})
export class GlobalPanelComponent {}
```

## ベストプラクティス
- 原則として`Emulated`を使い、スタイル衝突を防ぐ
- ライブラリやテーマ用にグローバルへ広げたい場合のみ`None`を検討
- Web Components互換や完全な隔離が必要な場合に`ShadowDom`を選択

## 注意点
- `None`を多用するとスタイル衝突が起きやすくなるため命名規則を徹底する
- `ShadowDom`では外部スタイル（Normalize.cssなど）が効かないため、Shadowルート内で読み込む必要がある
- CSS変数はShadow DOM内外で共有できるが、期待どおりに動くか確認する

## 関連技術
- Angular CLIオプション `--view-encapsulation`
- Web Components / Shadow DOM API
- グローバルテーマ管理（SCSS、CSS変数）
