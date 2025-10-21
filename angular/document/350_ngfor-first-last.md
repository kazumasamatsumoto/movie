# #350 「first / last - 最初/最後の判定」

## 概要
`*ngFor`で`let isFirst = first`や`let isLast = last`を使うと、先頭・末尾要素に対して条件付きでUIを変更できる。

## 学習目標
- `first`/`last`の真偽値を利用する方法を理解する
- 区切り線やボタン表示などの制御パターンを学ぶ
- 複数条件と組み合わせて柔軟なスタイル制御を行う

## 技術ポイント
- `first`は最初のアイテムでtrue、`last`は最後のアイテムでtrue
- `even`/`odd`と併用して複雑な条件を表現可能
- DOM構造を変えずにスタイルや要素表示を切り替えられる

## 📺 画面表示用コード（動画用）
```html
<li *ngFor="let step of steps; let isLast = last">
  {{ step }}<span *ngIf="!isLast">→</span>
</li>
```

## 💻 詳細実装例（学習用）
```typescript
@Component({
  selector: 'app-ngfor-first-last-demo',
  standalone: true,
  imports: [CommonModule],
  template: `
    <ul class="timeline">
      <li *ngFor="let step of steps; let isFirst = first; let isLast = last"
          [class.timeline__item--first]="isFirst"
          [class.timeline__item--last]="isLast">
        {{ step }}
      </li>
    </ul>
  `,
  styles: [`
    .timeline { list-style: none; padding: 0; }
    .timeline__item--first { font-weight: 700; }
    .timeline__item--last::after { content: ' ✅'; }
  `]
})
export class NgForFirstLastDemoComponent {
  protected steps = ['要件定義', '実装', 'テスト', 'リリース'];
}
```

## ベストプラクティス
- スタイル変更はCSSクラスバインディングを使い、テンプレートを簡潔に保つ
- `last`を活用して区切り線やボタンを制御し、無駄な要素を生成しない
- 先頭・末尾で異なるコンポーネントを表示したい場合は`ng-container`と組み合わせる

## 注意点
- リスト更新時も`first`/`last`は再評価されるため、条件に依存した副作用は避ける
- ネストしたリストで外側と内側の変数名が衝突しないようにする
- trackBy未設定だとDOM再生成が起きやすく、スタイルがちらつく可能性がある

## 関連技術
- CSSクラスバインディング
- trackBy
- Structural Directiveコンテキスト変数
