# #364 「Structural Directive の組み合わせ」

## 概要
Structural Directiveを組み合わせると複雑なUIロジックを表現できるが、`ng-container`を使ってDOMの過剰増加を防ぎつつ責務を分割する必要がある。

## 学習目標
- 複数の構造ディレクティブを組み合わせるパターンを理解する
- DOM構造を整理するテクニックを学ぶ
- テンプレートを小さく保つリファクタリング戦略を把握する

## 技術ポイント
- 同一要素に複数構造ディレクティブは付けられないため、`ng-container`で分割
- 条件→ループ→分岐の順にロジックを整理すると読みやすい
- 複雑な場合は子コンポーネントへ責務を移譲

## 📺 画面表示用コード（動画用）
```html
<ng-container *ngIf="isReady">
  <li *ngFor="let item of items" [ngSwitch]="item.type"></li>
</ng-container>
```

## 💻 詳細実装例（学習用）
```typescript
@Component({
  selector: 'app-structural-combo-demo',
  standalone: true,
  imports: [CommonModule],
  template: `
    <ng-container *ngIf="items().length; else emptyTpl">
      <div *ngFor="let item of items(); trackBy: trackById">
        <ng-container [ngSwitch]="item.type">
          <p *ngSwitchCase="'text'">{{ item.value }}</p>
          <p *ngSwitchCase="'link'"><a [href]="item.href">{{ item.value }}</a></p>
          <p *ngSwitchDefault>未対応タイプ</p>
        </ng-container>
      </div>
    </ng-container>
    <ng-template #emptyTpl>
      <p>アイテムがありません。</p>
    </ng-template>
  `
})
export class StructuralComboDemoComponent {
  private readonly itemsSignal = signal([
    { id: 1, type: 'text', value: 'Hello Angular' },
    { id: 2, type: 'link', value: '公式ドキュメント', href: 'https://angular.dev' }
  ]);
  protected items = this.itemsSignal.asReadonly();

  protected trackById(_: number, item: { id: number }): number {
    return item.id;
  }
}
```

## ベストプラクティス
- `ng-container`でディレクティブを階層化し、意図的に構造を分ける
- 条件や分岐が複雑化したらコンポーネント分割を検討
- テンプレートが長くなりすぎないようにセクションごとにコメントを入れる

## 注意点
- `ng-container`を多用しすぎると理解が難しくなるためバランスをとる
- 子コンポーネントへ切り出す際はInput契約を明確にする
- パフォーマンス要件が高い場合は構造ディレクティブを自作してロジックを最適化する

## 関連技術
- ng-container
- Component Composition
- Custom Structural Directives
