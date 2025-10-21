# #367 「複数ディレクティブの適用」

## 概要
Structural Directiveは1要素に1つしか適用できないため、複数ディレクティブを組み合わせる場合は`ng-container`で要素を分割して適用する。

## 学習目標
- 複数ディレクティブを適用する制約を理解する
- `ng-container`を使った分割手法を学ぶ
- Attribute Directiveとの組み合わせパターンを把握する

## 技術ポイント
- Structural Directiveはテンプレートを置き換えるため共存できない
- `ng-container`や子コンポーネントで処理を段階的に適用
- Attribute Directiveは同一要素に併用可能

## 📺 画面表示用コード（動画用）
```html
<ng-container *ngIf="ready">
  <li *ngFor="let item of items">{{ item }}</li>
</ng-container>
```

## 💻 詳細実装例（学習用）
```typescript
@Component({
  selector: 'app-multi-directive-demo',
  standalone: true,
  imports: [CommonModule],
  template: `
    <ng-container *ngIf="filtered().length">
      <p *ngFor="let tag of filtered(); trackBy: trackByTag">{{ tag }}</p>
    </ng-container>
  `
})
export class MultiDirectiveDemoComponent {
  private readonly tagsSignal = signal(['Angular', 'Directive', 'Signals']);
  protected filtered = computed(() => this.tagsSignal().filter(tag => tag.length > 4));

  protected trackByTag(_: number, tag: string): string {
    return tag;
  }
}
```

## ベストプラクティス
- 複数の構造ディレクティブを順番に適用する際は`ng-container`で意図を明確にする
- コードレビューで過剰なディレクティブネストがないかチェックする
- Attribute Directiveはスタイル制御などと組み合わせ、テンプレートの責務を分離する

## 注意点
- `*ngIf`と`*ngFor`を同じ要素に書くとビルドエラーになる
- 分割のために増やした`ng-container`が過剰にならないようにする
- カスタムStructural Directiveを組み合わせる場合は命名や責務を明確にする

## 関連技術
- ng-container
- Attribute Directives
- Custom Structural Directives
