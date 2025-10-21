# #365 「ng-container の活用」

## 概要
`ng-container`は実際のDOM要素を生成せずに構造ディレクティブを適用できる仮想コンテナで、マークアップをクリーンに保つのに役立つ。

## 学習目標
- ng-containerの役割と使い所を理解する
- DOMを増やさずにディレクティブを組み合わせる方法を学ぶ
- 条件分岐やループの整理術を身につける

## 技術ポイント
- `ng-container`はレンダリングされず、テンプレート内のみで存在
- 複数の構造ディレクティブを順番に適用する橋渡し役となる
- `#ref`を付けてテンプレート参照として使うことも可能

## 📺 画面表示用コード（動画用）
```html
<ng-container *ngIf="items.length">
  <li *ngFor="let item of items">{{ item }}</li>
</ng-container>
```

## 💻 詳細実装例（学習用）
```typescript
@Component({
  selector: 'app-ng-container-demo',
  standalone: true,
  imports: [CommonModule],
  template: `
    <ng-container *ngIf="menu().length; else emptyTpl">
      <button *ngFor="let action of menu()">{{ action }}</button>
    </ng-container>
    <ng-template #emptyTpl>
      <p>アクションがありません。</p>
    </ng-template>
  `
})
export class NgContainerDemoComponent {
  private readonly menuSignal = signal<string[]>(['保存', '共有', '削除']);
  protected menu = this.menuSignal.asReadonly();
}
```

## ベストプラクティス
- 不要なdivラップを避け、CSSやアクセシビリティに影響しない構造を保つ
- 複数ディレクティブを組み合わせる際に`ng-container`を挟む
- テンプレート内のロジックをブロックごとに整理し、読みやすさを向上させる

## 注意点
- `ng-container`はDOMに現れないため、スタイルやイベントを直接適用できない
- 過剰に入れ子にすると逆に読みにくくなるので節度を持つ
- テスト時にDOMへ現れないため、構造を理解するにはテンプレート理解が必要

## 関連技術
- ng-template
- Structural Directives
- Accessibility
