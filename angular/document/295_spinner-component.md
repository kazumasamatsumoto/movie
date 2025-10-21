# #295 「Spinner Component - スピナー」

## 概要
Spinner Componentは処理中を示すアニメーションを提供し、サイズ・色・スピードをInputで調整できる軽量なUI部品である。

## 学習目標
- SVGとCSSアニメーションでスピナーを実装する
- サイズと色をInputで切り替える
- prefers-reduced-motionに対応したフォールバックを用意する

## 技術ポイント
- SVG circleアニメーション
- CSS animation
- Media query `prefers-reduced-motion`

## 📺 画面表示用コード（動画用）
```typescript
@Component({ selector: 'app-spinner', standalone: true, template: `<svg class="spinner" [style.width.px]="size" [style.height.px]="size" viewBox="0 0 50 50" role="img" aria-label="処理中"><circle class="path" cx="25" cy="25" r="20" fill="none" [attr.stroke-width]="stroke" [attr.stroke]="color"></circle></svg>`, changeDetection: ChangeDetectionStrategy.OnPush })
export class SpinnerComponent {
  @Input() size = 32;
  @Input() stroke = 4;
  @Input() color = '#0d6efd';
}
```

```css
.spinner { animation: spin 1s linear infinite; }
.path { stroke-linecap: round; }
@keyframes spin { 0% { transform: rotate(0); } 100% { transform: rotate(360deg); } }
@media (prefers-reduced-motion: reduce) { .spinner { animation: none; } }
```

```html
<app-spinner [size]="48" [color]="'#38bdf8'"></app-spinner>
```

## 💻 詳細実装例（学習用）
```typescript
@Component({
  selector: 'app-spinner-demo',
  standalone: true,
  imports: [SpinnerComponent],
  template: `
    <div class="demo">
      <app-spinner [size]="24"></app-spinner>
      <app-spinner [size]="40" [color]="'#22c55e'"></app-spinner>
      <app-spinner [size]="56" [stroke]="6" [color]="'#f97316'"></app-spinner>
    </div>
  `,
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class SpinnerDemoComponent {}
```

## ベストプラクティス
- サイズとカラーをInputで提供し、デザインシステムと同期する
- aria-labelで意味を伝え、テキストフォールバックも検討する
- アニメーションスピードは0.8〜1.2秒程度で統一する

## 注意点
- prefers-reduced-motionでアニメーションを停止する
- SVGのstroke幅が小さいと視認性が下がるためバランスを取る
- 複数設置時には回転の同期が不要か検討する

## 関連技術
- SVG
- CSS Animation
- Accessibility
