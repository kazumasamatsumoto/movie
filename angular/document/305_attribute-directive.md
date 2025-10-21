# #305 「Attribute Directive - 属性ディレクティブ」

## 概要
Attribute Directiveは既存の要素に属性のように付与し、スタイルや振る舞いを局所的に変更する軽量なDOM拡張手法である。

## 学習目標
- Attribute Directiveの責務と利用場面を理解する
- HostBinding/HostListenerによるホスト要素制御を学ぶ
- Renderer2を使って安全にスタイルやクラスを変更する

## 技術ポイント
- 属性セレクタで既存要素へ付与
- `HostBinding`でプロパティ同期、`HostListener`でイベント処理
- Renderer2によるプラットフォーム非依存のDOM操作

## 📺 画面表示用コード（動画用）
```typescript
@Directive({ selector: '[appAccentBorder]', standalone: true })
export class AccentBorderDirective {
  @HostBinding('style.outline') outline = '2px solid #22d3ee';
  @HostListener('focus') onFocus(): void { this.outline = '2px solid #0ea5e9'; }
  @HostListener('blur') onBlur(): void { this.outline = '2px solid #22d3ee'; }
}
```

## 💻 詳細実装例（学習用）
```typescript
@Directive({
  selector: '[appAccentBorder]',
  standalone: true
})
export class AccentBorderDirective implements OnInit, OnDestroy {
  @Input() appAccentBorder = '#22d3ee';
  private removeFocus?: () => void;
  private removeBlur?: () => void;

  constructor(private readonly el: ElementRef<HTMLElement>, private readonly renderer: Renderer2) {}

  ngOnInit(): void {
    this.renderer.setStyle(this.el.nativeElement, 'outline', `2px solid ${this.appAccentBorder}`);
    this.removeFocus = this.renderer.listen(this.el.nativeElement, 'focus', () =>
      this.renderer.setStyle(this.el.nativeElement, 'outline-color', '#0ea5e9')
    );
    this.removeBlur = this.renderer.listen(this.el.nativeElement, 'blur', () =>
      this.renderer.setStyle(this.el.nativeElement, 'outline-color', this.appAccentBorder)
    );
  }

  ngOnDestroy(): void {
    this.removeFocus?.();
    this.removeBlur?.();
    this.renderer.removeStyle(this.el.nativeElement, 'outline');
  }
}

@Component({
  selector: 'app-accent-border-demo',
  standalone: true,
  imports: [CommonModule, FormsModule, AccentBorderDirective],
  template: `
    <input appAccentBorder [(ngModel)]="value" placeholder="属性ディレクティブの例" />
    <p>入力値: {{ value }}</p>
  `
})
export class AccentBorderDemoComponent {
  protected value = '';
}
```

## ベストプラクティス
- ビジュアル変更はHostBindingで初期値を与え、詳細な制御はRenderer2に委ねる
- 入力値は`@Input`で受け取り、可能なら`transform`オプションでバリデーションを行う
- イベントリスナーはクリーンアップ関数を保持し、ngOnDestroyで必ず解除する

## 注意点
- DOM構造を変更する場合は構造ディレクティブを検討し責務を混在させない
- 同一要素に複数Directiveを付与する際はCSSプロパティの衝突を確認する
- SSR環境ではフォーカスイベントが発火しないため、フォールバックを考慮する

## 関連技術
- HostBinding / HostListener
- Renderer2
- Angular Forms
