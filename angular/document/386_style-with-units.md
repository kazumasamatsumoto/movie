# #386 「単位付き値の指定」

## 概要
`ngStyle`で数値を扱う際は`'16px'`のように単位を付けた文字列を渡す必要があり、テンプレートリテラルやヘルパーで統一的に管理すると安全である。

## 学習目標
- スタイル値に単位を付ける理由と方法を理解する
- テンプレートリテラルやヘルパー関数で単位を付与する手法を学ぶ
- 単位レスプロパティと単位必須プロパティの違いを把握する

## 技術ポイント
- `px`, `rem`, `%`などCSS単位を文字列として渡す
- `lineHeight`など一部プロパティは数値で扱えるが統一した方が可読性が高い
- ヘルパー`px(value)`などを用意すると再利用性が上がる

## 📺 画面表示用コード（動画用）
```html
<div [ngStyle]="{ width: width + 'px', height: height + 'px' }">サイズ</div>
```

## 💻 詳細実装例（学習用）
```typescript
@Component({
  selector: 'app-style-with-units-demo',
  standalone: true,
  imports: [CommonModule],
  template: `
    <div [ngStyle]="boxStyle()">リサイズ可能</div>
    <input type="range" min="100" max="300" [value]="size" (input)="update($event)" />
  `
})
export class StyleWithUnitsDemoComponent {
  protected size = 150;

  protected boxStyle(): Record<string, string> {
    return {
      width: `${this.size}px`,
      height: `${this.size}px`,
      borderRadius: '1rem',
      background: '#38bdf8'
    };
  }

  protected update(event: Event): void {
    this.size = Number((event.target as HTMLInputElement).value);
  }
}
```

## ベストプラクティス
- ヘルパー関数で単位付与を行い、テンプレートの文字列結合を減らす
- チームで使用する単位を統一し、`px`と`rem`が混在しないようにする
- 数値直接指定が可能なプロパティも読みやすさのために文字列化を検討

## 注意点
- `borderWidth={2}`など直接数値を渡すと意図しない描画になることがある
- 国際化対応で`rem`や`em`を使う場合、ベースフォントサイズに注意
- 単位付与をミスると`NaNpx`などが出力されるためバリデーションを加える

## 関連技術
- CSS単位
- テンプレートリテラル
- Angular Forms
