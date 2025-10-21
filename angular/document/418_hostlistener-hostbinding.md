# #418 「HostListener + HostBinding」

## 概要
HostListenerでイベントを監視し、HostBindingで状態をDOMへ反映する組み合わせはインタラクティブなディレクティブ実装の基本パターンである。

## 学習目標
- HostListenerとHostBindingの連携フローを理解する
- 状態を更新する際のベストプラクティスを学ぶ
- UIへの反映をテストする方法を把握する

## 技術ポイント
- HostListenerで状態更新 → HostBindingでDOM反映
- 状態はプロパティまたはsignalで保持
- イベントと表示の責務を分離

## 📺 画面表示用コード（動画用）
```typescript
@HostBinding('class.is-active') active = false;
@HostListener('click') toggle(): void { this.active = !this.active; }
```

## 💻 詳細実装例（学習用）
```typescript
@Directive({
  selector: '[appHoverToggle]',
  standalone: true
})
export class HoverToggleDirective {
  @HostBinding('class.is-hover') hover = false;

  @HostListener('mouseenter')
  onEnter(): void {
    this.hover = true;
  }

  @HostListener('mouseleave')
  onLeave(): void {
    this.hover = false;
  }
}
```

## ベストプラクティス
- 状態更新はできるだけ同期で行い、非同期処理が必要な場合は明示的に管理
- HostBindingの値は読み取り専用プロパティにし、不変データで表現
- テストでイベント発火→DOM変化の連携を確認する

## 注意点
- 状態が複雑になる場合はサービスやSignalへ移譲
- 同じイベントを複数ディレクティブが処理する際は順序に注意
- SSRではイベントが発火しないため初期表示状態を一致させる

## 関連技術
- Angular Signals
- EventEmitter
- Testing Library
