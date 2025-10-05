# #129 「Component 通信のセキュリティ考慮」

## 概要
Angular v20におけるコンポーネント通信でのセキュリティ考慮事項。適切なデータ検証とアクセス制御により、安全で信頼性の高いアプリケーションを構築するためのセキュリティ実装方法を学ぶ。

## 学習目標
- コンポーネント通信でのセキュリティリスクを理解する
- 適切なデータ検証手法を学ぶ
- アクセス制御の実装方法を把握する

## 技術ポイント
- 入力値の検証とサニタイゼーション
- 権限チェックとアクセス制御
- 機密データの適切な扱い
- XSS対策とCSRF対策

## 📺 画面表示用コード

### セキュアな入力検証
```typescript
interface SecureUserData {
  id: number;
  name: string;
  email: string;
  role: 'admin' | 'user';
}

@Component({
  selector: 'app-secure-component',
  template: `
    <div *ngIf="hasPermission">
      <h3>{{ sanitizedUserName }}</h3>
      <p>{{ sanitizedUserEmail }}</p>
    </div>
  `
})
export class SecureComponent implements OnInit {
  @Input() userData: SecureUserData | null = null;
  @Output() dataChange = new EventEmitter<SecureUserData>();
  
  hasPermission = false;
  sanitizedUserName = '';
  sanitizedUserEmail = '';
  
  constructor(private sanitizer: DomSanitizer) {}
  
  ngOnInit() {
    if (this.userData) {
      this.validateAndSanitizeData();
      this.checkPermissions();
    }
  }
  
  private validateAndSanitizeData() {
    if (!this.userData) return;
    
    // データ検証
    if (!this.isValidEmail(this.userData.email)) {
      throw new Error('Invalid email format');
    }
    
    // データサニタイゼーション
    this.sanitizedUserName = this.sanitizer.sanitize(
      SecurityContext.HTML, 
      this.userData.name
    ) || '';
    
    this.sanitizedUserEmail = this.sanitizer.sanitize(
      SecurityContext.HTML, 
      this.userData.email
    ) || '';
  }
  
  private checkPermissions() {
    // 権限チェック
    this.hasPermission = this.userData?.role === 'admin';
  }
  
  private isValidEmail(email: string): boolean {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
  }
}
```

### セキュアなService通信
```typescript
@Injectable()
export class SecureDataService {
  private _userRole = signal<'admin' | 'user'>('user');
  userRole = this._userRole.asReadonly();
  
  setUserRole(role: 'admin' | 'user') {
    // 権限チェック
    if (this.isValidRole(role)) {
      this._userRole.set(role);
    }
  }
  
  getSecureData(): Observable<SecureData> {
    // 権限チェック
    if (this.userRole() !== 'admin') {
      throw new Error('Insufficient permissions');
    }
    
    return this.http.get<SecureData>('/api/secure-data');
  }
  
  private isValidRole(role: string): boolean {
    return ['admin', 'user'].includes(role);
  }
}
```

## 実践的な活用例
- 管理者機能の実装
- ユーザーデータの保護
- 機密情報の表示制御

## ベストプラクティス
- 入力値の検証を必ず行う
- 権限チェックを適切に実装する
- データサニタイゼーションを忘れない
- セキュリティテストを実施する

## 注意点
- クライアントサイドの検証だけでは不十分
- サーバーサイドでの検証も必須
- 機密情報をクライアントサイドで扱わない

## 関連技術
- セキュリティ実装
- データ検証
- アクセス制御
- XSS/CSRF対策
