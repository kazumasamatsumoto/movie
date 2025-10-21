# #450 「Debounce Directive - デバウンス」

## 概要
Debounceディレクティブは入力イベントなどを一定時間遅延させてから発火させる仕組みで、API呼び出しや検索処理の負荷を削減できる。

## 学習目標
- デバウンスの基本原理を理解する
- HostListenerでイベントを受け取り、タイマーやRxJSで遅延処理する方法を学ぶ
- Outputで遅延後のイベントを通知する設計を把握する

## 技術ポイント
- `setTimeout`/`clearTimeout`またはRxJS `debounceTime`
- Inputで待機時間を設定
- Outputで遅延後の値を通知

## 📺 画面表示用コード（動画用）
```typescript
@HostListener('input', ['$event.target.value']) onInput(value: string) { this.schedule(value); }
```

## 💻 詳細実装例（学習用）
```typescript
@Directive({
  selector: '[appDebounce]',
  standalone: true
})
export class DebounceDirective implements OnDestroy {
  @Input() debounceTime = 300;
  @Output() debounce = new EventEmitter<string>();
  private timer?: number;

  @HostListener('input', ['$event.target.value'])
  onInput(value: string): void {
    if (this.timer) {
      clearTimeout(this.timer);
    }
    this.timer = window.setTimeout(() => {
      this.debounce.emit(value);
    }, this.debounceTime);
  }

  ngOnDestroy(): void {
    if (this.timer) {
      clearTimeout(this.timer);
    }
  }
}
```

## ベストプラクティス
- Inputで待機時間を受け取り柔軟に調整
- `ngOnDestroy`でタイマーをクリアしメモリリークを防ぐ
- RxJSを利用してObservableに変換すると複雑なパターンにも対応

## 注意点
- ネイティブ`setTimeout`は数値が0の場合でも直ちに実行されるためエッジケースに注意
- SSRではwindowが存在しないためブラウザガードが必要
- 連続イベントの中で最新値のみ扱うため、必要な入力が失われないよう要件を確認

## 関連技術
- RxJS `debounceTime`
- EventEmitter
- Reactive Forms
