# #574 「自動購読解除」

## 概要
AsyncPipeはコンポーネントが破棄されると自動的にunsubscribeするため、手動で購読解除する必要がなく、メモリリークや不要な更新を防げる。

## 学習目標
- AsyncPipeが自動解除を行うタイミングを理解する
- 手動unsubscribeとの違いを学ぶ
- メモリリーク防止の観点からAsyncPipeを活用する理由を把握する

## 技術ポイント
- Viewが破棄されるとAsyncPipeが購読解除
- Observableの再購読は再描画時に行われる
- 手動subscriptionと組み合わせる必要はない

## 📺 画面表示用コード（動画用）
```html
<span>{{ data$ | async }}</span>
```

## 💻 詳細実装例（学習用）
```typescript
@Component({
  selector: 'app-counter',
  template: `<h3>{{ counter$ | async }}</h3>`,
  standalone: true
})
export class CounterComponent {
  protected readonly counter$ = interval(1000);
}
```

## ベストプラクティス
- コンポーネントでのsubscribeはできるだけAsyncPipeへ委譲
- 複数非同期ソースでも各々AsyncPipeに任せると安全
- Observableのリソース解放も自動化できる

## 注意点
- AsyncPipeで購読しているObservableが外部に副作用を持つ場合、解除後の挙動を確認
- `takeUntil`などと併用する必要は基本的にない
- 再びテンプレートに表示されると再購読が発生することを理解

## 関連技術
- AsyncPipe
- RxJS interval/timer
- メモリリーク防止パターン
