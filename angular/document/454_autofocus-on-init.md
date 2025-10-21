# #454 「表示時の自動フォーカス」

## 概要
表示時に自動フォーカスするには、ビューが初期化されたタイミングで`focus()`を呼び出し、ユーザーがすぐ入力できる状態にする。

## 学習目標
- 表示タイミングでフォーカスを設定するライフサイクルを理解する
- SSR環境でエラーにならないガード方法を学ぶ
- 遅延実行でフォーカスが確実に当たるようにするテクニックを把握する

## 技術ポイント
- `ngAfterViewInit`で`focus()`実行
- `requestAnimationFrame`や`setTimeout`で遅延
- `isPlatformBrowser`でブラウザチェック

## 📺 画面表示用コード（動画用）
```typescript
ngAfterViewInit(): void { requestAnimationFrame(() => this.el.nativeElement.focus()); }
```

## 💻 詳細実装例（学習用）
```typescript
@Directive({
  selector: '[appAutoFocusOnInit]',
  standalone: true
})
export class AutoFocusOnInitDirective implements AfterViewInit {
  constructor(
    private readonly el: ElementRef<HTMLElement>,
    @Inject(PLATFORM_ID) private readonly platformId: Object
  ) {}

  ngAfterViewInit(): void {
    if (!isPlatformBrowser(this.platformId)) return;
    requestAnimationFrame(() => this.el.nativeElement.focus());
  }
}
```

## ベストプラクティス
- `requestAnimationFrame`でDOM更新後にフォーカスを当てる
- ブラウザ判定を行い、SSRで例外を回避
- モーダルなど非同期表示はInputで遅延時間を別途指定

## 注意点
- タブキー操作の邪魔にならないよう、フォーカスが必要な場面に限定
- モバイルブラウザではフォーカス時にキーボードが開くためUXを考慮
- 多数のフォーカスディレクティブが同じ画面にあると競合が起きる

## 関連技術
- AfterViewInit
- PLATFORM_ID判定
- モーダルフォーカスマネジメント
