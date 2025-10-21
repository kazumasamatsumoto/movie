# #419 「インタラクティブな実装」

## 概要
イベント監視と状態反映を組み合わせることで、ホバー、トグル、フォーカスハイライトなどインタラクティブなUIをディレクティブとして再利用できる。

## 学習目標
- 代表的なインタラクティブパターンを理解する
- 状態管理とDOM反映の設計を学ぶ
- デザインシステムへ組み込むための考慮事項を把握する

## 技術ポイント
- HostListenerでイベント取得、HostBindingでスタイル/クラス更新
- Inputで設定値を受け取り、複数シナリオに対応
- Outputでインタラクション結果を外部通知

## 📺 画面表示用コード（動画用）
```typescript
@HostListener('focus') onFocus(): void { this.focused = true; }
@HostBinding('class.is-focus') focused = false;
```

## 💻 詳細実装例（学習用）
```typescript
@Directive({
  selector: '[appInteractiveCard]',
  standalone: true
})
export class InteractiveCardDirective {
  @HostBinding('class.is-active') active = false;

  @HostListener('click')
  onClick(): void {
    this.active = !this.active;
  }

  @HostListener('keyup.enter')
  onEnter(): void {
    this.active = !this.active;
  }
}
```

## ベストプラクティス
- マウス・キーボード両方の操作をサポートしアクセシビリティを確保
- 状態をInput/Outputで外部と同期させると制御しやすい
- デザインシステムで利用例・制約を明文化する

## 注意点
- イベントの二重処理に注意し、ハンドラ内で停止制御が必要か検討
- 見た目の変化だけでなくARIA属性を更新して情報を伝える
- 状態を内部で保持する場合はリセットタイミングを明確にする

## 関連技術
- HostListener/HostBinding
- EventEmitter
- Accessibility
