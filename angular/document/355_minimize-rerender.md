# #355 「再描画の最小化」

## 概要
`*ngFor`を使用するリストは不変データとtrackBy、OnPush戦略を組み合わせることで再描画を最小化できる。

## 学習目標
- 再描画が発生するメカニズムを理解する
- インメモリの配列更新戦略を学ぶ
- trackByとChangeDetectionの連携を把握する

## 技術ポイント
- 不変更新で配列差分を検知しやすくする
- trackByでDOM再利用＆OnPushでChange Detection境界を設定
- Signalsを使うと局所的な再レンダリングに留められる

## 📺 画面表示用コード（動画用）
```html
<item-card *ngFor="let card of cards(); trackBy: trackById"
           [card]="card"></item-card>
```

## 💻 詳細実装例（学習用）
```typescript
interface Card {
  id: number;
  title: string;
}

@Component({
  selector: 'app-minimize-rerender-demo',
  standalone: true,
  changeDetection: ChangeDetectionStrategy.OnPush,
  imports: [CommonModule],
  template: `
    <button (click)="shuffle()">シャッフル</button>
    <ul>
      <li *ngFor="let card of cards(); trackBy: trackById">{{ card.title }}</li>
    </ul>
  `
})
export class MinimizeRerenderDemoComponent {
  private readonly cardsSignal = signal<Card[]>([
    { id: 1, title: 'Directive' },
    { id: 2, title: 'Component' },
    { id: 3, title: 'Service' }
  ]);
  protected cards = this.cardsSignal.asReadonly();

  protected shuffle(): void {
    this.cardsSignal.update(list => [...list].reverse());
  }

  protected trackById(_: number, card: Card): number {
    return card.id;
  }
}
```

## ベストプラクティス
- 不変更新とtrackByをセットで導入し、再描画を可視化して確認する
- OnPushコンポーネントでは外部入力が変わったときだけ描画されるので、データフローを明確に保つ
- Signalsを使うと更新対象の部分だけ再描画できる

## 注意点
- ミュータブルな更新を行うとOnPushで描画されないケースがある
- trackBy関数が新しい参照を返すと逆効果なので注意
- ブラウザ開発ツールでパフォーマンスを計測し、最適化の効果を検証する

## 関連技術
- ChangeDetectionStrategy.OnPush
- Angular Signals
- Performance Profiling
