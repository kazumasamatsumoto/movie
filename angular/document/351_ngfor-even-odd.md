# #351 「even / odd - 偶数/奇数の判定」

## 概要
`*ngFor`で`let isEven = even`や`let isOdd = odd`を使うと、偶数・奇数行でスタイルや表示内容を切り替えられる。

## 学習目標
- even/oddコンテキスト変数の使い方を理解する
- 行のスタイル分岐に活用する方法を学ぶ
- 条件付きクラス付与のベストプラクティスを把握する

## 技術ポイント
- `even`は偶数インデックス(0,2,4…)でtrue
- `odd`は奇数インデックス(1,3,5…)でtrue
- CSSクラスや属性を動的に付け替えて視認性を高める

## 📺 画面表示用コード（動画用）
```html
<tr *ngFor="let row of rows; let isOdd = odd"
    [class.is-odd]="isOdd">
  ...
</tr>
```

## 💻 詳細実装例（学習用）
```typescript
@Component({
  selector: 'app-even-odd-demo',
  standalone: true,
  imports: [CommonModule],
  template: `
    <table class="striped">
      <tr *ngFor="let row of rows; let isEven = even; let isOdd = odd"
          [class.striped__row--even]="isEven"
          [class.striped__row--odd]="isOdd">
        <td>{{ row }}</td>
      </tr>
    </table>
  `,
  styles: [`
    .striped__row--even { background: #f1f5f9; }
    .striped__row--odd { background: #e2e8f0; }
  `]
})
export class EvenOddDemoComponent {
  protected rows = ['Row A', 'Row B', 'Row C', 'Row D'];
}
```

## ベストプラクティス
- 視覚的な区別だけでなく`aria`属性でアクセシビリティも向上させる
- クラス名は`--even`/`--odd`などBEM風にして衝突を避ける
- 大量の行でも条件式が軽量なためパフォーマンスへの影響が小さい

## 注意点
- 奇数判定を`i % 2 === 1`で書くと`isOdd`との二重指定になるので控える
- ダイナミックに配列を操作する場合は再描画が発生することを想定する
- nestedな*ngForで同名の変数を定義すると可読性が低下する

## 関連技術
- CSS Utilityクラス
- trackBy
- Accessibility (ARIA)
