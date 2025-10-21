# #309 「@Directive デコレータ」

## 概要
`@Directive`デコレータはAngularにディレクティブのメタデータを提供し、selectorや依存サービス、ホスト設定などの構成情報を宣言する。

## 学習目標
- `@Directive`デコレータで指定できる主なプロパティを理解する
- hostメタデータやprovidersの設定方法を学ぶ
- Standaloneディレクティブに必要な構成を把握する

## 技術ポイント
- `selector`で適用対象を定義
- `standalone`, `host`, `providers`, `exportAs`などで挙動を調整
- デコレータはTypeScriptメタデータとしてコンパイル時に解析される

## 📺 画面表示用コード（動画用）
```typescript
@Directive({
  selector: '[appTooltip]',
  standalone: true,
  host: { '(mouseenter)': 'show()', '(mouseleave)': 'hide()', '[attr.aria-hidden]': '!visible' }
})
export class TooltipDirective {
  visible = false;
  show(): void { this.visible = true; }
  hide(): void { this.visible = false; }
}
```

## 💻 詳細実装例（学習用）
```typescript
export const TOOLTIP_REF = new InjectionToken<TooltipDirective>('TOOLTIP_REF');

@Directive({
  selector: '[appTooltip]',
  standalone: true,
  exportAs: 'appTooltip',
  host: { '(focus)': 'show()', '(blur)': 'hide()', '[class.tooltip-open]': 'visible' },
  providers: [{ provide: TOOLTIP_REF, useExisting: TooltipDirective }]
})
export class TooltipDirective {
  visible = false;

  constructor(private readonly overlay: TooltipOverlayService) {}

  show(): void {
    if (this.visible) return;
    this.visible = true;
    this.overlay.open(this);
  }

  hide(): void {
    if (!this.visible) return;
    this.visible = false;
    this.overlay.close(this);
  }
}

@Component({
  selector: 'app-tooltip-demo',
  standalone: true,
  imports: [CommonModule, TooltipDirective],
  template: `
    <button appTooltip #tooltip="appTooltip">フォーカスで表示</button>
    <p>状態: {{ tooltip.visible }}</p>
  `
})
export class TooltipDemoComponent {}
```

## ベストプラクティス
- `host`プロパティでHostBinding/HostListener相当の設定を一箇所にまとめる
- `providers`でトークンを公開し、複数Directive間の連携に活用する
- `exportAs`でテンプレート参照を提供し、ロジックを外部に漏らさない

## 注意点
- `providers`で`useExisting`を使うと循環参照に注意が必要
- `host`プロパティでコールされるメソッドは軽量に保ちパフォーマンスを確保する
- メタデータ変更後はテストでselectorやexport名の破壊的変更がないか確認する

## 関連技術
- InjectionToken
- HostBinding / HostListener
- Standalone Directives
