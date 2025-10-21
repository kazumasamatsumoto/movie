# #298 「Badge Component - バッジ」

## 概要
Badge Componentは通知数や状態を示す小さなラベルで、variantによる色分けや最大値の丸めを統一したUIとして提供する。

## 学習目標
- バッジのvariantとサイズをInputで制御する
- 数値バッジの最大値丸めを実装する
- アイコン併用時のpositioningを整える

## 技術ポイント
- max表示(99+など)
- CSS position
- aria-label

## 📺 画面表示用コード（動画用）
```typescript
@Component({ selector: 'app-badge', standalone: true, template: `<span class="badge" [class.badge--success]="variant==='success'" [class.badge--danger]="variant==='danger'" [attr.aria-label]="ariaLabel">{{ display }}</span>`, changeDetection: ChangeDetectionStrategy.OnPush })
export class BadgeComponent {
  @Input() value: number | string = '';
  @Input() variant: 'neutral' | 'success' | 'danger' = 'neutral';
  @Input() max = 99;
  get display(): string { return typeof this.value === 'number' && this.value > this.max ? `${this.max}+` : String(this.value); }
  get ariaLabel(): string | null { return typeof this.value === 'number' ? `通知 ${this.display}` : null; }
}
```

```css
.badge { display: inline-flex; align-items: center; justify-content: center; min-width: 20px; padding: 0 6px; border-radius: 999px; font-size: 12px; background: #64748b; color: white; }
.badge--success { background: #22c55e; }
.badge--danger { background: #ef4444; }
```

```html
<button type="button" class="icon-button">
  <span class="material-symbols-outlined">mail</span>
  <app-badge [value]="120" variant="danger"></app-badge>
</button>
```

## 💻 詳細実装例（学習用）
```typescript
@Component({
  selector: 'app-badge-demo',
  standalone: true,
  imports: [BadgeComponent],
  template: `
    <app-badge [value]="12"></app-badge>
    <app-badge [value]="0" variant="success"></app-badge>
    <div class="icon-wrapper">
      <span class="material-symbols-outlined">notifications</span>
      <app-badge [value]="156" variant="danger"></app-badge>
    </div>
  `,
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class BadgeDemoComponent {}
```

## ベストプラクティス
- 数値バッジはmaxを設け視覚的なノイズを抑える
- ボタンやアイコンとの組み合わせはposition:relativeで配置する
- テキストバッジはvariantで意味を明確にする

## 注意点
- 装飾用途のバッジはaria-hiddenをtrueにする
- 長いテキストを表示する場合は余白と折返しを調整する
- 多数表示時は色の選択によりコントラストを確保する

## 関連技術
- Design Tokens
- CSS Positioning
- Accessibility
