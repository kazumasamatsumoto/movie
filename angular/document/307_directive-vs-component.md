# #307 「Directive vs Component の違い」

## 概要
DirectiveとComponentは共通の基盤を持ちながら、テンプレートの有無やUI構築の責務によって役割が分かれている。適切な選択がアプリの保守性を左右する。

## 学習目標
- DirectiveとComponentの共通点と差異を明確に説明できる
- 適切な抽象を選ぶ判断基準を身につける
- 二者を組み合わせた設計パターンを理解する

## 技術ポイント
- Componentは`@Component`デコレータでテンプレートとスタイルを持つ
- Directiveは`@Directive`で既存DOMに振る舞いを追加する
- 双方とも依存注入やライフサイクルフックを共有する

## 📺 画面表示用コード（動画用）
```typescript
@Directive({ selector: '[appFocusTrap]', standalone: true })
export class FocusTrapDirective {}

@Component({
  selector: 'app-focus-trap',
  standalone: true,
  template: `<div appFocusTrap><ng-content /></div>`
})
export class FocusTrapComponent {}
```

## 💻 詳細実装例（学習用）
```typescript
@Directive({
  selector: '[appFocusTrap]',
  standalone: true
})
export class FocusTrapDirective implements OnInit, OnDestroy {
  private removeListener?: () => void;

  constructor(private readonly el: ElementRef<HTMLElement>, private readonly renderer: Renderer2) {}

  ngOnInit(): void {
    const element = this.el.nativeElement;
    this.removeListener = this.renderer.listen(element, 'keydown', event => {
      if ((event as KeyboardEvent).key !== 'Tab') return;
      // 実際のフォーカストラップ処理は省略
    });
  }

  ngOnDestroy(): void {
    this.removeListener?.();
  }
}

@Component({
  selector: 'app-focus-trap',
  standalone: true,
  imports: [CommonModule, FocusTrapDirective],
  template: `
    <section appFocusTrap role="dialog" aria-modal="true" class="dialog">
      <header><ng-content select="[slot=title]" /></header>
      <div class="dialog__body"><ng-content /></div>
    </section>
  `,
  styles: [`
    .dialog { padding: 1.5rem; background: #fff; border-radius: 1rem; }
    .dialog__body { margin-top: 1rem; }
  `]
})
export class FocusTrapComponent {}
```

## ベストプラクティス
- UIを伴う場合はコンポーネント化し、付加的な振る舞いはディレクティブに分離する
- 同じ機能でも表示責務の有無で二層構成にし、テスト対象を明確にする
- APIはコンポーネントが外部契約、ディレクティブが内部補助という役割で整理する

## 注意点
- Directiveへテンプレートを追加すると責務が曖昧になり保守が困難
- Componentへ過度なDOM操作を入れるとSRPが崩れるためDirectiveへ委譲する
- どちらもChangeDetectionに影響するため、必要に応じて`OnPush`や`signal`で制御する

## 関連技術
- Standalone Components
- HostDirectives
- Angular CDK
