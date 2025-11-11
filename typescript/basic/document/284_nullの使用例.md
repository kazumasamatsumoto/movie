# #284 「nullの使用例」

四国めたん「nullの実践的な使用例を見ていきましょう!」
ずんだもん「findUser関数でユーザーが見つからない時にnullを返すんだね!」
四国めたん「はい。??演算子を使ってundefinedをnullに変換しています。」
ずんだもん「CacheServiceクラスでキャッシュ管理にnullを使っているのだ!」
四国めたん「その通りです。初期状態や無効な状態をnullで表現します。」
ずんだもん「APIレスポンスでもdata: T | nullを使うんだね!」
四国めたん「はい。成功時はデータ、失敗時はnullとerrorメッセージを返します。」
ずんだもん「AngularのサービスでもcurrentUserの管理に使えるのだ!」

---

## 📺 画面表示用コード

```typescript
// データ検索とキャッシュ管理
function findUser(id: number): User | null {
  return users.find(u => u.id === id) ?? null;
}
class CacheService {
  private cache: Map<string, any> | null = null;
}
```

```typescript
// APIレスポンス
interface ApiResponse<T> {
  data: T | null;
  error: string | null;
}
```

```typescript
// Angular DI
@Injectable()
class UserService {
  private currentUser: User | null = null;
  setUser(user: User | null): void {
    this.currentUser = user;
  }
}
```
