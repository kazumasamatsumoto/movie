# #378 「オブジェクトでのクラス指定」

## 概要
`[ngClass]`にオブジェクトを渡すと、キーをクラス名、値を真偽値として解釈し、trueになったクラスだけが適用される。条件付きクラス管理に最も柔軟な形式。

## 学習目標
- オブジェクト形式でのクラス指定方法を理解する
- 状態マップを使って宣言的に管理する手法を学ぶ
- 派生状態をcomputedなどで計算するパターンを把握する

## 技術ポイント
- `Record<string, boolean>`を返す
- `computed`などでオブジェクトを生成しChange Detectionを最適化
- 同じクラス名で複数条件が競合しないよう整理

## 📺 画面表示用コード（動画用）
```html
<div [ngClass]="{ card: true, 'card--error': hasError, 'card--loading': loading }"></div>
```

## 💻 詳細実装例（学習用）
```typescript
@Component({
  selector: 'app-ngclass-object-demo',
  standalone: true,
  imports: [CommonModule],
  template: `
    <article [ngClass]="stateClasses()">
      <h3>状態: {{ state() }}</h3>
    </article>
  `,
  styles: [`
    .panel { padding: 1rem; border-radius: 0.75rem; background: #f1f5f9; }
    .panel--loading { animation: pulse 1s infinite alternate; }
    .panel--error { border: 2px solid #f97316; }
    @keyframes pulse { from { opacity: 0.6; } to { opacity: 1; } }
  `]
})
export class NgClassObjectDemoComponent {
  private readonly stateSignal = signal<'idle' | 'loading' | 'error'>('idle');
  protected state = this.stateSignal.asReadonly();

  protected readonly stateClasses = computed(() => ({
    panel: true,
    'panel--loading': this.state() === 'loading',
    'panel--error': this.state() === 'error'
  }));
}
```

## ベストプラクティス
- クラス集合をcomputedで返すと不要な再計算が抑えられる
- 状態をUnion型で管理し、クラスとの対応を明確にする
- 共有クラスは`true`固定で保持し、条件付きのものだけ動的に変える

## 注意点
- オブジェクトリテラルをテンプレート内で直接生成すると毎回新しい参照となる
- クラス名の衝突を避け、命名規約を統一
- 真偽値以外の値を渡すと想定外の挙動になるためbooleanに限定

## 関連技術
- Angular Signals / computed
- TypeScript Union型
- CSS状態クラス設計
