# #284 "Examples of Using null"

Shikoku Metan: "Let's look at practical examples of using null!"
Zundamon: "The findUser function returns null when a user is not found!"
Shikoku Metan: "That's right. We use the ?? operator to convert undefined to null."
Zundamon: "The CacheService class uses null for cache management!"
Shikoku Metan: "Exactly. We represent initial state or invalid state with null."
Zundamon: "API responses also use data: T | null!"
Shikoku Metan: "Yes. On success, we return data; on failure, we return null and an error message."
Zundamon: "We can also use it in Angular services to manage currentUser!"

---

## 📺 Code for Display

```typescript
// Data retrieval and cache management
function findUser(id: number): User | null {
  return users.find(u => u.id === id) ?? null;
}
class CacheService {
  private cache: Map<string, any> | null = null;
}
```

```typescript
// API response
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
