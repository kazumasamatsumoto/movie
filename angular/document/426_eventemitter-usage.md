# #426 「EventEmitter の使用」

## 概要
`EventEmitter`はAngularが提供するObservableベースのイベント発火クラスで、ディレクティブやコンポーネントからシンプルにイベントを通知できる。

## 学習目標
- EventEmitterの仕組みと使い方を理解する
- emitメソッドでペイロードを送る方法を学ぶ
- Observableとして公開するパターンを把握する

## 技術ポイント
- `new EventEmitter<T>()`で型付きイベントを宣言
- `emit(value)`で購読側へ通知
- `asObservable()`で読み取り専用にラップ可能

## 📺 画面表示用コード（動画用）
```typescript
@Output() toggled = new EventEmitter<boolean>();
```

## 💻 詳細実装例（学習用）
```typescript
@Directive({
  selector: '[appHoverEvent]',
  standalone: true
})
export class HoverEventDirective {
  private readonly hoverSubject = new EventEmitter<boolean>();

  @Output()
  get appHover(): Observable<boolean> {
    return this.hoverSubject.asObservable();
  }

  @HostListener('mouseenter')
  enter(): void {
    this.hoverSubject.emit(true);
  }

  @HostListener('mouseleave')
  leave(): void {
    this.hoverSubject.emit(false);
  }
}
```

## ベストプラクティス
- イベント型を明示し、利用側の補完を効かせる
- 必要に応じて`asObservable()`で公開し、外部から`emit`できないようにする
- DebounceやThrottleが必要なら利用側でRxJSオペレーターを適用

## 注意点
- EventEmitterはAngularゾーン内でemitされるため、外部非同期を扱う場合は`ngZone.run`でラップ
- `emit`を大量に呼び出すとChange Detectionコストが増える
- 完了・エラー通知はAngularでは推奨されず、`emit`のみ使用が一般的

## 関連技術
- RxJS Observable
- Angularゾーン
- Output双方向バインディング
