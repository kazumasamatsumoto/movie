# #406 「HostListener - イベント監視」

## 概要
`HostListener`はディレクティブがホスト要素のイベントを簡潔に監視できるデコレータで、`addEventListener`を記述せず安全にイベント処理を実装できる。

## 学習目標
- HostListenerの基本的な役割を理解する
- イベント名と引数の指定方法を学ぶ
- ライフサイクルに沿ったイベント管理の重要性を知る

## 技術ポイント
- `@HostListener('eventName', ['arg'])`
- DI不要でイベントをバインド
- デコレータを付けたメソッドはDirective破棄時に自動解除

## 📺 画面表示用コード（動画用）
```typescript
@HostListener('click') handleClick(): void { console.log('clicked'); }
```

## 💻 詳細実装例（学習用）
```typescript
@Directive({
  selector: '[appLogClick]',
  standalone: true
})
export class LogClickDirective {
  @HostListener('click', ['$event'])
  handleClick(event: MouseEvent): void {
    console.log('[appLogClick]', event.target);
  }
}
```

## ベストプラクティス
- イベント名はDOMイベント準拠で小文字にする
- 必要な引数だけを`['$event']`などで受け取り、関数を軽量に保つ
- 複数イベントを監視する場合はメソッドを分け、責務を明確にする

## 注意点
- イベント処理に重いロジックを入れるとUIが遅延するためサービスに委譲
- Angular外でトリガーされるカスタムイベントを扱う場合は名前に注意
- HostListenerはホスト要素にのみ適用され、子要素のイベントは別途処理が必要

## 関連技術
- HostBinding
- Renderer2.listen
- Angular Lifecycle Hooks
