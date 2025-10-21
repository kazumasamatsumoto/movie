# #360 「[ngSwitch] での値指定」

## 概要
`[ngSwitch]`には任意の式を指定でき、型安全な列挙値やSignal、Observableの結果を渡すことでリッチな分岐を実現する。

## 学習目標
- `[ngSwitch]`に渡せる値の種類を理解する
- SignalやComputed値を使用した分岐を学ぶ
- テスト観点から値指定を整理する

## 技術ポイント
- 任意の式を評価しcase値と厳密比較
- Union型やenumを使うとIDE補完が効く
- Observableの場合は`AsyncPipe`で解決してから渡す

## 📺 画面表示用コード（動画用）
```html
<section [ngSwitch]="state()">
  <p *ngSwitchCase="'idle'">待機中</p>
  <p *ngSwitchCase="'running'">実行中</p>
</section>
```

## 💻 詳細実装例（学習用）
```typescript
type JobState = 'idle' | 'running' | 'failed';

@Component({
  selector: 'app-switch-value-demo',
  standalone: true,
  imports: [CommonModule],
  template: `
    <section [ngSwitch]="state()">
      <p *ngSwitchCase="'idle'">ジョブは待機しています。</p>
      <p *ngSwitchCase="'running'">ジョブを実行中です。</p>
      <p *ngSwitchCase="'failed'">ジョブが失敗しました。</p>
      <p *ngSwitchDefault>不明な状態です。</p>
    </section>
  `
})
export class SwitchValueDemoComponent {
  private readonly stateSignal = signal<JobState>('idle');
  protected state = this.stateSignal.asReadonly();
}
```

## ベストプラクティス
- 値はUnion型で定義し、`const assertions`でリテラル型を維持する
- SignalやComputedを使うと状態管理と分岐を同期させやすい
- テストでは各ケースに対する表示を確認して、状態遷移のバグを防ぐ

## 注意点
- `null`や`undefined`が渡る可能性がある場合はdefaultでフォローする
- 複雑な式を直接指定すると読みづらくなるためコンポーネントで事前計算
- case値の型が一致しないとマッチしないので注意

## 関連技術
- Angular Signals
- Enums / Literal Types
- AsyncPipe
