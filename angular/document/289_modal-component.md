# #289 「Modal Component - モーダルダイアログ」

## 概要
Modal Componentはユーザーの注意を引くためのダイアログUIを提供し、バックドロップ・フォーカストラップ・ESCキー対応を備えた実装を共有する。

## 学習目標
- CDK Overlayを利用したモーダル表示を実装する
- フォーカストラップとアクセシビリティ属性を整える
- 開閉状態をSignalで管理する

## 技術ポイント
- Angular CDK Overlay
- FocusTrap
- 動的コンポーネント生成

## 📺 画面表示用コード（動画用）
```typescript
@Component({ selector: 'app-modal', standalone: true, template: `<div class="backdrop" (click)="close()"></div><section class="modal" cdkTrapFocus role="dialog" [attr.aria-labelledby]="labelId"><header><ng-content select="[slot=header]"></ng-content></header><div class="body"><ng-content></ng-content></div><footer><ng-content select="[slot=footer]"></ng-content></footer></section>`, changeDetection: ChangeDetectionStrategy.OnPush })
export class ModalComponent {
  @Input({ required: true }) labelId!: string;
  @Output() dismissed = new EventEmitter<void>();
  close(): void { this.dismissed.emit(); }
}
```

```typescript
@Injectable({ providedIn: 'root' })
export class ModalService {
  private readonly overlay = inject(Overlay);
  open(component: ComponentType<unknown>): OverlayRef {
    const ref = this.overlay.create({ hasBackdrop: true, positionStrategy: this.overlay.position().global().centerHorizontally().centerVertically() });
    ref.attach(new ComponentPortal(component));
    return ref;
  }
}
```

```html
<app-modal [labelId]="'dialog-title'" (dismissed)="close()">
  <h2 slot="header" id="dialog-title">設定</h2>
  <p>通知の頻度を選択してください。</p>
  <div slot="footer"><button type="button" (click)="close()">閉じる</button></div>
</app-modal>
```

## 💻 詳細実装例（学習用）
```typescript
@Component({
  selector: 'app-modal-demo',
  standalone: true,
  imports: [ModalComponent, ButtonComponent],
  template: `
    <button type="button" (click)="open()">モーダルを開く</button>
    <ng-template [ngIf]="opened()">
      <app-modal [labelId]="titleId" (dismissed)="close()">
        <h2 slot="header" [id]="titleId">お知らせ</h2>
        <p>最新バージョンが利用可能です。</p>
        <div slot="footer">
          <button type="button" (click)="close()">閉じる</button>
        </div>
      </app-modal>
    </ng-template>
  `,
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class ModalDemoComponent {
  readonly titleId = 'modal-title';
  private readonly state = signal(false);
  readonly opened = this.state.asReadonly();
  open(): void { this.state.set(true); }
  close(): void { this.state.set(false); }
}
```

## ベストプラクティス
- role="dialog"とaria-labelledbyでアクセシビリティを担保する
- フォーカストラップはCDKの`cdkTrapFocus`で簡潔に実装する
- オーバーレイはサービス化し再利用しやすくする

## 注意点
- 開いたときにフォーカスを最初のフォーカス可能要素に移動する
- バックドロップクリックを無効にしたい場合はInputで切り替える
- スクロール制御をbodyクラスで行い背景操作を禁止する

## 関連技術
- Angular CDK Overlay
- FocusTrap
- Signals
