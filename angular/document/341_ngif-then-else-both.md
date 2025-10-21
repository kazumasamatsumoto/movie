# #341 「then/else 両方の指定」

## 概要
`*ngIf`でthen/else両方のテンプレートを指定すると、条件ごとの表示を明確に分離しつつテンプレートの重複を減らせる。

## 学習目標
- then/elseテンプレートの配置と命名を理解する
- 共通部分を抽出してテンプレートの重複を避ける
- 複雑な分岐を整理する構造化手法を学ぶ

## 技術ポイント
- `then`と`else`で別テンプレート参照を指定
- 共通部分は`ng-container`や子コンポーネントで抽出
- コンテキスト変数でテンプレートにデータを渡せる

## 📺 画面表示用コード（動画用）
```html
<div *ngIf="status === 'success'; then successTpl; else failTpl"></div>
<ng-template #successTpl><p>処理成功</p></ng-template>
<ng-template #failTpl><p>失敗しました</p></ng-template>
```

## 💻 詳細実装例（学習用）
```typescript
type LoadState = 'loading' | 'success' | 'error';

@Component({
  selector: 'app-then-else-both-demo',
  standalone: true,
  imports: [CommonModule],
  template: `
    <ng-container *ngIf="state() === 'success'; then successTpl; else pendingTpl"></ng-container>
    <ng-template #successTpl>
      <h2>ダッシュボード</h2>
      <p>最新データを表示します。</p>
    </ng-template>
    <ng-template #pendingTpl>
      <section *ngIf="state() === 'loading'; else errorTpl">
        <p>読み込み中...</p>
      </section>
    </ng-template>
    <ng-template #errorTpl>
      <p>読み込みに失敗しました。</p>
      <button type="button" (click)="retry()">再試行</button>
    </ng-template>
  `
})
export class ThenElseBothDemoComponent {
  private readonly stateSignal = signal<LoadState>('loading');
  protected state = this.stateSignal.asReadonly();

  protected retry(): void {
    this.stateSignal.set('loading');
    setTimeout(() => this.stateSignal.set('success'), 600);
  }
}
```

## ベストプラクティス
- テンプレート参照は`successTpl`, `errorTpl`のように役割を明確化する
- 共通部分は`ng-container`でまとめ、各ブロックの差分だけをテンプレートに残す
- テストで各状態が正しく切り替わることを確認し、回 regressions を防ぐ

## 注意点
- テンプレートが増えるとスコープが複雑になるため、命名規約を守る
- 多数の状態を分岐させる場合は`*ngSwitch`や新しい`@switch`構文を検討する
- SSRで状態が異なるとHydrationに失敗するため、初期値を一致させる

## 関連技術
- ng-container
- Angular Signals
- Template Composition
