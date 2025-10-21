# #381 「ngStyle - スタイル制御」

## 概要
`ngStyle`はインラインスタイルをオブジェクトで制御できるディレクティブで、複数のスタイルプロパティを状態に合わせてまとめて変更できる。

## 学習目標
- ngStyleの役割と基本的な使い方を理解する
- Renderer2を使用せずにスタイルを安全に変更する方法を学ぶ
- 条件に応じたスタイルの切り替えパターンを把握する

## 技術ポイント
- `[ngStyle]="{ property: value }"`でプロパティを指定
- 値は文字列・数値・式結果を使用可能
- Falsy値を渡すとそのプロパティは削除される

## 📺 画面表示用コード（動画用）
```html
<div [ngStyle]="{ color: themeColor, fontSize: fontSize + 'px' }">スタイル制御</div>
```

## 💻 詳細実装例（学習用）
```typescript
@Component({
  selector: 'app-ngstyle-demo',
  standalone: true,
  imports: [CommonModule],
  template: `
    <section [ngStyle]="styleMap()">
      <h3>デザインプレビュー</h3>
      <p>インラインスタイルを状態で切り替えています。</p>
    </section>
    <button type="button" (click)="toggle()">テーマ切替</button>
  `
})
export class NgStyleDemoComponent {
  private dark = false;

  protected styleMap(): Record<string, string> {
    return {
      background: this.dark ? '#0f172a' : '#f1f5f9',
      color: this.dark ? '#e2e8f0' : '#0f172a',
      padding: '1.5rem',
      borderRadius: '1rem'
    };
  }

  protected toggle(): void {
    this.dark = !this.dark;
  }
}
```

## ベストプラクティス
- 複数スタイルを切り替える場合はコンポーネントでオブジェクトを生成し、テンプレートを簡潔に保つ
- 数値値には単位を付けるなどフォーマットを統一
- 長期的に使うスタイルはCSSクラス化を検討し、ngStyleは例外時に利用する

## 注意点
- インラインスタイルは優先度が高く難読になりがちなので必要最小限に
- TransitionなどはCSSクラスに任せた方が管理しやすい
- パフォーマンス観点から、毎回新しいオブジェクトを生成する場合は`computed`やメモ化を検討

## 関連技術
- Renderer2.setStyle
- CSSクラス設計
- Angular Signals
