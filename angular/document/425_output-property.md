# #425 「@Output() プロパティ」

## 概要
`@Output()`で宣言したプロパティはイベントエミッターとして利用側へ公開でき、ディレクティブ内のイベントを外へ伝搬する。

## 学習目標
- Outputプロパティの宣言方法を理解する
- イベント型と型安全な`emit`呼び出しを学ぶ
- Observableとして公開する設計パターンを把握する

## 技術ポイント
- `@Output() change = new EventEmitter<MyEvent>();`
- `change.asObservable()`で読み取り専用公開
- `@Output('appChange')`でイベント名エイリアス指定

## 📺 画面表示用コード（動画用）
```typescript
@Output('appToggle') toggled = new EventEmitter<boolean>();
```

## 💻 詳細実装例（学習用）
```typescript
@Directive({
  selector: '[appPress]',
  standalone: true
})
export class PressDirective {
  @Output() appPress = new EventEmitter<{ x: number; y: number }>();

  @HostListener('click', ['$event'])
  onClick(event: MouseEvent): void {
    this.appPress.emit({ x: event.clientX, y: event.clientY });
  }
}
```

## ベストプラクティス
- イベントペイロードの型を別ファイルで定義し、利用側も参照できるようにする
- Observableとして公開する場合は`readonly`アクセサを提供
- Outputは非同期発火がデフォルトのため、同期が必要な場合は理由を明記

## 注意点
- EventEmitterはAngular固有の仕組みであり、RxJS Subjectとの違いを理解
- Output名とInput名が衝突しないよう命名に注意
- Outputを内部でsubscribeしない（自己購読するとリークの原因）

## 関連技術
- EventEmitter vs Subject
- @Outputエイリアス
- Angularテンプレートバインディング
