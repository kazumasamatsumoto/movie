# #411 「event オブジェクトの取得」

## 概要
HostListenerで`$event`を受け取るとネイティブイベントオブジェクトにアクセスでき、詳細なイベント情報を利用した処理が可能になる。

## 学習目標
- `$event`引数の取得方法を理解する
- 型注釈で安全にイベントプロパティへアクセスする
- イベント情報をビジネスロジックへ伝搬させる手法を学ぶ

## 技術ポイント
- `@HostListener('click', ['$event'])`
- TypeScriptの型（`MouseEvent`, `KeyboardEvent`など）を付与
- 必要に応じて引数を複数渡す（`['$event', '$event.target']`）

## 📺 画面表示用コード（動画用）
```typescript
@HostListener('click', ['$event']) onClick(event: MouseEvent) { console.log(event.clientX); }
```

## 💻 詳細実装例（学習用）
```typescript
@Directive({
  selector: '[appCaptureEvent]',
  standalone: true
})
export class CaptureEventDirective {
  @HostListener('mousemove', ['$event'])
  onMove(event: MouseEvent): void {
    const { clientX, clientY } = event;
    console.log(`mouse at ${clientX}, ${clientY}`);
  }
}
```

## ベストプラクティス
- 型注釈を付けてIDE補完と安全性を向上
- イベント情報をサービスやEventEmitterへ渡して再利用
- 必要なプロパティだけを抽出し、ロジックを軽量に保つ

## 注意点
- イベントが頻繁に発火する場合はパフォーマンスに注意
- カスタムイベントは型定義が必要になる場合がある
- `$event.target`は`EventTarget`型なので`instanceof`で絞り込む

## 関連技術
- HostListener
- EventEmitter
- TypeScript型ガード
