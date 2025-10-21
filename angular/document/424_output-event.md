# #424 「Output でのイベント発火」

## 概要
`@Output()`でEventEmitterを定義するとディレクティブから利用側へイベントを通知でき、UIの状態を外部と同期させられる。

## 学習目標
- Outputの宣言とemit方法を理解する
- カスタムイベントの設計指針を学ぶ
- OutputとInputの連携による双方向パターンを把握する

## 技術ポイント
- `@Output() toggled = new EventEmitter<boolean>();`
- `this.toggled.emit(true)`で通知
- `EventEmitter`をObservableとして公開する設計も可能

## 📺 画面表示用コード（動画用）
```typescript
@Output() appToggle = new EventEmitter<boolean>();
```

## 💻 詳細実装例（学習用）
```typescript
@Directive({
  selector: '[appToggle]',
  standalone: true
})
export class ToggleDirective {
  @Output() appToggle = new EventEmitter<boolean>();
  private state = false;

  @HostListener('click')
  onClick(): void {
    this.state = !this.state;
    this.appToggle.emit(this.state);
  }
}
```

## ベストプラクティス
- イベント名は`appSomething`や`somethingChange`など明確な契約を示す
- 型ファイルでイベントペイロードの型を共有し、利用側の安全性を高める
- 双方向バインディングが必要なら`@Output() valueChange`パターンを採用

## 注意点
- EventEmitterを`new EventEmitter(true)`とすると同期発火になるため注意
- イベント多発時は`auditTime`などで制御
- Outputが発火しないケース（無効状態など）をドキュメントに記載

## 関連技術
- EventEmitter
- SignalsとOutput
- 双方向バインディング
