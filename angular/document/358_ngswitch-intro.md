# #358 「*ngSwitch - 多分岐」

## 概要
`*ngSwitch`は値に基づく多分岐をテンプレートで表現する構造ディレクティブで、条件を整理し読みやすい構造を提供する。

## 学習目標
- `*ngSwitch`の構造と用途を理解する
- `*ngSwitchCase`/`*ngSwitchDefault`の組み合わせ方を学ぶ
- 複数分岐を持つテンプレートの整理方法を知る

## 技術ポイント
- `[ngSwitch]="value"`で対象値を指定
- `*ngSwitchCase="'caseValue'"`で分岐を宣言
- どのケースにも一致しない場合は`*ngSwitchDefault`が表示

## 📺 画面表示用コード（動画用）
```html
<section [ngSwitch]="status">
  <p *ngSwitchCase="'loading'">読込中...</p>
  <p *ngSwitchCase="'done'">完了！</p>
  <p *ngSwitchDefault>未知の状態</p>
</section>
```

## 💻 詳細実装例（学習用）
```typescript
type Status = 'loading' | 'done' | 'error';

@Component({
  selector: 'app-switch-demo',
  standalone: true,
  imports: [CommonModule],
  template: `
    <section [ngSwitch]="status()">
      <p *ngSwitchCase="'loading'">読み込み中...</p>
      <p *ngSwitchCase="'done'">完了しました。</p>
      <p *ngSwitchCase="'error'">エラーが発生しました。</p>
      <p *ngSwitchDefault>未知の状態です。</p>
    </section>
    <button (click)="cycle()">状態を変更</button>
  `
})
export class SwitchDemoComponent {
  private readonly statuses: Status[] = ['loading', 'done', 'error'];
  private index = 0;
  private readonly statusSignal = signal<Status>('loading');
  protected status = this.statusSignal.asReadonly();

  protected cycle(): void {
    this.index = (this.index + 1) % this.statuses.length;
    this.statusSignal.set(this.statuses[this.index]);
  }
}
```

## ベストプラクティス
- 状態は列挙型やUnion型を使って型安全に管理する
- 複雑なUIは各ケースをコンポーネント化し、switch内には呼び出しのみ残す
- defaultケースを必ず用意し想定外の状態を可視化する

## 注意点
- case値は厳密比較（===）で判定されるため型と値を一致させる
- 大量のケースでテンプレートが長くなる場合は`@switch`構文も検討する
- SSRで状態がずれるとdefaultに落ちる可能性があるため初期値を合わせる

## 関連技術
- Union Types
- Angular Signals
- Control Flow構文
