# #338 「*ngIf=\"condition; else template\"」

## 概要
`*ngIf="expr; else tpl"`は条件が偽のときに表示するテンプレートを指定でき、待機状態やエラー表示を整理できる。

## 学習目標
- elseテンプレートの指定方法を学ぶ
- テンプレート参照変数のスコープを理解する
- 再利用可能なfallbackテンプレートを設計する

## 技術ポイント
- `else`に指定するのは`<ng-template #name>`の参照
- テンプレート内でコンテキストを受け取るため`let-`構文を利用できる
- 多数の条件分岐はthen/else構文へ発展させられる

## 📺 画面表示用コード（動画用）
```html
<section *ngIf="data; else loading">データ表示</section>
<ng-template #loading><p>読み込み中です...</p></ng-template>
```

## 💻 詳細実装例（学習用）
```typescript
@Component({
  selector: 'app-ngif-else-demo',
  standalone: true,
  imports: [CommonModule],
  template: `
    <section *ngIf="user(); else fallback">
      <h3>{{ user()!.name }}</h3>
      <p>{{ user()!.email }}</p>
    </section>
    <ng-template #fallback>
      <p>ユーザー情報を取得できませんでした。</p>
      <button type="button" (click)="retry()">再試行</button>
    </ng-template>
  `
})
export class NgIfElseDemoComponent {
  private readonly store = signal<{ name: string; email: string } | null>(null);
  protected user = this.store.asReadonly();

  protected retry(): void {
    setTimeout(() => {
      this.store.set({ name: 'Retry User', email: 'retry@example.com' });
    }, 500);
  }
}
```

## ベストプラクティス
- Fallbackテンプレートは別ファイルや再利用可能なテンプレートにまとめる
- `let-error`のようにコンテキスト変数を渡して詳細を表示できる設計にする
- else部分でもフォーカスやアクセシビリティを考慮する

## 注意点
- elseテンプレートは`ng-template`内でのみ記述でき、他要素では使用できない
- `if`側が破棄されるとDOM状態がリセットされることを意識する
- 同じテンプレート参照を複数箇所で使うときは意図しない共有がないか確認する

## 関連技術
- Template Reference Variables
- Angular Signals
- Retryパターン
