# #409 「マウスイベントの監視」

## 概要
マウスイベントはホバーやドラッグといったインタラクションを実現する上で重要で、HostListenerで`mouseenter`, `mouseleave`, `mousemove`等を監視してUIを制御できる。

## 学習目標
- 代表的なマウスイベントを理解する
- HostListenerで複数イベントを連動させる方法を学ぶ
- Renderer2やHostBindingと組み合わせてスタイルを変更する手順を把握する

## 技術ポイント
- `mouseenter`/`mouseleave`でホバー状態を管理
- `mousemove`で座標取得、`DragEvent`でドラッグ状態検知
- イベントオブジェクトは`MouseEvent`/`DragEvent`として型付け

## 📺 画面表示用コード（動画用）
```typescript
@HostListener('mouseenter') onEnter(): void { this.hover = true; }
@HostListener('mouseleave') onLeave(): void { this.hover = false; }
```

## 💻 詳細実装例（学習用）
```typescript
@Directive({
  selector: '[appHoverGlow]',
  standalone: true
})
export class HoverGlowDirective {
  @HostBinding('class.is-hover') hover = false;

  @HostListener('mouseenter')
  onEnter(): void {
    this.hover = true;
  }

  @HostListener('mouseleave')
  onLeave(): void {
    this.hover = false;
  }

  @HostListener('mousemove', ['$event.clientX', '$event.clientY'])
  onMove(x: number, y: number): void {
    console.log('mouse position', x, y);
  }
}
```

## ベストプラクティス
- 状態管理はboolean等でシンプルにし、スタイル変更はHostBindingで行う
- `mousemove`は頻繁に発火するためスロットリングを検討
- ドラッグ操作が必要ならHTML5 Drag & Drop APIや外部ライブラリと連携

## 注意点
- モバイルではマウスイベントが発火しないためフォールバックを準備
- イベント監視によるパフォーマンス影響をChrome DevToolsで計測
- `mousemove`は非同期処理を避け、必要なら`requestAnimationFrame`を使用

## 関連技術
- Renderer2
- DragEvent API
- RxJS throttleTime
