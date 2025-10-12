# #192 「ng-content の仕組み」

## 概要
Angularにおけるコンテンツ投影の内部仕組みを理解し、親コンポーネントのコンテンツが子コンポーネント内の`ng-content`へどのように挿入されるのかを学びます。

## 学習目標
- コンテンツ投影のレンダリングフローを説明できる
- 複数の`ng-content`がある場合の選択順序を理解する
- 投影されないコンテンツ（フォールバック）の挙動を把握する

## 技術ポイント
- **収集と挿入**: 親コンポーネントの子要素がコンパイル時に収集され、`ng-content`の位置へ差し込まれる
- **セレクタ評価**: `select`属性がある場合、CSSセレクタにマッチした順に挿入される。マッチしないコンテンツは最後のデフォルトスロットへ
- **再描画**: 投影コンテンツは親の変更検知サイクルで再評価される

## 📺 画面表示用コード（動画用）

```html
<!-- parent -->
<app-panel>
  <h3 card-title>タイトル</h3>
  <p>本文</p>
</app-panel>
```

```html
<!-- child -->
<ng-content select="[card-title]"></ng-content>
<ng-content></ng-content>
```

```html
<!-- 結果 -->
<app-panel>
  <h3 card-title>タイトル</h3>
  <p>本文</p>
</app-panel>
```

## 💻 詳細実装例（学習用）
```typescript
// panel.component.ts
import { Component } from '@angular/core';

@Component({
  selector: 'app-panel',
  standalone: true,
  templateUrl: './panel.component.html',
  styleUrls: ['./panel.component.scss'],
})
export class PanelComponent {}
```

```html
<!-- panel.component.html -->
<article class="panel">
  <header class="panel__header">
    <ng-content select="[panel-title]"></ng-content>
  </header>
  <section class="panel__body">
    <ng-content></ng-content>
  </section>
</article>
```

```html
<!-- parent.component.html -->
<app-panel>
  <h2 panel-title>仕組み解説</h2>
  <p>セレクタに一致するコンテンツが順番に差し込まれます。</p>
  <p>一致しないコンテンツはデフォルトスロットへ回ります。</p>
</app-panel>
```

## ベストプラクティス
- スロットの順序は`ng-content`の宣言順に評価されるため、優先度の高いスロットを先に記述する
- セレクタの設計はシンプルに保ち、どの要素がどこに入るかをドキュメント化する
- 投影が存在しない場合を想定し、デフォルトコンテンツまたは警告メッセージを用意する

## 注意点
- 投影コンテンツは親コンポーネントのテンプレートに属するため、子から直接データバインディングはできない
- 動的に投影を切り替える場合は`ng-template`や`ContentChild`を用いてレンダリングを制御する
- 複雑な投影ロジックを持たせすぎると保守が難しくなるため、責務を分割する

## 関連技術
- Multi Slot Projection（#194）
- `ContentChild` / `ContentChildren`で投影コンテンツへのアクセス
- `ngTemplateOutlet`による動的レンダリング


