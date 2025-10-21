# #430 「設定可能な実装」

## 概要
設定可能なディレクティブはオプションオブジェクトを受け取り、デフォルト設定とマージして多様なユースケースに対応できる柔軟性を持つ。

## 学習目標
- 設定可能な実装パターンを理解する
- デフォルト設定とのマージ方法を学ぶ
- 設定変更時のバリデーションとエラーハンドリングを把握する

## 技術ポイント
- `@Input() options?: Partial<Settings>;`
- `const config = { ...DEFAULT, ...options };`
- `ngOnChanges`で検証し、必要ならログや例外を投げる

## 📺 画面表示用コード（動画用）
```typescript
@Input() appTooltipOptions?: Partial<TooltipOptions>;
```

## 💻 詳細実装例（学習用）
```typescript
interface RippleOptions {
  color: string;
  duration: number;
}

const DEFAULT_RIPPLE: RippleOptions = { color: '#38bdf8', duration: 250 };

@Directive({
  selector: '[appRipple]',
  standalone: true
})
export class RippleDirective implements OnChanges {
  @Input() appRipple?: Partial<RippleOptions>;
  private options = DEFAULT_RIPPLE;

  ngOnChanges(): void {
    this.options = { ...DEFAULT_RIPPLE, ...this.appRipple };
    if (this.options.duration < 0) {
      console.warn('[appRipple] duration must be >= 0');
      this.options = { ...this.options, duration: 0 };
    }
  }
}
```

## ベストプラクティス
- 設定値はオブジェクトにまとめ、型で制約をかける
- 不正値が渡った場合の対処（デフォルトへ戻す、例外を投げる）を決めておく
- 設定APIはドキュメントとStorybookでわかりやすく提示する

## 注意点
- Optional設定が増えるとユーザーが混乱するため、必要最低限に
- 変更がある度にドキュメントを更新し、破壊的変更を避ける
- 設定オブジェクトを直接ミューテートせず、イミュータブルに扱う

## 関連技術
- Partial型
- Storybook Controls
- OnChangesライフサイクル
