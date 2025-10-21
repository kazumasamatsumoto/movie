# #458 「追加データの自動読み込み」

## 概要
追加データの自動読み込みはスクロール監視イベントでOutputを発火し、コンポーネント側がAPIを呼び出してリストを拡張するフローで実現する。

## 学習目標
- 自動読み込みのイベントフローを理解する
- Outputイベントを通じてサービス呼び出しを行う方法を学ぶ
- ローディング状態や重複呼び出し防止策を把握する

## 技術ポイント
- Outputで`loadMore`イベント
- コンポーネントでロード中フラグを管理
- 完了後にスクロール監視を再開

## 📺 画面表示用コード（動画用）
```html
<div appInfiniteScroll (scrolled)="loadMore()" [disabled]="loading"></div>
```

## 💻 詳細実装例（学習用）
```typescript
@Component({
  selector: 'app-infinite-list',
  standalone: true,
  imports: [CommonModule, InfiniteScrollDirective],
  template: `
    <div class="list" appInfiniteScroll (scrolled)="loadMore()" [disabled]="loading">
      <article *ngFor="let item of items">{{ item }}</article>
      <p *ngIf="loading">読み込み中...</p>
    </div>
  `
})
export class InfiniteListComponent {
  protected items = Array.from({ length: 20 }, (_, i) => `Item ${i}`);
  protected loading = false;

  protected loadMore(): void {
    if (this.loading) return;
    this.loading = true;
    fakeFetch(this.items.length).subscribe(more => {
      this.items = [...this.items, ...more];
      this.loading = false;
    });
  }
}
```

## ベストプラクティス
- ローディング状態中はディレクティブを無効化し重複読み込みを防止
- API失敗時のリトライやエラーメッセージを実装
- 読み込み完了（全件取得）をディレクティブへ知らせて監視停止

## 注意点
- すぐ末尾に到達するケースではループ的に呼ばれないよう初期データ量を調整
- モバイル環境ではスクロール速度が速いため適切なthresholdを設定
- 新規データが空の場合は監視を停止する

## 関連技術
- IntersectionObserver
- RxJS switchMap/concatMap
- Loadingインジケーター
