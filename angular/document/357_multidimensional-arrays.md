# #357 「多次元配列の表示」

## 概要
多次元配列はネストした`*ngFor`で表示でき、行列やグリッドの構造を表現する際に活用される。

## 学習目標
- 多次元配列のテンプレート展開を学ぶ
- 行ループと列ループの組み合わせを理解する
- 複合キーによるtrackBy実装を把握する

## 技術ポイント
- 外側ループで行を、内側ループで列を処理
- trackByで`rowIndex`と`colIndex`を組み合わせたキーを返す
- セルコンポーネントを導入すると責務分離が進む

## 📺 画面表示用コード（動画用）
```html
<tr *ngFor="let row of matrix; let rowIndex = index">
  <td *ngFor="let cell of row">{{ cell }}</td>
</tr>
```

## 💻 詳細実装例（学習用）
```typescript
@Component({
  selector: 'app-matrix-demo',
  standalone: true,
  imports: [CommonModule],
  template: `
    <table>
      <tr *ngFor="let row of matrix; let r = index">
        <td *ngFor="let cell of row; let c = index; trackBy: trackCell(r)">
          {{ cell }}
        </td>
      </tr>
    </table>
  `
})
export class MatrixDemoComponent {
  protected matrix = [
    ['A1', 'A2', 'A3'],
    ['B1', 'B2', 'B3']
  ];

  protected trackCell(rowIndex: number) {
    return (_: number, __: string, colIndex: number) => `${rowIndex}-${colIndex}`;
  }
}
```

## ベストプラクティス
- 行・列インデックスを明示し、テンプレート内で分かりやすくする
- セルの描画が複雑な場合は`<app-cell>`などに切り出す
- 変更検知コストを下げるため、matrixは不変構造で管理する

## 注意点
- trackByを使わないと大量のセルが再描画される可能性がある
- ネストが深いと可読性が落ちるため、コメントやコンポーネント分割を検討
- 行列のサイズが大きい場合は仮想化やページングを導入する

## 関連技術
- trackBy
- Angular CDK Table
- Component Composition
