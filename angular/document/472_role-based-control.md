# #472 「ロールベースの表示制御」

## 概要
ロールベースの表示制御はInputで必要ロールを指定し、認可サービスで照会した結果に応じて要素の表示・非表示を切り替える。複数ロールや権限のOR/AND条件をサポートする設計が重要。

## 学習目標
- ロール条件の評価方法を理解する
- 認可サービスとディレクティブの連携を学ぶ
- 表示制御のモード（hidden/ngIf）を設計する

## 技術ポイント
- `@Input() appPermission: string | string[]`
- 認可サービス`hasRole`, `hasAllRoles`
- HostBindingまたは`ViewContainerRef`で表示制御

## 📺 画面表示用コード（動画用）
```html
<button appPermission="admin">管理者のみ</button>
```

## 💻 詳細実装例（学習用）
```typescript
@Directive({
  selector: '[appPermission]',
  standalone: true
})
export class PermissionDirective implements OnChanges {
  @Input('appPermission') roles: string | string[] = [];
  @Input() appPermissionMode: 'hidden' | 'remove' = 'hidden';

  constructor(
    private readonly auth: AuthService,
    private readonly viewContainer: ViewContainerRef,
    private readonly template: TemplateRef<unknown>
  ) {}

  ngOnChanges(): void {
    const required = Array.isArray(this.roles) ? this.roles : [this.roles];
    const allowed = required.length === 0 || required.some(role => this.auth.hasRole(role));
    if (allowed) {
      if (this.viewContainer.length === 0) {
        this.viewContainer.createEmbeddedView(this.template);
      }
    } else {
      if (this.appPermissionMode === 'remove') {
        this.viewContainer.clear();
      } else {
        if (this.viewContainer.length === 0) {
          this.viewContainer.createEmbeddedView(this.template);
        }
        this.viewContainer.element.nativeElement.style.display = 'none';
      }
    }
  }
}
```

## ベストプラクティス
- モード切り替えでDOM除去と単純な非表示を選択可能に
- 認可サービスはObservableで権限変更通知を提供
- ロール条件の組み合わせ（AND/OR）をInputで指定できるよう拡張

## 注意点
- 認可情報が非同期取得の場合は初期状態でチラつきが起こらないようfallback
- hiddenモードでは`display: none`を解除するタイミングに注意
- Role名のハードコードを避け、定数やEnumで管理

## 関連技術
- AuthService
- Structural Directive
- Angular Securityガイド
