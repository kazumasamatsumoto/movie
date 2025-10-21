# #382 「[ngStyle] の基本構文」

## 概要
`[ngStyle]`はオブジェクトでスタイルプロパティと値を指定する構文で、複数スタイルをまとめて適用できる。

## 学習目標
- `[ngStyle]`の記法を理解する
- プロパティ名と値の書き方を把握する
- 条件式や計算を交えたスタイル適用を習得する

## 技術ポイント
- プロパティ名はキャメルケースまたはハイフンを含む文字列
- 数値は文字列に変換されるため単位を付与する
- Falsy値でスタイル解除を表現できる

## 📺 画面表示用コード（動画用）
```html
<div [ngStyle]="{ borderColor: accentColor, borderWidth: border + 'px', borderStyle: 'solid' }"></div>
```

## 💻 詳細実装例（学習用）
```typescript
@Component({
  selector: 'app-ngstyle-syntax-demo',
  standalone: true,
  imports: [CommonModule],
  template: `
    <div [ngStyle]="boxStyle">ボックス</div>
  `
})
export class NgStyleSyntaxDemoComponent {
  protected border = 2;
  protected accentColor = '#38bdf8';

  protected get boxStyle(): Record<string, string> {
    return {
      borderColor: this.accentColor,
      borderWidth: `${this.border}px`,
      borderStyle: 'solid',
      padding: '1rem',
      borderRadius: '0.75rem'
    };
  }
}
```

## ベストプラクティス
- コンポーネントでスタイルオブジェクトを組み立て、テンプレートのロジックを最小化
- 単位を付け忘れないようテンプレートリテラルを利用する
- 共有スタイルはCSSクラスとして定義し、ngStyleは差分に限定する

## 注意点
- 文字列にハイフンを含むプロパティは`'background-color'`のようにクォートが必要
- 大規模なスタイル制御はビューの責務が膨らむため専用ディレクティブ化を検討
- 変更検知で頻繁にオブジェクトが再生成される場合はメモ化が有効

## 関連技術
- Renderer2
- CSSカスタムプロパティ
- HostBinding
