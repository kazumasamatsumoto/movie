# #471 「Permission Directive - 権限制御」

## 概要
Permissionディレクティブはユーザー権限に応じて要素を表示・非表示にし、UIでアクセス制御を行う。ロールベース認可サービスと連携して実装する。

## 学習目標
- 権限制御ディレクティブの設計思想を理解する
- 認可サービスから権限情報を取得する仕組みを学ぶ
- 表示制御とARIA対応を組み合わせた実装を把握する

## 技術ポイント
- Inputで必要ロール/権限を受け取る
- 認可サービス`hasRole`/`hasPermission`をDI
- HostBindingやngIfで表示制御

## 📺 画面表示用コード（動画用）
```typescript
@Input('appPermission') requiredRoles: string[] = [];
```

## 💻 詳細実装例（学習用）
```typescript
@Directive({
  selector: '[appPermission]',
  standalone: true
})
export class PermissionDirective implements OnChanges {
  @Input('appPermission') roles: string[] = [];
  @HostBinding('hidden') hidden = false;

  constructor(private readonly auth: AuthService) {}

  ngOnChanges(): void {
    const allowed = this.roles.length === 0 || this.roles.some(role => this.auth.hasRole(role));
    this.hidden = !allowed;
  }
}
```

## ベストプラクティス
- 認可条件はInputで柔軟に指定し、デフォルトは表示
- `hidden`ではなく`ngIf`でDOMから除去する方法も提供
- サービスのキャッシュやObservableで非同期権限にも対応

## 注意点
- SSRでは権限情報がまだ取得できない場合があるのでガード処理
- UI非表示だけでなくバックエンド側でも検証が必須
- 認可ロジック変更に合わせてディレクティブも更新

## 関連技術
- AuthService
- Role-based Access Control
- Structural Directive (ngIf)
