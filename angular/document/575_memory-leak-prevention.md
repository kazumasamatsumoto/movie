# #575 「メモリリーク防止」

## 概要
AsyncPipeを利用すると購読解除忘れによるメモリリークを防げる。特にコンポーネント破棄後も流れ続けるObservableを扱う際に有効。

## 学習目標
- 手動購読で発生しがちなメモリリークをAsyncPipeが防ぐ理由を理解する
- コンポーネントライフサイクルと購読解除の関係を学ぶ
- サービス側のリソース管理との組み合わせを把握する

## 技術ポイント
- AsyncPipeはView破棄時にunsubscribe
- ルータ遷移やngIfで表示が切り替わるケースでも安全
- サービス側でリソースを保持する場合は別途制御が必要

## 📺 画面表示用コード（動画用）
```html
<div *ngIf="show">
  <p>{{ stream$ | async }}</p>
</div>
```

## 💻 詳細実装例（学習用）
```typescript
@Component({
  selector: 'app-news',
  template: `<li *ngFor="let news of news$ | async">{{ news.title }}</li>`,
  standalone: true
})
export class NewsComponent {
  protected readonly news$ = this.newsService.latest$;
}
```

## ベストプラクティス
- AsyncPipeを使うことでunsubscribe漏れを防ぎ、保守性を高める
- ルータ遷移でコンポーネントが破棄されても安心
- カスタムPipeやサービスでプロデューサーを止めたい場合は別途制御

## 注意点
- AsyncPipeが購読解除しても、ホットObservableのプロデューサーは動き続ける場合があるためサービス側の設計も重要
- 即時subscribeが必要な処理はコンポーネントで行いつつ`takeUntilDestroyed`で解除
- AsyncPipeに頼りすぎてロジックが複雑化しないよう整理

## 関連技術
- takeUntilDestroyed
- shareReplay
- メモリリーク検知
