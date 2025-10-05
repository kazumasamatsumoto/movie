# #077 ngOnInit での API 呼び出し

## 概要
Angular v20におけるngOnInitでのAPI呼び出しを学びます。適切なタイミングでのデータ取得とエラーハンドリング、パフォーマンス最適化の方法について解説します。

## 学習目標
- ngOnInitでのAPI呼び出しの基本を理解する
- 適切なエラーハンドリング方法を習得する
- パフォーマンスを考慮した実装方法を身につける

## 📺 画面表示用コード

```typescript
// ngOnInitでのAPI呼び出し
export class ApiCallComponent implements OnInit, OnDestroy {
  data: any[] = [];
  loading = false;
  error: string | null = null;
  private subscription = new Subscription();
  
  ngOnInit() {
    this.loadData();
  }
  
  ngOnDestroy() {
    this.subscription.unsubscribe();
  }
  
  private loadData() {
    this.loading = true;
    this.error = null;
    
    this.subscription.add(
      this.dataService.getData().subscribe({
        next: (data) => {
          this.data = data;
          this.loading = false;
        },
        error: (error) => {
          this.error = 'データの取得に失敗しました';
          this.loading = false;
        }
      })
    );
  }
}
```

```typescript
// async/awaitパターン
export class AsyncApiComponent implements OnInit {
  data: any[] = [];
  
  async ngOnInit() {
    try {
      this.data = await this.dataService.getData().toPromise();
    } catch (error) {
      console.error('API呼び出しエラー:', error);
    }
  }
}
```

## 技術ポイント

### 1. 基本的なAPI呼び出し
- 適切なタイミング（ngOnInit）
- エラーハンドリング
- ローディング状態の管理
- 購読の管理

### 2. エラーハンドリング
- try-catch文の使用
- Observableのerrorハンドラー
- ユーザーフレンドリーなエラーメッセージ
- リトライ機能

### 3. パフォーマンス最適化
- 適切な購読管理
- キャッシュの活用
- 重複リクエストの防止
- 遅延読み込み

## 実践的な活用例

### 1. 複数API呼び出し
```typescript
export class MultipleApiComponent implements OnInit, OnDestroy {
  users: User[] = [];
  posts: Post[] = [];
  loading = { users: false, posts: false };
  private subscription = new Subscription();
  
  ngOnInit() {
    this.loadUsers();
    this.loadPosts();
  }
  
  ngOnDestroy() {
    this.subscription.unsubscribe();
  }
  
  private loadUsers() {
    this.loading.users = true;
    this.subscription.add(
      this.userService.getUsers().subscribe({
        next: (users) => {
          this.users = users;
          this.loading.users = false;
        },
        error: (error) => {
          this.loading.users = false;
          console.error('ユーザー取得エラー:', error);
        }
      })
    );
  }
  
  private loadPosts() {
    this.loading.posts = true;
    this.subscription.add(
      this.postService.getPosts().subscribe({
        next: (posts) => {
          this.posts = posts;
          this.loading.posts = false;
        },
        error: (error) => {
          this.loading.posts = false;
          console.error('投稿取得エラー:', error);
        }
      })
    );
  }
}
```

### 2. 条件付きAPI呼び出し
```typescript
export class ConditionalApiComponent implements OnInit {
  @Input() userId?: string;
  user?: User;
  
  ngOnInit() {
    if (this.userId) {
      this.loadUser(this.userId);
    }
  }
  
  private loadUser(id: string) {
    this.userService.getUser(id).subscribe(user => {
      this.user = user;
    });
  }
}
```

### 3. キャッシュ付きAPI呼び出し
```typescript
export class CachedApiComponent implements OnInit {
  data: any[] = [];
  private cache: any[] | null = null;
  
  ngOnInit() {
    if (this.cache) {
      this.data = this.cache;
    } else {
      this.loadData();
    }
  }
  
  private loadData() {
    this.dataService.getData().subscribe(data => {
      this.data = data;
      this.cache = data;
    });
  }
}
```

## ベストプラクティス

1. **適切なエラーハンドリング**: ユーザーフレンドリーなエラー処理
2. **購読管理**: 適切な購読の解除
3. **ローディング状態**: ユーザーエクスペリエンスの向上
4. **パフォーマンス**: キャッシュと重複リクエストの防止

## 注意点

- 適切な購読管理
- エラーハンドリングの実装
- パフォーマンスへの影響を考慮
- メモリリークの防止

## 関連技術
- HTTP クライアント
- Observable
- エラーハンドリング
- パフォーマンス最適化
