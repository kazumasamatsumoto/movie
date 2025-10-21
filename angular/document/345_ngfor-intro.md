# #345 「*ngFor - 繰り返し表示」

## 概要
`*ngFor`はコレクションを反復して要素を生成する構造ディレクティブで、リストレンダリングの基本を提供する。

## 学習目標
- *ngForの基本的な役割を理解する
- テンプレート内で利用できるコンテキスト変数を把握する
- パフォーマンスのためにtrackByを意識する

## 技術ポイント
- `let item of items`構文で配列やIterableを展開
- `index`, `first`, `last`, `even`, `odd`, `count`などが利用可能
- `trackBy`でDOM再利用が促進される

## 📺 画面表示用コード（動画用）
```html
<li *ngFor="let task of tasks">{{ task.title }}</li>
```

## 💻 詳細実装例（学習用）
```typescript
interface Task {
  id: number;
  title: string;
}

@Component({
  selector: 'app-ngfor-demo',
  standalone: true,
  imports: [CommonModule],
  template: `
    <ul>
      <li *ngFor="let task of tasks; trackBy: trackById">
        {{ task.title }}
      </li>
    </ul>
  `
})
export class NgForDemoComponent {
  protected tasks: Task[] = [
    { id: 1, title: 'Directiveの学習' },
    { id: 2, title: 'コンポーネントの分割' }
  ];

  protected trackById(_: number, task: Task): number {
    return task.id;
  }
}
```

## ベストプラクティス
- データは不変オブジェクトとして扱い、変更時に新しい配列を生成する
- trackByを実装して再描画を最小化する
- コンポーネント側でソートやフィルタリングを行い、テンプレートをシンプルにする

## 注意点
- 長大なリストは仮想スクロールなどの最適化を検討する
- `index`をキーにすると順序入れ替えでDOMが再生成される
- 非同期データの扱いでは`AsyncPipe`で確実に購読解除する

## 関連技術
- trackBy
- Angular CDK Virtual Scroll
- AsyncPipe
