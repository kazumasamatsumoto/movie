# #376 「文字列でのクラス指定」

## 概要
`[ngClass]`に文字列を渡すと、その文字列をスペース区切りで分割してクラスを適用できる。既存の`class`属性ともマージされるためシンプルなトグルに向いている。

## 学習目標
- 文字列形式でのクラス指定方法を理解する
- class属性との併用時の挙動を把握する
- 条件によって文字列を切り替えるパターンを学ぶ

## 技術ポイント
- 文字列はスペースで分割され複数クラスに展開
- バインディング式で条件演算子を使い切り替え可能
- 既存classと重複した場合は`DOMTokenList`が重複を排除

## 📺 画面表示用コード（動画用）
```html
<p [ngClass]="isDark ? 'badge badge--dark' : 'badge'">テーマ</p>
```

## 💻 詳細実装例（学習用）
```typescript
@Component({
  selector: 'app-ngclass-string-demo',
  standalone: true,
  imports: [CommonModule],
  template: `
    <label>
      <input type="checkbox" [checked]="isDark" (change)="toggle()" />
      ダークモード
    </label>
    <p class="badge" [ngClass]="isDark ? 'badge--dark badge--outline' : 'badge--light'">
      現在: {{ isDark ? 'Dark' : 'Light' }}
    </p>
  `,
  styles: [`
    .badge { display: inline-block; padding: 0.25rem 0.75rem; border-radius: 9999px; }
    .badge--dark { background: #0f172a; color: #fff; }
    .badge--light { background: #e0f2fe; color: #0f172a; }
    .badge--outline { border: 1px solid currentColor; }
  `]
})
export class NgClassStringDemoComponent {
  protected isDark = false;

  protected toggle(): void {
    this.isDark = !this.isDark;
  }
}
```

## ベストプラクティス
- 可読性のためにクラス名はスペース区切りで整理し、テンプレートに複雑な式を入れすぎない
- 文字列生成はテンプレートリテラルよりも条件演算子で簡潔に書く
- 共有クラスは事前に`class`属性へ記述し、バインディング側は条件による追加に集中させる

## 注意点
- 末尾に余分なスペースを付けると空クラスが生成される
- 大量の条件式を文字列結合で行うと読みづらくなるため他形式へ移行
- テンプレート内で難読なテンプレートリテラルを使うと保守性が下がる

## 関連技術
- class属性
- テンプレート式
- CSSユーティリティ
