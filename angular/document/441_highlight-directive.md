# #441 「Highlight Directive - ハイライト」

## 概要
Highlightディレクティブは要素の背景色やアウトラインを変更して視覚的に強調し、ユーザーの注目を集める用途で利用する。

## 学習目標
- Highlightディレクティブの基本的な用途と仕組みを理解する
- HostListener/HostBindingを用いた色変更パターンを学ぶ
- フォーカス時やホバー時のアクセシビリティを向上させる

## 技術ポイント
- HostBindingで背景色/枠線をバインド
- HostListenerで`mouseenter`/`mouseleave`を監視
- Inputで色を動的に指定

## 📺 画面表示用コード（動画用）
```typescript
@HostBinding('style.backgroundColor') bg = '#fef08a';
@HostListener('mouseenter') activate(): void { this.bg = '#fde047'; }
@HostListener('mouseleave') deactivate(): void { this.bg = '#fef08a'; }
```

## 💻 詳細実装例（学習用）
```typescript
@Directive({
  selector: '[appHighlight]',
  standalone: true
})
export class HighlightDirective implements OnChanges {
  @Input('appHighlight') color = '#fde047';
  @Input() hoverColor = '#facc15';
  @HostBinding('style.backgroundColor') background = this.color;

  @HostListener('mouseenter')
  onEnter(): void {
    this.background = this.hoverColor;
  }

  @HostListener('mouseleave')
  onLeave(): void {
    this.background = this.color;
  }

  ngOnChanges(): void {
    this.background = this.color;
  }
}
```

## ベストプラクティス
- 色設定をInputで受け取り、デフォルト値を備えて柔軟性を確保
- フォーカスイベントも扱いキーボード操作に対応
- ARIA属性や説明を追加してアクセシビリティを向上

## 注意点
- インラインスタイルは優先度が高く、テーマとの整合性に注意
- ちらつきを避けるためtransitionをCSSで設定
- SSRでは初期色が適切に表示されるよう初期値を指定

## 関連技術
- HostBinding/HostListener
- Angular Signals
- Accessibility (focus可視化)
