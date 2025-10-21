# #352 「trackBy - パフォーマンス最適化」

## 概要
`trackBy`は`*ngFor`でアイテムの識別子を返し、Angularが既存DOMノードを再利用できるようにする仕組みで描画性能を高める。

## 学習目標
- trackByの役割と効果を理解する
- trackBy関数のシグネチャと戻り値を学ぶ
- パフォーマンス改善のベストプラクティスを把握する

## 技術ポイント
- 関数のシグネチャは`trackBy(index, item)`で識別子を返却
- デフォルトはアイテム参照比較だが、trackByでカスタムキーを利用
- 大量リストや再ソート時の再描画削減に効果的

## 📺 画面表示用コード（動画用）
```html
<li *ngFor="let todo of todos; trackBy: trackById">
  {{ todo.title }}
</li>
```

## 💻 詳細実装例（学習用）
```typescript
interface Todo {
  id: string;
  title: string;
}

@Component({
  selector: 'app-trackby-demo',
  standalone: true,
  imports: [CommonModule],
  template: `
    <ul>
      <li *ngFor="let todo of todos; trackBy: trackById">{{ todo.title }}</li>
    </ul>
  `
})
export class TrackByDemoComponent {
  protected todos: Todo[] = [
    { id: 't1', title: 'Signal対応' },
    { id: 't2', title: 'Structural Directive' }
  ];

  protected trackById(_: number, todo: Todo): string {
    return todo.id;
  }
}
```

## ベストプラクティス
- 一意キー（IDなど）を返し、順序変更時も再利用できるようにする
- trackBy関数は状態を持たず、副作用のない純粋関数にする
- 複雑なロジックが必要ならサービスへ切り出しテストしやすくする

## 注意点
- 同じ値を返すとAngularが要素を区別できなくなる
- ウィジェット内で複数trackBy関数を定義する場合は命名に注意
- trackByを使っても大量DOMが生成されるとパフォーマンス問題は残る

## 関連技術
- ChangeDetectionStrategy.OnPush
- Angular Signals
- Virtual Scrolling
