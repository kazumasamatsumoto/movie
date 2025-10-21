# #422 「Directive のカスタマイズ」

## 概要
DirectiveをInput/Outputでパラメータ化し、外部から挙動を設定できるようにすると再利用性が大きく向上する。

## 学習目標
- Directiveカスタマイズの基本戦略を理解する
- 設定オブジェクトの設計パターンを学ぶ
- カスタマイズポイントをドキュメント化する重要性を把握する

## 技術ポイント
- Inputでオプションを受け取りデフォルトとマージ
- Outputでイベントを通知し利用側で制御
- 設定値は型定義して可読性を高める

## 📺 画面表示用コード（動画用）
```typescript
@Input() appTooltip = { placement: 'top', delay: 200 };
```

## 💻 詳細実装例（学習用）
```typescript
export interface TooltipOptions {
  placement: 'top' | 'bottom' | 'left' | 'right';
  delay: number;
}

const DEFAULT_OPTIONS: TooltipOptions = { placement: 'top', delay: 150 };

@Directive({
  selector: '[appTooltip]',
  standalone: true
})
export class TooltipDirective implements OnChanges {
  @Input() appTooltip?: Partial<TooltipOptions>;
  private options: TooltipOptions = DEFAULT_OPTIONS;

  ngOnChanges(): void {
    this.options = { ...DEFAULT_OPTIONS, ...this.appTooltip };
  }
}
```

## ベストプラクティス
- 設定オブジェクトは`Partial`で受け取りデフォルトをマージ
- Optionsの型とデフォルト値をエクスポートし、利用側も参照できるようにする
- 変更に応じてドキュメントやStorybookを更新

## 注意点
- 無制限にオプションを増やすと責務過多になるため要件を精査
- 設定変更時に即反映が必要なら`ngOnChanges`で差分処理
- オプションに関するバリデーションを追加し、不正値を防ぐ

## 関連技術
- Partial型
- Storybook Controls
- Directive API設計
