# #290 「Drawer Component - サイドドロワー」

## 概要
Drawer Componentは画面の端から表示されるナビゲーションや設定パネルを提供し、位置・サイズ・開閉アニメーションを統一したコンポーネントである。

## 学習目標
- ドロワーの開閉制御をSignalで実装する
- 位置とサイズをInputで切り替える
- バックドロップとキーボード操作で閉じる処理を統一する

## 技術ポイント
- Standalone Component
- CSSトランジション
- キーボードアクセシビリティ

## 📺 画面表示用コード（動画用）
```typescript
@Component({ selector: 'app-drawer', standalone: true, template: `<div class="drawer-backdrop" [hidden]="!open" (click)="close()"></div><aside class="drawer" [class.open]="open" [class.right]="position==='right'" role="dialog" (keyup.escape)="close()"><ng-content></ng-content></aside>`, changeDetection: ChangeDetectionStrategy.OnPush })
export class DrawerComponent {
  @Input() position: 'left' | 'right' = 'left';
  @Input() open = false;
  @Output() openChange = new EventEmitter<boolean>();
  close(): void { this.openChange.emit(false); }
}
```

```css
.drawer { position: fixed; top: 0; bottom: 0; width: 320px; transform: translateX(-100%); transition: transform .3s ease; background: #fff; box-shadow: 0 8px 24px rgba(15,23,42,.18); }
.drawer.right { right: 0; transform: translateX(100%); }
.drawer.open { transform: translateX(0); }
.drawer-backdrop { position: fixed; inset: 0; background: rgba(15,23,42,.4); }
```

```html
<app-drawer [open]="menuOpen" (openChange)="menuOpen = $event">
  <nav>...</nav>
</app-drawer>
```

## 💻 詳細実装例（学習用）
```typescript
@Component({
  selector: 'app-drawer-demo',
  standalone: true,
  imports: [DrawerComponent],
  template: `
    <button type="button" (click)="toggle()">メニュー</button>
    <app-drawer [open]="isOpen()" (openChange)="setOpen($event)">
      <h2>メニュー</h2>
      <ul>
        <li><a href="#">ダッシュボード</a></li>
        <li><a href="#">設定</a></li>
      </ul>
    </app-drawer>
  `,
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class DrawerDemoComponent {
  private readonly state = signal(false);
  isOpen = this.state.asReadonly();
  toggle(): void { this.state.update(v => !v); }
  setOpen(value: boolean): void { this.state.set(value); }
}
```

## ベストプラクティス
- positionはInputで切り替え、RTL対応時に左右を反転できるようにする
- バックドロップクリックとEscapeキーで閉じる体験を統一する
- モバイルでは幅100%に切り替えるCSSを提供する

## 注意点
- フォーカス制御を追加し、開いたときにドロワー内部へフォーカスを移動する
- メニュー内のリンクにtabindexを適切に設定する
- bodyスクロール制御と組み合わせて背景スクロールを防ぐ

## 関連技術
- Signals
- CSSトランジション
- Accessibility
