# #047 「(mouseenter) マウスイベント」

## 概要
マウスが要素に乗ったタイミングを検出する(mouseenter)イベントを活用し、ホバー演出やツールチップ表示を制御する方法を学びます。

## 学習目標
- (mouseenter) と(mouseleave)の役割と違いを理解する
- ホバー状態に応じたUI更新の基本パターンを実装する
- ポインタ操作とアクセシビリティの両立方法を考える

## 技術ポイント
- **mouseenterイベント**: バブルしないホバー開始イベントで、子要素への移動では再発火しない
- **mouseleave組み合わせ**: ホバー終了を補足して状態を戻す
- **ARIAサポート**: キーボード利用者へも同様の体験を提供する必要がある

## 📺 画面表示用コード（動画用）
**表示ルール**: 最大3個、各10行以内、動画で見せる部分のみ

```html
<div (mouseenter)="showTip()" (mouseleave)="hideTip()">ℹ️</div>
```

```html
<li (mouseenter)="focusItem(item)" (mouseleave)="focusItem(null)">
  {{ item.name }}
</li>
```

```html
<img (mouseenter)="highlight = true" (mouseleave)="highlight = false" />
```

## 💻 詳細実装例（学習用）
```typescript
import { Component, signal } from '@angular/core';

type Feature = { id: number; name: string; description: string };

@Component({
  selector: 'app-mouseenter-demo',
  standalone: true,
  templateUrl: './mouseenter-demo.component.html',
})
export class MouseenterDemoComponent {
  features = signal<Feature[]>([
    { id: 1, name: 'Signal', description: 'リアクティブで軽量な状態管理' },
    { id: 2, name: 'Control Flow', description: '@if / @for の新構文' },
    { id: 3, name: 'Standalone', description: 'Moduleレスのコンポーネント設計' },
  ]);
  hoveredId = signal<number | null>(null);
  tipVisible = signal(false);

  focusItem(item: Feature | null): void {
    this.hoveredId.set(item?.id ?? null);
  }

  toggleTip(state: boolean): void {
    this.tipVisible.set(state);
  }
}
```

```html
<section class="tooltip-area">
  <span
    tabindex="0"
    (mouseenter)="toggleTip(true)"
    (mouseleave)="toggleTip(false)"
    (focus)="toggleTip(true)"
    (blur)="toggleTip(false)"
  >
    ℹ️
  </span>
  <aside *ngIf="tipVisible()">Signalsはリアクティブな状態APIです</aside>
</section>

<ul>
  <li
    @for (feature of features(); track feature.id)
    (mouseenter)="focusItem(feature)"
    (mouseleave)="focusItem(null)"
    [class.active]="hoveredId() === feature.id"
  >
    {{ feature.name }}
  </li>
</ul>
<p>
  詳細:
  {{
    features().find((f) => f.id === hoveredId())?.description ??
      '項目にホバーしてください'
  }}
</p>
```

## ベストプラクティス
- マウス専用の演出はフォーカスイベントでも同等の情報を提供する
- 状態をSignalなどで管理し、描画ロジックをテンプレートへ委譲する
- ホバーとクリックが同時に存在する場合は操作優先度を明確にする

## 注意点
- タッチデバイスではmouseenterが発火しないため代替操作を準備する
- 子要素にマウスが移動してもmouseenterは再発火しない点を理解する
- 複数のHover状態を同時に扱う場合は識別子を用意して競合を避ける

## 関連技術
- :hover CSS擬似クラスとAngularの組み合わせ
- フォーカス管理とアクセシビリティ
- Pointer Events API
