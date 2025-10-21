# #473 「権限チェック」

## 概要
権限チェックは認可サービスを通じてユーザーの権限を確認し、指定したパーミッションがあるかどうかを判定してUIを制御する。非同期チェックにも対応が必要。

## 学習目標
- 権限チェックの基本ロジックを理解する
- 同期・非同期権限データの扱いを学ぶ
- チェック結果をディレクティブに反映する方法を把握する

## 技術ポイント
- AuthServiceの`hasPermission`や`observePermissions`
- Observableを`async`パイプやsubscribeで処理
- 非同期完了までloading状態を表示

## 📺 画面表示用コード（動画用）
```typescript
const allowed = this.auth.hasPermission(permission);
```

## 💻 詳細実装例（学習用）
```typescript
@Injectable({ providedIn: 'root' })
export class AuthService {
  private readonly permissions$ = new BehaviorSubject<string[]>(['read', 'write']);

  hasPermission(permission: string): boolean {
    return this.permissions$.value.includes(permission);
  }

  observePermissions(): Observable<string[]> {
    return this.permissions$.asObservable();
  }
}

@Directive({
  selector: '[appPermissionCheck]',
  standalone: true
})
export class PermissionCheckDirective implements OnDestroy {
  @Input('appPermissionCheck') permission = '';
  @HostBinding('hidden') hidden = true;
  private sub?: Subscription;

  constructor(private readonly auth: AuthService) {}

  ngOnInit(): void {
    this.sub = this.auth.observePermissions().subscribe(perms => {
      this.hidden = !perms.includes(this.permission);
    });
  }

  ngOnDestroy(): void {
    this.sub?.unsubscribe();
  }
}
```

## ベストプラクティス
- AuthServiceで権限情報をObservableとして提供し、リアルタイム更新に対応
- ディレクティブ側ではサブスクリプション管理を徹底
- 権限エラー時にはユーザーに提示するメッセージも用意

## 注意点
- ネットワーク遅延で権限判定が遅れる場合、初期表示をどうするか決める
- クライアント側の権限チェックだけでは不十分でサーバー側でも検証が必要
- 多数のディレクティブが権限チェックを行う場合、キャッシュを活用

## 関連技術
- AuthService/Permissions
- BehaviorSubject
- Async Pipe
