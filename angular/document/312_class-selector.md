# #312 「クラスセレクタ .xxx」

## 概要
クラスセレクタはCSSクラスに紐づいてディレクティブを適用する方法で、既存のクラス命名と連動させたいときに有効。ただし命名衝突に注意が必要である。

## 学習目標
- クラスセレクタの書き方と適用方法を理解する
- 動的なクラス切り替えとディレクティブの連携方法を学ぶ
- プロジェクト全体での命名戦略を検討する

## 技術ポイント
- `selector: '.appDraggable'`のようにドット付きで指定
- テンプレートでは`class="appDraggable"`または`[class.appDraggable]="flag"`で適用
- HostBindingでクラス付与を補助し衝突を避ける

## 📺 画面表示用コード（動画用）
```typescript
@Directive({ selector: '.appDraggable', standalone: true })
export class DraggableDirective {
  constructor(private readonly el: ElementRef<HTMLElement>) {}
  ngOnInit(): void {
    this.el.nativeElement.setAttribute('draggable', 'true');
  }
}
```

## 💻 詳細実装例（学習用）
```typescript
@Directive({
  selector: '.appDraggable',
  standalone: true
})
export class DraggableDirective implements OnInit, OnDestroy {
  private removeListener?: () => void;

  constructor(private readonly el: ElementRef<HTMLElement>, private readonly renderer: Renderer2) {}

  ngOnInit(): void {
    const element = this.el.nativeElement;
    this.renderer.setAttribute(element, 'draggable', 'true');
    this.removeListener = this.renderer.listen(element, 'dragstart', event => {
      (event as DragEvent).dataTransfer?.setData('text/plain', element.id);
    });
  }

  ngOnDestroy(): void {
    this.removeListener?.();
    this.renderer.removeAttribute(this.el.nativeElement, 'draggable');
  }
}

@Component({
  selector: 'app-class-selector-demo',
  standalone: true,
  imports: [CommonModule, DraggableDirective],
  template: `
    <div class="appDraggable" id="drag-1">ドラッグ可能な要素</div>
    <div class="dropzone">ドロップ先</div>
  `,
  styles: [`
    .dropzone { margin-top: 1rem; padding: 1rem; border: 2px dashed #38bdf8; }
  `]
})
export class ClassSelectorDemoComponent {}
```

## ベストプラクティス
- プレフィックス付きのクラス名を採用し、外部ライブラリとの衝突を避ける
- 動的付与は`[class.appDraggable]="condition"`で制御し、不要なときはクラスを外す
- 仕様をドキュメント化し、他開発者が命名を誤用しないようにする

## 注意点
- CSSの責務と重ならないよう、スタイルは別クラスに委譲する
- コンパイル時にツリーシェイク対象にならないため、未使用判定を定期的に実施する
- SSRではドラッグイベントが発火しない点を考慮しフォールバックを用意する

## 関連技術
- Renderer2
- Drag and Drop API
- BEM/utilityクラス設計
