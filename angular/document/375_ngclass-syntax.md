# #375 「[ngClass] の基本構文」

## 概要
`[ngClass]`では任意の式を評価してクラス名を設定でき、文字列・配列・オブジェクトのいずれかで柔軟に指定できる。

## 学習目標
- `[ngClass]`の記述方法を理解する
- 各データ形式がどのようにクラスへ変換されるか把握する
- 拡張性を考えたクラス制御の設計を学ぶ

## 技術ポイント
- 文字列: スペース区切りで複数クラス付与
- 配列: 要素ごとにクラス付与、Falsyは無視
- オブジェクト: 真偽値で付与可否を決定

## 📺 画面表示用コード（動画用）
```html
<div [ngClass]="{ badge: true, 'badge--warn': level === 'warn' }">
  ステータス
</div>
```

## 💻 詳細実装例（学習用）
```typescript
@Component({
  selector: 'app-ngclass-syntax-demo',
  standalone: true,
  imports: [CommonModule],
  template: `
    <p [ngClass]="statusClasses">現在のステータス: {{ level }}</p>
    <button type="button" (click)="cycle()">切り替え</button>
  `
})
export class NgClassSyntaxDemoComponent {
  private readonly levels = ['info', 'warn', 'error'] as const;
  private index = 0;
  protected level = this.levels[this.index];

  protected get statusClasses(): (string | undefined)[] | Record<string, boolean> {
    return [
      'status',
      this.level === 'warn' ? 'status--warning' : undefined,
      this.level === 'error' ? 'status--error' : undefined
    ];
  }

  protected cycle(): void {
    this.index = (this.index + 1) % this.levels.length;
    this.level = this.levels[this.index];
  }
}
```

## ベストプラクティス
- 条件式が複雑になる前にコンポーネントで派生データを準備する
- undefinedやnullを返すとクラスが付与されないことを活用して分岐を整理
- 共有のクラスセットは定数として切り出し、再利用性を高める

## 注意点
- 文字列でスペルミスするとスタイルが適用されないのでレビューで検出
- 配列形式では空文字がクラスとして残るため、`undefined`を返す
- オブジェクト形式は`__proto__`のような特殊キーを避ける

## 関連技術
- CSS BEM記法
- Angular Signals
- Tailwind / Utility-first CSS
