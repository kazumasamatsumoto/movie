# #356 「*ngFor のネスト」

## 概要
`*ngFor`をネストすると多次元データや親子関係を表示できるが、可読性とパフォーマンスに注意が必要である。

## 学習目標
- ネストした*ngForの書き方を理解する
- 外側コンテキスト変数を内側で使う方法を学ぶ
- ネスト深度に応じたリファクタリング戦略を把握する

## 技術ポイント
- 外側の変数は内側*ngForでも参照可能
- ネストが深い場合は子コンポーネント化して責務を分離
- trackByをそれぞれのループに実装すると再描画が抑えられる

## 📺 画面表示用コード（動画用）
```html
<div *ngFor="let group of groups">
  <p>{{ group.title }}</p>
  <span *ngFor="let item of group.items">{{ item }}</span>
</div>
```

## 💻 詳細実装例（学習用）
```typescript
interface Group {
  id: number;
  title: string;
  items: string[];
}

@Component({
  selector: 'app-ngfor-nesting-demo',
  standalone: true,
  imports: [CommonModule],
  template: `
    <section *ngFor="let group of groups; trackBy: trackGroup">
      <h3>{{ group.title }}</h3>
      <ul>
        <li *ngFor="let item of group.items; trackBy: trackItem">{{ item }}</li>
      </ul>
    </section>
  `
})
export class NgForNestingDemoComponent {
  protected groups: Group[] = [
    { id: 1, title: 'カテゴリA', items: ['A-1', 'A-2'] },
    { id: 2, title: 'カテゴリB', items: ['B-1', 'B-2', 'B-3'] }
  ];

  protected trackGroup(_: number, group: Group): number {
    return group.id;
  }

  protected trackItem(index: number): number {
    return index;
  }
}
```

## ベストプラクティス
- ネストが2段を超える場合は子コンポーネントに切り出し、テンプレートを簡潔にする
- トラックキーは階層ごとに決め、DOM再生成を抑える
- ネスト内で重い処理を避け、事前にデータを整形する

## 注意点
- インデックス変数名が衝突しないようにする
- 大量のネストはパフォーマンスに影響するため、仮想リストなどを検討
- 内側で外側の変数を変更すると予期せぬ副作用が起きる

## 関連技術
- Component Composition
- trackBy
- Angular CDK Tree
