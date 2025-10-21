# #451 「入力イベントの遅延」

## 概要
入力イベントを遅延させるデバウンスは、ユーザーがタイプを止めてから一定時間後に処理を行うことで、無駄なAPI呼び出しや状態更新を抑制する。

## 学習目標
- 入力デバウンス処理の仕組みを理解する
- タイマーやRxJSを用いた遅延処理の実装を学ぶ
- Outputで遅延処理後の結果を通知する方法を把握する

## 技術ポイント
- `setTimeout`/`clearTimeout`で最終入力だけ残す
- Inputで待機時間を設定
- Outputイベントで遅延後の値を通知

## 📺 画面表示用コード（動画用）
```typescript
@HostListener('input', ['$event.target.value'])
onInput(value: string): void { this.schedule(value); }
```

## 💻 詳細実装例（学習用）
```typescript
@Directive({
  selector: '[appInputDebounce]',
  standalone: true
})
export class InputDebounceDirective implements OnDestroy {
  @Input() delay = 300;
  @Output() debounceValue = new EventEmitter<string>();
  private timer?: number;

  @HostListener('input', ['$event.target.value'])
  handleInput(value: string): void {
    if (this.timer) {
      clearTimeout(this.timer);
    }
    this.timer = window.setTimeout(() => {
      this.debounceValue.emit(value);
    }, this.delay);
  }

  ngOnDestroy(): void {
    if (this.timer) {
      clearTimeout(this.timer);
    }
  }
}
```

## ベストプラクティス
- 遅延時間はコンポーネントから設定可能にし、シナリオごとに調整
- Outputイベントで最終値だけ通知し、フォームと連携
- `ngOnDestroy`でタイマーを解除しリークを防ぐ

## 注意点
- `window`利用時はSSRでエラーになるためブラウザチェックを行う
- 入力のたびにタイマーが生成されるため高頻度入力でも性能に影響がないか確認
- 0msに設定した場合の挙動を仕様として定義

## 関連技術
- RxJS `debounceTime`
- EventEmitter
- Reactive Forms
