# #452 「検索ボックスでの活用」

## 概要
検索ボックスにデバウンスを適用すると、タイプ入力のたびにAPIを呼ばず、一定時間後に検索を行うことで効率とユーザー体験が向上する。

## 学習目標
- デバウンスを検索ボックスに適用する利点を理解する
- Outputイベントをコンポーネントで受け取り検索処理へ繋ぐ方法を学ぶ
- ローディング制御やエラーハンドリングを組み合わせる

## 技術ポイント
- Debounceディレクティブを入力要素に適用
- Outputイベントで検索語を受け取りサービス呼び出し
- ローディング状態をUIへ反映

## 📺 画面表示用コード（動画用）
```html
<input appDebounce [debounceTime]="400" (debounce)="search($event)" />
```

## 💻 詳細実装例（学習用）
```typescript
@Component({
  selector: 'app-search-box',
  standalone: true,
  imports: [CommonModule, FormsModule, DebounceDirective],
  template: `
    <label>
      検索
      <input appDebounce [debounceTime]="400" (debounce)="search($event)" />
    </label>
    <p *ngIf="loading">検索中...</p>
    <ul>
      <li *ngFor="let item of results">{{ item }}</li>
    </ul>
  `
})
export class SearchBoxComponent {
  protected results: string[] = [];
  protected loading = false;

  protected search(keyword: string): void {
    this.loading = true;
    fakeApi(keyword).subscribe(data => {
      this.results = data;
      this.loading = false;
    });
  }
}
```

## ベストプラクティス
- 遅延時間はAPI性能やUXに合わせて調整
- 空文字入力時の処理（検索結果クリア等）を明確に定義
- ローディングインジケーターを表示しユーザーへフィードバック

## 注意点
- 迅速な応答が必要な場面では遅延がUXを損なうため要件確認
- 途中でAPIレスポンスが返る順序が変わる場合は結果の破棄条件を設定
- デバウンス後の検索が失敗した場合のエラーメッセージを表示

## 関連技術
- Observable検索（RxJS switchMap）
- Angular HttpClient
- DebounceDirective
