# #292 「Tooltip Component - ツールチップ」

## 概要
Tooltip Componentは要素に補足情報を表示するUIで、マウスホバーやフォーカス時に説明文を表示してアクセシビリティを向上させるコンポーネントである。

## 学習目標
- トリガーとツールチップの表示制御を実装する
- フォーカス操作でも表示できるようにする
- 位置・遅延・ARIA属性を管理する

## 技術ポイント
- hover/focusイベントのハンドリング
- @if制御フローによる表示切り替え
- aria-describedby

## 📺 画面表示用コード（動画用）
```typescript
@Component({ selector: 'app-tooltip', standalone: true, template: `<span class="tooltip-wrapper" (mouseenter)="show()" (mouseleave)="hide()" (focusin)="show()" (focusout)="hide()" (keyup.escape)="hide()"><ng-content></ng-content>@if (visible) {<span class="tooltip" role="tooltip" [id]="id">{{ message }}</span>}</span>`, changeDetection: ChangeDetectionStrategy.OnPush })
export class TooltipComponent {
  @Input({ required: true }) message!: string;
  @Input() id = crypto.randomUUID();
  visible = false;
  show(): void { this.visible = true; }
  hide(): void { this.visible = false; }
}
```

```css
.tooltip-wrapper { position: relative; display: inline-flex; align-items: center; }
.tooltip { position: absolute; bottom: calc(100% + 8px); left: 50%; transform: translateX(-50%); padding: 4px 8px; border-radius: 4px; background: rgba(15,23,42,.92); color: white; font-size: 12px; white-space: nowrap; }
```

```html
<app-tooltip message="保存されます" id="tooltip-save"><button type="button" aria-describedby="tooltip-save">保存</button></app-tooltip>
```

## 💻 詳細実装例（学習用）
```typescript
@Component({
  selector: 'app-tooltip-demo',
  standalone: true,
  imports: [TooltipComponent],
  template: `
    <app-tooltip message="パスワードは8文字以上です" id="pwd-tip">
      <label>
        パスワード
        <input type="password" aria-describedby="pwd-tip">
      </label>
    </app-tooltip>
  `,
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class TooltipDemoComponent {}
```

## ベストプラクティス
- マウスとキーボードの両方でツールチップを表示できるようにする
- aria-describedbyを用意し支援技術に説明文を提供する
- 表示位置と遅延をInput化しUXに合わせて調整できるようにする

## 注意点
- モバイルではタップやlongpressで表示する代替UIを検討する
- Tooltip内のテキストは短く、読み上げやすい文にする
- Escapeキーで閉じられるようキーボード操作を追加する

## 関連技術
- Content Projection
- Accessibility
- CSS Positioning
