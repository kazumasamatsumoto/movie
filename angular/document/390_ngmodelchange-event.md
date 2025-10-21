# #390 「ngModelChange イベント」

## 概要
`ngModelChange`はngModelが値を更新した際に発火するイベントで、新しい値を受け取って追加処理や入力検証を行える。

## 学習目標
- `ngModelChange`イベントの役割とタイミングを理解する
- `$event`から新値を取得しロジックを実行する方法を学ぶ
- 変更イベントをデバウンスするパターンを把握する

## 技術ポイント
- `(ngModelChange)="handler($event)"`で新しい値を取得
- `updateOn: 'blur'`設定時はフォーカスアウトでイベント発火
- RxJSの`Subject`や`debounceTime`で連打を防げる

## 📺 画面表示用コード（動画用）
```html
<input [(ngModel)]="keyword" (ngModelChange)="search($event)" />
```

## 💻 詳細実装例（学習用）
```typescript
@Component({
  selector: 'app-ngmodelchange-demo',
  standalone: true,
  imports: [CommonModule, FormsModule],
  template: `
    <input
      type="text"
      placeholder="キーワード"
      [(ngModel)]="keyword"
      (ngModelChange)="onKeywordChange($event)" />
    <p>変換後: {{ normalized }}</p>
  `
})
export class NgModelChangeDemoComponent {
  protected keyword = '';
  protected normalized = '';

  protected onKeywordChange(value: string): void {
    this.normalized = value.trim().toLowerCase();
  }
}
```

## ベストプラクティス
- 入力値の正規化やAPI検索など副作用処理を`ngModelChange`で分離する
- 連続入力による過剰な処理は`debounceTime`などで緩和
- `updateOn`を調整し、意図するタイミングでイベントが発火するように設計

## 注意点
- `[(ngModel)]="value"`と`(ngModelChange)="value = $event"`を同時に書くと二重更新になるため注意
- イベントが頻発するため重い処理を直接実行しない
- Reactive Formsと異なり`valueChanges`Observableはないので必要なら自分でSubjectを用意

## 関連技術
- RxJS debounceTime
- ngModelOptions
- Reactive Forms valueChanges
