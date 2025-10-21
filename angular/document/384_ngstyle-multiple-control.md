# #384 「複数スタイルの動的制御」

## 概要
複数スタイルを動的に制御する場合、コンポーネントでスタイルオブジェクトをまとめて生成し、状態に応じてまとめて反映することで管理しやすくなる。

## 学習目標
- 動的スタイル制御の設計パターンを理解する
- computedでスタイルを構築し再描画を最小化する方法を学ぶ
- CSSクラスとngStyleの使い分けを把握する

## 技術ポイント
- 状態ごとにスタイルセットを定義し、必要に応じてスプレッド
- 数値プロパティはテンプレートリテラルで単位付与
- ヘビーな計算はコンポーネントで行い、テンプレートは参照のみ

## 📺 画面表示用コード（動画用）
```html
<div [ngStyle]="boxStyles()">複数制御</div>
```

## 💻 詳細実装例（学習用）
```typescript
@Component({
  selector: 'app-multi-style-demo',
  standalone: true,
  imports: [CommonModule],
  template: `
    <div [ngStyle]="boxStyles()">ステータス: {{ status() }}</div>
    <button type="button" (click)="cycle()">切り替え</button>
  `
})
export class MultiStyleDemoComponent {
  private readonly statuses = ['info', 'warn', 'error'] as const;
  private index = 0;
  private readonly statusSignal = signal<typeof this.statuses[number]>('info');
  protected status = this.statusSignal.asReadonly();

  protected boxStyles(): Record<string, string> {
    switch (this.status()) {
      case 'warn':
        return { background: '#f97316', color: '#fff', padding: '1rem', borderRadius: '0.75rem' };
      case 'error':
        return { background: '#b91c1c', color: '#fff', padding: '1rem', borderRadius: '0.75rem' };
      default:
        return { background: '#0ea5e9', color: '#fff', padding: '1rem', borderRadius: '0.75rem' };
    }
  }

  protected cycle(): void {
    this.index = (this.index + 1) % this.statuses.length;
    this.statusSignal.set(this.statuses[this.index]);
  }
}
```

## ベストプラクティス
- スタイルセットを`Record<string, string>`で型付けし、記述漏れを防ぐ
- 同じスタイル値が繰り返される場合は共通基底オブジェクトをスプレッドする
- computedでスタイルを返す場合は副作用を避け、純粋関数にする

## 注意点
- 大量のスタイルをインラインで指定するとCSS設計が崩れるのでケースを限定
- 変更検知で毎回新しいオブジェクトが生成され性能に影響する場合はmemo化
- CSSアニメーションなどはクラスで管理した方がコントロールしやすい

## 関連技術
- Angular Signals
- CSSクラス設計
- Renderer2
