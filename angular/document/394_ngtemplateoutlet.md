# #394 「ngTemplateOutlet - テンプレート挿入」

## 概要
`ngTemplateOutlet`はテンプレート参照を外部から注入し、指定されたコンテキストでレンダリングするディレクティブでレイアウトカスタマイズに役立つ。

## 学習目標
- `ngTemplateOutlet`の使い方とコンテキスト渡しを理解する
- テンプレート差し替えを行うコンポーネント設計を学ぶ
- `ngTemplateOutletContext`の構造を把握する

## 技術ポイント
- `[ngTemplateOutlet]="tpl"`でテンプレート参照を指定
- `[ngTemplateOutletContext]="{ $implicit: value }"`で値を渡す
- `$implicit`以外にも任意のキーで渡せる

## 📺 画面表示用コード（動画用）
```html
<ng-container [ngTemplateOutlet]="itemTpl" [ngTemplateOutletContext]="{ $implicit: item }"></ng-container>
```

## 💻 詳細実装例（学習用）
```typescript
@Component({
  selector: 'app-template-outlet-demo',
  standalone: true,
  imports: [CommonModule],
  template: `
    <ng-container *ngFor="let task of tasks" [ngTemplateOutlet]="taskTpl" [ngTemplateOutletContext]="{ $implicit: task }"></ng-container>
    <ng-template #taskTpl let-task>
      <p class="task">{{ task }}</p>
    </ng-template>
  `
})
export class TemplateOutletDemoComponent {
  protected tasks = ['レビュー', '実装', 'リリース'];
}
```

## ベストプラクティス
- コンポーネントの`@Input() template?: TemplateRef`を活用すると利用側でレイアウトを差し替えられる
- コンテキストのキーはdocs化し、テンプレート側が迷わないようにする
- Defaultテンプレートを用意して、未指定でも動作する堅牢なAPIにする

## 注意点
- 渡すテンプレートのライフサイクルに注意し、nullチェックを行う
- 複雑なテンプレートを注入すると可読性が下がるためファイル分割を検討
- SSRでテンプレート切り替えが正しく描画されるか確認する

## 関連技術
- TemplateRef
- ViewContainerRef
- Content Projection
