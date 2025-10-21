# #442 「マウスオーバーで色変更」

## 概要
マウスオーバー時に色を変更するディレクティブはホバーでスタイルを強調し、ユーザーへインタラクション可能であることを示せる。

## 学習目標
- ホバーイベントを利用した色変更ロジックを理解する
- HostListenerとHostBindingの組み合わせを学ぶ
- フォーカス時の同等挙動を提供しアクセシビリティ対応を行う

## 技術ポイント
- `mouseenter`/`mouseleave`で背景色を切り替え
- `focus`/`blur`も扱いキーボード操作に対応
- Renderer2またはHostBindingでスタイル適用

## 📺 画面表示用コード（動画用）
```typescript
@HostListener('mouseenter') onEnter(): void { this.bg = this.hoverColor; }
@HostListener('mouseleave') onLeave(): void { this.bg = this.baseColor; }
```

## 💻 詳細実装例（学習用）
```typescript
@Directive({
  selector: '[appHoverHighlight]',
  standalone: true
})
export class HoverHighlightDirective {
  @Input() baseColor = '#fef08a';
  @Input() hoverColor = '#facc15';

  @HostBinding('style.backgroundColor') background = this.baseColor;

  @HostListener('mouseenter')
  handleEnter(): void {
    this.background = this.hoverColor;
  }

  @HostListener('mouseleave')
  handleLeave(): void {
    this.background = this.baseColor;
  }

  @HostListener('focus')
  handleFocus(): void {
    this.background = this.hoverColor;
  }

  @HostListener('blur')
  handleBlur(): void {
    this.background = this.baseColor;
  }
}
```

## ベストプラクティス
- キーボード使用時のため`focus`/`blur`も監視
- Inputで色を受け取りテーマや状態に合わせて変更
- 変化をCSS transitionで滑らかにする

## 注意点
- 要素が`display: inline`の場合は背景色が期待通り表示されないことがある
- 透過色を指定すると背景と重なり合うので注意
- イベント重複（SPデバイスのタッチ）にも配慮する

## 関連技術
- HostBinding
- HostListener
- CSS Transition
