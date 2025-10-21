# #335 「*ngIf - 条件付き表示」

## 概要
`*ngIf`は条件に応じて要素をDOMに追加または削除する構造ディレクティブで、表示制御とアクセシビリティを両立できる。

## 学習目標
- *ngIfの基本概念と用途を理解する
- CSS表示制御との違いを説明できる
- コンディション設計のポイントを学ぶ

## 技術ポイント
- 真偽値評価で要素の生成/破棄を行う
- else/thenテンプレートで分岐表示を整理
- `as`構文で値を再利用し、`null`ガードに使える

## 📺 画面表示用コード（動画用）
```html
<p *ngIf="isReady">ロード完了しました。</p>
<p *ngIf="!isReady">読み込み中...</p>
```

## 💻 詳細実装例（学習用）
```typescript
@Component({
  selector: 'app-ngif-demo',
  standalone: true,
  imports: [CommonModule],
  template: `
    <button type="button" (click)="toggle()">状態切替</button>
    <p *ngIf="loading; else content">読み込み中です...</p>
    <ng-template #content>
      <article>
        <h2>読み込み完了</h2>
        <p>{{ message }}</p>
      </article>
    </ng-template>
  `
})
export class NgIfDemoComponent {
  protected loading = true;
  protected message = 'データ取得が完了しました';

  protected toggle(): void {
    this.loading = !this.loading;
  }
}
```

## ベストプラクティス
- 状態はコンポーネントやSignalで管理し、テンプレートではシンプルな条件式に留める
- elseテンプレートを活用してローディング表示やエラー表示を整理する
- DOM生成/破棄が行われることを念頭に、フォーカス管理やアニメーションを考慮する

## 注意点
- 繰り返し評価される重い式を条件に書くとパフォーマンスが低下する
- `template reference`を利用する場合は参照スコープを理解する
- SSRで条件がずれるとHydrationエラーを誘発するため、サーバーとクライアントのロジックを一致させる

## 関連技術
- Angular Signals
- AsyncPipe
- Angular Universal
