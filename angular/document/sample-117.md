# #117 「Service を使った Component 間通信」

## 概要
Angular v20におけるInjectable Serviceを活用したコンポーネント間通信の実装方法。SignalやSubjectを使用してグローバルな状態管理を実現し、アプリケーション全体で一貫したデータ管理を行う。

## 学習目標
- Service を使った状態管理の基本を理解する
- Signal と Observable の使い分けを学ぶ
- グローバルな状態管理パターンを把握する

## 技術ポイント
- Injectable Service の実装
- Signal によるリアクティブな状態管理
- Subject を使ったイベント通信
- inject() による依存性注入

## 📺 画面表示用コード

### 状態管理 Service
```typescript
@Injectable({
  providedIn: 'root'
})
export class AppStateService {
  private _user = signal<User | null>(null);
  private _loading = signal(false);

  // Readonly signals
  user = this._user.asReadonly();
  loading = this._loading.asReadonly();

  // Actions
  setUser(user: User) {
    this._user.set(user);
  }

  setLoading(loading: boolean) {
    this._loading.set(loading);
  }

  logout() {
    this._user.set(null);
  }
}
```

### コンポーネントでの使用
```typescript
@Component({
  selector: 'app-header',
  template: `
    <div *ngIf="user(); else loginButton">
      Welcome, {{ user()?.name }}!
      <button (click)="logout()">ログアウト</button>
    </div>
    <ng-template #loginButton>
      <button (click)="login()">ログイン</button>
    </ng-template>
  `
})
export class HeaderComponent {
  private appState = inject(AppStateService);
  user = this.appState.user;

  login() {
    this.appState.setUser({ id: 1, name: 'John Doe' });
  }

  logout() {
    this.appState.logout();
  }
}
```

## 実践的な活用例
- ユーザー認証状態の管理
- ショッピングカートの状態管理
- アプリケーション設定の共有

## ベストプラクティス
- Service の責任範囲を明確にする
- Signal と Observable を適切に使い分ける
- 型安全性を保った実装を行う
- 単一責任の原則に従う

## 注意点
- 過度なグローバル状態を避ける
- メモリリークを防ぐため、適切なクリーンアップを行う
- 循環依存を避ける

## 関連技術
- Dependency Injection
- Signal
- RxJS Observable
- 状態管理パターン
