# #332 「* (アスタリスク) 構文の意味」

## 概要
`*`構文はAngularの構造ディレクティブを簡潔に記述するための糖衣構文で、実際は`<ng-template>`へ展開される。

## 学習目標
- `*`構文が内部でどう展開されるか理解する
- 展開後のテンプレート構造を読めるようになる
- カスタムStructural Directive実装時のヒントを得る

## 技術ポイント
- `*directive="expr"` → `<ng-template [directive]="expr"></ng-template>`
- `TemplateRef`と`ViewContainerRef`が展開後のテンプレートを扱う
- `let`宣言や`as`構文も展開時に属性へ変換される

## 📺 画面表示用コード（動画用）
```html
<p *ngIf="flag">Asterisk syntax</p>
<!-- 展開後: <ng-template [ngIf]="flag"><p>...</p></ng-template> -->
```

## 💻 詳細実装例（学習用）
```typescript
@Directive({
  selector: '[appSugar]',
  standalone: true
})
export class SugarDirective implements OnInit {
  @Input({ alias: 'appSugar' }) condition = false;

  constructor(private readonly view: ViewContainerRef, private readonly template: TemplateRef<unknown>) {}

  ngOnInit(): void {
    if (this.condition) {
      this.view.createEmbeddedView(this.template);
    }
  }
}

@Component({
  selector: 'app-sugar-demo',
  standalone: true,
  imports: [CommonModule, SugarDirective],
  template: `
    <p *appSugar="isEnabled">Directiveは<ng-template>に展開される</p>
    <ng-template [appSugar]="isEnabled">
      <p>手動で書くとこうなります。</p>
    </ng-template>
  `
})
export class SugarDemoComponent {
  protected isEnabled = true;
}
```

## ベストプラクティス
- 複雑な条件式はテンプレートではなくコンポーネントで計算し、`*`構文内はシンプルに保つ
- 展開後の形を理解しておくとデバッグやカスタム実装が容易になる
- 差分検出を最適化するために、テンプレート内で重い処理を避ける

## 注意点
- `*`構文は1要素に1つだけ適用可能で、複数付与するとビルドエラーになる
- 展開を意識せずにネストするとDOM構造が深くなる可能性がある
- 直接`<ng-template>`を書く場合はコンテキスト変数の指定を忘れない

## 関連技術
- TemplateRef
- ViewContainerRef
- Angular Template Syntax
