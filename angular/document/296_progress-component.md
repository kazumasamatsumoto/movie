# #296 「Progress Component - プログレスバー」

## 概要
Progress Componentは処理の進捗率を視覚的に示すUIで、確定値と不定値の両方に対応しアクセシビリティ属性を備えたコンポーネントである。

## 学習目標
- 進捗率をInputで受け取り視覚とARIAを同期させる
- indeterminateモードのアニメーションを実装する
- テーマ変数で色と高さを調整する

## 技術ポイント
- aria-valuenow/aria-valuemin/aria-valuemax
- CSS幅計算
- indeterminateアニメーション

## 📺 画面表示用コード（動画用）
```typescript
@Component({ selector: 'app-progress', standalone: true, template: `<div class="progress" role="progressbar" [attr.aria-valuenow]="indeterminate ? undefined : value" aria-valuemin="0" aria-valuemax="100"><div class="progress__bar" [class.progress__bar--indeterminate]="indeterminate" [style.width.%]="indeterminate ? 100 : value"></div><span class="progress__label">{{ indeterminate ? '処理中' : value + '%' }}</span></div>`, changeDetection: ChangeDetectionStrategy.OnPush })
export class ProgressComponent {
  @Input() value = 0;
  @Input() indeterminate = false;
}
```

```css
.progress { position: relative; background: rgba(148,163,184,.2); border-radius: 999px; height: 8px; overflow: hidden; }
.progress__bar { height: 100%; background: linear-gradient(90deg,#38bdf8,#0ea5e9); transition: width .3s ease; }
.progress__bar--indeterminate { animation: progress-indeterminate 1.2s infinite; }
.progress__label { display: block; margin-top: 8px; font-size: 12px; color: #475569; }
@keyframes progress-indeterminate { 0% { transform: translateX(-100%); } 50% { transform: translateX(0); } 100% { transform: translateX(100%); } }
```

```html
<app-progress [value]="72"></app-progress>
```

## 💻 詳細実装例（学習用）
```typescript
@Component({
  selector: 'app-progress-demo',
  standalone: true,
  imports: [ProgressComponent],
  template: `
    <app-progress [value]="completed"></app-progress>
    <button type="button" (click)="advance(10)">+10%</button>
    <app-progress [indeterminate]="true"></app-progress>
  `,
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class ProgressDemoComponent {
  completed = 30;
  advance(step: number): void {
    this.completed = Math.min(100, this.completed + step);
  }
}
```

## ベストプラクティス
- valueは0〜100の範囲に正規化し、ARIA属性と同期させる
- indeterminateモードではテキストで状態を補足する
- テーマ変数を使って色と高さを一括変更できるようにする

## 注意点
- 進捗が停滞する場合は残り時間など追加情報を検討する
- アニメーションのコントラストを確保し視認性を高める
- スクリーンリーダーでは頻繁な更新を避けるためスロットリングする

## 関連技術
- Accessibility
- CSS Animation
- Design Tokens
