# #077 「ngOnInit での API 呼び出し」

## 概要
`ngOnInit`で初回レンダリングに必要なAPI呼び出しを行い、ローディング状態やエラーハンドリングを整理する手法を紹介します。

## 学習目標
- 初回APIフェッチを`ngOnInit`で実行する流れを理解する
- ローディング／エラー状態をSignalで管理する
- `HttpClient`やfetchの非同期処理を安全に扱う

## 技術ポイント
- **初期データ取得**: `ngOnInit`でサービスを呼び出し、結果を状態に格納
- **ローディング管理**: SignalやRxJSで状態遷移を明示
- **エラーハンドリング**: try/catchや`catchError`でユーザー通知

## 📺 画面表示用コード（動画用）
**表示ルール**: 最大3個、各10行以内、動画で見せる部分のみ

```typescript
ngOnInit(): void {
  this.fetchUsers();
}
```

```typescript
async fetchUsers() {
  this.loading.set(true);
}
```

```typescript
this.users.set(await this.api.getUsers());
```

## 💻 詳細実装例（学習用）
```typescript
import { Component, OnInit, computed, signal } from '@angular/core';
import { HttpClient, provideHttpClient } from '@angular/common/http';
import { catchError, firstValueFrom, of } from 'rxjs';

type User = { id: number; name: string };

@Component({
  selector: 'app-user-list',
  standalone: true,
  templateUrl: './user-list.component.html',
  providers: [provideHttpClient()],
})
export class UserListComponent implements OnInit {
  private readonly http = inject(HttpClient);
  readonly users = signal<User[]>([]);
  readonly loading = signal(false);
  readonly error = signal<string | null>(null);
  readonly count = computed(() => this.users().length);

  ngOnInit(): void {
    void this.fetchUsers();
  }

  private async fetchUsers(): Promise<void> {
    this.loading.set(true);
    this.error.set(null);
    try {
      const response = await firstValueFrom(
        this.http
          .get<User[]>('/api/users')
          .pipe(catchError(() => of([]))),
      );
      this.users.set(response);
    } catch (err) {
      this.error.set('ユーザー取得に失敗しました');
    } finally {
      this.loading.set(false);
    }
  }
}
```

```html
<section *ngIf="loading()">読み込み中...</section>
<section *ngIf="error()">{{ error() }}</section>
<ul>
  <li @for (user of users(); track user.id)>{{ user.name }}</li>
</ul>
<p>総数: {{ count() }}</p>
```

## ベストプラクティス
- `void this.fetchUsers()`のように呼び出し側で未処理Promiseを意図的に無視する
- API呼び出しはサービス層に移し、UIコンポーネントでは状態の管理に専念する
- エラー発生時はユーザーメッセージとログ出力の双方を検討する

## 注意点
- `ngOnInit`で同期的に重い処理を行うと初期描画が遅延する
- 再読込が必要な場合はボタンなどで別メソッドから再利用できるようにする
- SSR環境では`window.fetch`やブラウザ依存APIが使えないため`HttpClient`を優先する

## 関連技術
- Angular `HttpClient`と`provideHttpClient`
- Signalsによる状態管理
- Router Resolverとの比較（ルート解決時にデータ取得）
