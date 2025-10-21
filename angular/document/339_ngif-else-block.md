# #339 「else ブロックの使用」

## 概要
`*ngIf`のelseブロックは条件が偽のときに表示するテンプレートで、フォールバックUIを明示的に定義できる。

## 学習目標
- elseブロックを設計・管理する方法を理解する
- テンプレート参照スコープを適切に扱う
- 共通のfallbackテンプレートを再利用する

## 技術ポイント
- `else`で参照するテンプレートは同一スコープ内に定義
- `ng-container`と併用してDOMを増やさずに管理
- テンプレートにコンテキストを渡して汎用性を高める

## 📺 画面表示用コード（動画用）
```html
<article *ngIf="items.length; else empty">リスト表示</article>
<ng-template #empty><p>項目がありません。</p></ng-template>
```

## 💻 詳細実装例（学習用）
```typescript
@Component({
  selector: 'app-else-block-demo',
  standalone: true,
  imports: [CommonModule],
  template: `
    <ul *ngIf="products.length; else emptyTpl">
      <li *ngFor="let product of products">{{ product }}</li>
    </ul>
    <ng-template #emptyTpl>
      <p>商品が登録されていません。</p>
      <button type="button" (click)="seed()">ダミーデータを追加</button>
    </ng-template>
  `
})
export class ElseBlockDemoComponent {
  protected products: string[] = [];

  protected seed(): void {
    this.products = ['Angular Handbook', 'Directive Mastery'];
  }
}
```

## ベストプラクティス
- Fallbackテンプレートに操作方法や次のアクションを明記する
- 複数の要素で使う場合は`ng-template`を別コンポーネントへ切り出す
- テストでは真偽両ケースを検証し、テンプレートが正しく切り替わるか確認する

## 注意点
- elseテンプレートに含まれる要素は表示時に新しく生成されるため、フォーム状態などがリセットされる
- ネストした`*ngIf`で`#elseTpl`を共有するとスコープが衝突する場合がある
- SSRでは条件がずれるとHydrationエラーになるため、判定を揃える

## 関連技術
- ng-container
- Angular Testing Library
- SSR/Hydration
