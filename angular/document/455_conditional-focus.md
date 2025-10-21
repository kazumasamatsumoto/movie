# #455 「条件付きフォーカス」

## 概要
条件付きフォーカスではInputで受け取った条件が真の場合にのみフォーカスを当て、例えばバリデーションエラー時のフォーカス誘導などを実現する。

## 学習目標
- 条件付きフォーカスの仕組みを理解する
- Inputとライフサイクルを組み合わせた実装を学ぶ
- バリデーションと連携したフォーカス誘導パターンを把握する

## 技術ポイント
- `@Input() appAutoFocusIf = false;`
- `ngOnChanges`で条件を評価してフォーカス
- フォーカス済みのときは不要な再フォーカスを避ける

## 📺 画面表示用コード（動画用）
```typescript
@Input() appAutoFocusIf = false;
ngOnChanges(): void { if (this.appAutoFocusIf) this.focus(); }
```

## 💻 詳細実装例（学習用）
```typescript
@Directive({
  selector: '[appAutoFocusIf]',
  standalone: true
})
export class AutoFocusIfDirective implements OnChanges {
  @Input() appAutoFocusIf = false;
  @Input() focusDelay = 0;
  private focused = false;

  constructor(
    private readonly el: ElementRef<HTMLElement>,
    @Inject(PLATFORM_ID) private readonly platformId: Object
  ) {}

  ngOnChanges(): void {
    if (!isPlatformBrowser(this.platformId)) return;
    if (this.appAutoFocusIf && !this.focused) {
      setTimeout(() => {
        this.el.nativeElement.focus();
        this.focused = true;
      }, this.focusDelay);
    } else if (!this.appAutoFocusIf) {
      this.focused = false;
    }
  }
}
```

## ベストプラクティス
- フォーカス済みかどうかを記録し不必要な再フォーカスを避ける
- Inputで遅延時間や条件を設定し柔軟性を持たせる
- バリデーションエラー時にフォーカスを誘導してUXを向上

## 注意点
- 状態が頻繁に変わるとfocus/blurが繰り返されUXが低下するため条件を精査
- SSRではエラーになるためブラウザチェックを行う
- フォーカス制御はユーザー操作を阻害しないよう慎重に扱う

## 関連技術
- OnChanges
- Angular Formsバリデーション
- Accessibility (focus management)
