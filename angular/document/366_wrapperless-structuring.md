# #366 「ラッパー要素なしの構造化」

## 概要
`ng-container`や`ng-template`を活用するとラッパー要素を増やさずに構造ディレクティブを適用でき、既存レイアウトを崩さずにロジックを追加できる。

## 学習目標
- ラッパーレスで条件やループを適用する方法を理解する
- DOMを最小限に保つ設計手法を学ぶ
- アクセシビリティやスタイリングへの影響を最小化する

## 技術ポイント
- `ng-container`はDOMに出力されないため余計なdivが増えない
- `ng-template`はテンプレートを遅延評価し、必要時にだけ挿入
- Control Flow構文（@if/@for）への移行でも同様の考え方が活きる

## 📺 画面表示用コード（動画用）
```html
<ng-container *ngIf="visible">
  <button *ngFor="let action of actions">{{ action }}</button>
</ng-container>
```

## 💻 詳細実装例（学習用）
```typescript
@Component({
  selector: 'app-wrapperless-demo',
  standalone: true,
  imports: [CommonModule],
  template: `
    <header>
      <h2>{{ title }}</h2>
      <ng-container *ngIf="actions.length">
        <button *ngFor="let action of actions" type="button">{{ action }}</button>
      </ng-container>
    </header>
  `
})
export class WrapperlessDemoComponent {
  protected title = 'ラッパーレス構造';
  protected actions = ['保存', '共有'];
}
```

## ベストプラクティス
- マークアップ構造が重要な箇所ではラッパーを増やさず`ng-container`で制御
- CSSセレクタは`ng-container`を前提にせず、実際の要素に対して定義する
- Control Flow構文へ移行する際もDOM構造の最小化を意識する

## 注意点
- `ng-container`には属性を付けられないため、必要なら実体要素を用意する
- 複雑なロジックを内包すると読みにくくなるため、適宜コンポーネント分割を検討
- SSRで`ng-container`は出力されないが、テンプレートの整合性を確認する

## 関連技術
- ng-container
- Control Flow構文
- Accessibility
