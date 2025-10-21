# #288 「Card Component - カードUI」

## 概要
Card Componentは情報をまとまりとして表示するUIパターンで、ヘッダー/本文/アクションをSlotで受け取りスタイルとスペーシングを統一する。

## 学習目標
- 複数Slotを持つカードコンポーネントを実装する
- CSS変数で影や余白を制御する
- レスポンシブグリッドとの連携方法を理解する

## 技術ポイント
- ng-content複数スロット
- CSS custom properties
- Standalone Component

## 📺 画面表示用コード（動画用）
```typescript
@Component({ selector: 'app-card', standalone: true, template: `<article class="card"><header class="card__header"><ng-content select="[slot=header]"></ng-content></header><section class="card__body"><ng-content></ng-content></section><footer class="card__footer"><ng-content select="[slot=footer]"></ng-content></footer></article>`, changeDetection: ChangeDetectionStrategy.OnPush })
export class CardComponent {
  @Input() elevation: 'sm' | 'md' | 'lg' = 'md';
}
```

```css
.card { --card-padding: 16px; --card-shadow: 0 2px 6px rgba(15,23,42,.12); padding: var(--card-padding); border-radius: 16px; box-shadow: var(--card-shadow); background: #fff; display: flex; flex-direction: column; gap: 12px; }
.card__footer { display: flex; gap: 8px; justify-content: flex-end; }
```

```html
<app-card>
  <h3 slot="header">プランA</h3>
  <p>月額2,000円で利用できます。</p>
  <div slot="footer"><button>申し込む</button></div>
</app-card>
```

## 💻 詳細実装例（学習用）
```typescript
@Component({
  selector: 'app-card-grid',
  standalone: true,
  imports: [CardComponent],
  template: `
    <section class="grid">
      <app-card *ngFor="let item of cards" [attr.data-elevation]="item.elevation">
        <h3 slot="header">{{ item.title }}</h3>
        <p>{{ item.description }}</p>
        <div slot="footer"><button type="button">詳細</button></div>
      </app-card>
    </section>
  `,
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class CardGridComponent {
  readonly cards = [
    { title: 'スタンダード', description: '基本機能を提供します。', elevation: 'md' },
    { title: 'プロ', description: '高度な分析機能付き。', elevation: 'lg' }
  ];
}
```

## ベストプラクティス
- Slot名を固定化し、ヘッダーやアクションの位置を一貫させる
- CSS変数で影・余白・角丸を外部から調整可能にする
- レスポンシブは親コンテナのGridと連携し列幅を制御する

## 注意点
- Slotが空の場合は余白を調整し不要な領域を表示しない
- コンテンツ投影の中でフォーム要素を使う際はラベル関連を保持する
- カード背景色のコントラストを確保する

## 関連技術
- Content Projection
- CSS Grid
- Design Tokens
