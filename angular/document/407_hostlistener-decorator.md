# #407 「@HostListener デコレータ」

## 概要
`@HostListener`デコレータはイベント監視の設定をメソッド宣言に直接紐づける仕組みで、イベント名と引数を配列形式で指定する。

## 学習目標
- デコレータの書式とパラメータを理解する
- `$event`やDOMプロパティを引数として受け取る方法を学ぶ
- デコレータを用いた複数イベント処理の設計を把握する

## 技術ポイント
- `@HostListener('keydown', ['$event.key'])`
- 引数はテンプレート文字列のように`$event.property`を指定
- 複数デコレータを同じメソッドに付けることも可能

## 📺 画面表示用コード（動画用）
```typescript
@HostListener('keydown', ['$event.key'])
handleKey(key: string): void { console.log(key); }
```

## 💻 詳細実装例（学習用）
```typescript
@Directive({
  selector: '[appKeyLogger]',
  standalone: true
})
export class KeyLoggerDirective {
  @HostListener('keydown', ['$event.key'])
  onKey(key: string): void {
    console.log('keydown:', key);
  }

  @HostListener('keyup', ['$event'])
  onKeyUp(event: KeyboardEvent): void {
    console.log('keyup with ctrl?', event.ctrlKey);
  }
}
```

## ベストプラクティス
- 必要十分なイベント情報だけを引数に渡し、メソッドをテストしやすく保つ
- デコレータの定義はクラス冒頭にまとめて読みやすさを確保
- `$event`ではなく型付き引数に変換することで安全性を高める

## 注意点
- HostListenerで`this`を利用する場合は必ずクラスプロパティとして定義
- 追加引数を忘れると`undefined`になり、予期せぬ挙動を招く
- 木構造の外側イベントはリスナー対象外なのでdocument/windowは別途設定が必要

## 関連技術
- EventEmitter
- Renderer2.listen
- Angular Signals
