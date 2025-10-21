# #330 「Directive のデバッグ方法」

## 概要
ディレクティブのデバッグでは`ngDevMode`による条件ログやAngular DevTools、テストのSpyを活用し、ライフサイクルやホスト要素の状態を可視化する。

## 学習目標
- デバッグ時に有効なツールとテクニックを理解する
- ライフサイクルフックやHostBindingを検証する方法を学ぶ
- SSRやHydration環境でのデバッグ手法を知る

## 技術ポイント
- `ngDevMode`ガードで本番ビルドに影響を与えないログ出力
- Angular DevToolsのDirective検査タブを活用
- ユニットテストでHostBinding/ListenerをSpyする

## 📺 画面表示用コード（動画用）
```typescript
@Directive({ selector: '[appDebug]', standalone: true })
export class DebugDirective implements OnInit {
  ngOnInit(): void {
    if (ngDevMode) console.debug('DebugDirective init', this);
  }
}
```

## 💻 詳細実装例（学習用）
```typescript
@Directive({
  selector: '[appDebug]',
  standalone: true
})
export class DebugDirective implements OnInit, OnDestroy {
  @Input() label = 'debug';
  private remove?: () => void;

  constructor(private readonly el: ElementRef<HTMLElement>, private readonly renderer: Renderer2, private readonly zone: NgZone) {}

  ngOnInit(): void {
    if (ngDevMode) {
      console.debug(`[${this.label}] init`, this.el.nativeElement);
    }
    this.remove = this.renderer.listen(this.el.nativeElement, 'click', () => {
      if (ngDevMode) console.debug(`[${this.label}] click`, performance.now());
    });
  }

  ngOnDestroy(): void {
    this.remove?.();
    if (ngDevMode) {
      console.debug(`[${this.label}] destroy`);
    }
  }
}
```

## ベストプラクティス
- `ngDevMode`や環境変数でログを制御し、本番では排除する
- Angular DevToolsでホスト要素を選択し、Input/Outputの値変化を確認する
- テストでは`spyOn(renderer, 'listen')`などを使いイベントの登録状況を検証する

## 注意点
- 過剰なログはパフォーマンスを劣化させるため、条件付きで出力する
- SSR環境では`console`がモックされる場合があるためエラー処理を用意する
- デバッグ用属性を残したまま出荷しないように、ビルドパイプラインでチェックする

## 関連技術
- Angular DevTools
- ngDevMode
- Jasmine / Jest
