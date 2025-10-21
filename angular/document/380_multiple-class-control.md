# #380 「複数クラスの動的制御」

## 概要
複数クラスを同時に制御する場合は、配列やオブジェクト形式を組み合わせたり、コンポーネントでクラスセットを生成して渡すことで管理しやすくなる。

## 学習目標
- 複数クラスをまとめて制御する設計方法を理解する
- コンポーネントでクラスリストを生成しテンプレートをシンプルに保つ
- Tailwindなどユーティリティクラス使用時の注意点を把握する

## 技術ポイント
- オブジェクトと配列のハイブリッドを使って可読性を維持
- `computed`でクラスセットを返し再描画を最小化
- クラス競合を避けるため命名規則と優先順位を明確化

## 📺 画面表示用コード（動画用）
```html
<div [ngClass]="[baseClass, { 'is-loading': loading, 'is-error': error }]">カード</div>
```

## 💻 詳細実装例（学習用）
```typescript
@Component({
  selector: 'app-multi-class-control-demo',
  standalone: true,
  imports: [CommonModule],
  template: `
    <article [ngClass]="cardClasses()">
      <h3>{{ title }}</h3>
      <p>{{ description }}</p>
    </article>
  `
})
export class MultiClassControlDemoComponent {
  protected title = 'ユーザーカード';
  protected description = '状態によってスタイルを切り替えます。';
  private readonly status = signal<'idle' | 'loading' | 'error'>('idle');

  protected readonly cardClasses = computed(() => [
    'card',
    {
      'card--loading': this.status() === 'loading',
      'card--error': this.status() === 'error'
    }
  ]);
}
```

## ベストプラクティス
- 定数化したベースクラスと状態に応じたクラスを分離して管理
- computedを利用し、ステート更新時のみ差分を反映
- Tailwindなど利用時はクラスの重複や優先順位に注意し、必要なら`ngClass`より`class`リテラルを優先

## 注意点
- オブジェクトと配列を混在させると読みづらくなるため、チームでルールを決める
- 状態の組み合わせが増えすぎるとクラス管理が破綻するため、可能なら分解する
- クラスだけでなく`aria-*`や`data-*`属性も同時に更新して一貫した挙動を提供する

## 関連技術
- Angular Signals / computed
- Tailwind CSS
- 状態マシン設計
