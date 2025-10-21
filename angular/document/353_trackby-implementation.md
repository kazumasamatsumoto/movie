# #353 「trackBy 関数の実装」

## 概要
trackBy関数は`*ngFor`が要素を識別するためのキーを返す純粋関数で、一意IDを返す実装が推奨される。

## 学習目標
- trackBy関数の署名と戻り値の制約を理解する
- 安定したキーを返す実装パターンを学ぶ
- テストとデバッグの観点を把握する

## 技術ポイント
- 引数: `(index: number, item: T) => string | number`
- 安定した一意キーを返し、配列操作後も再利用を促進
- 関数は副作用なく純粋であるべき

## 📺 画面表示用コード（動画用）
```typescript
trackById(_index: number, item: { id: number }) {
  return item.id;
}
```

## 💻 詳細実装例（学習用）
```typescript
@Component({
  selector: 'app-trackby-impl-demo',
  standalone: true,
  imports: [CommonModule],
  template: `
    <ul>
      <li *ngFor="let user of users; trackBy: trackUser">{{ user.name }}</li>
    </ul>
  `
})
export class TrackByImplDemoComponent {
  protected users = [
    { id: 1, name: 'めたん' },
    { id: 2, name: 'ずんだもん' }
  ];

  protected trackUser(_: number, user: { id: number }): number {
    return user.id;
  }
}
```

## ベストプラクティス
- IDがないデータにはハッシュ生成ではなくデータソースを見直す
- trackBy関数はコンポーネントメソッドとして定義し、テストしやすくする
- ユニットテストで同じIDが返っているか検証し、回 regressions を防止する

## 注意点
- `index`をそのまま返すと挿入やソートでDOM再利用が無効になる
- UUIDを毎回生成すると値が変わり続けるため逆効果
- trackBy関数内部で状態を変更すると再描画の原因になるので避ける

## 関連技術
- trackBy
- Pure Functions
- Unit Testing
