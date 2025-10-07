# #018 「Component のベストプラクティス」

## 概要
高品質なComponentを作成するためのベストプラクティスを学びます。保守性、パフォーマンス、可読性を向上させる方法を理解します。

## 学習目標
- Component設計の原則を理解する
- パフォーマンス最適化手法を習得する
- 保守しやすいコードの書き方を学ぶ

## 技術ポイント
- **単一責任の原則**: 1つの役割に集中
- **OnPush変更検知**: パフォーマンス向上
- **型安全性**: TypeScriptの活用

## 📺 画面表示用コード（動画用）
**表示ルール**: 最大3個、各10行以内、動画で見せる部分のみ

```typescript
// 単一責任の原則
@Component({
  selector: 'app-user-card',
  standalone: true,
  template: `<div>{{user.name}}</div>`
})
export class UserCardComponent {
  @Input() user!: User;  // 1つの責任
}
```

```typescript
// OnPush変更検知
@Component({
  selector: 'app-product-list',
  standalone: true,
  changeDetection: ChangeDetectionStrategy.OnPush,
  template: `...`
})
export class ProductListComponent {}
```

```typescript
// 型安全性
interface User {
  id: number;
  name: string;
}

@Component({
  template: `<p>{{user.name}}</p>`
})
export class UserComponent {
  @Input() user!: User;  // 型定義
}
```

## 💻 詳細実装例（学習用）

### 1. 単一責任の原則
```typescript
// ❌ 悪い例: 複数の責任
@Component({
  selector: 'app-dashboard',
  template: `
    <!-- ユーザー管理 -->
    <!-- 商品管理 -->
    <!-- 注文管理 -->
  `
})
export class DashboardComponent {
  // すべての機能が1つのComponentに...
}

// ✅ 良い例: 分割
@Component({
  selector: 'app-dashboard',
  standalone: true,
  imports: [
    UserManagementComponent,
    ProductManagementComponent,
    OrderManagementComponent
  ],
  template: `
    <app-user-management />
    <app-product-management />
    <app-order-management />
  `
})
export class DashboardComponent {}
```

### 2. OnPush変更検知戦略
```typescript
import { ChangeDetectionStrategy } from '@angular/core';

@Component({
  selector: 'app-optimized-list',
  standalone: true,
  changeDetection: ChangeDetectionStrategy.OnPush,
  template: `
    <div *ngFor="let item of items; trackBy: trackById">
      {{item.name}}
    </div>
  `
})
export class OptimizedListComponent {
  @Input() items: Item[] = [];

  trackById(index: number, item: Item) {
    return item.id;
  }
}
```

### 3. Immutabilityの実践
```typescript
@Component({
  selector: 'app-user-list',
  standalone: true,
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class UserListComponent {
  @Input() users: readonly User[] = [];
  @Output() userUpdated = new EventEmitter<User>();

  updateUser(user: User, name: string) {
    // 不変性を維持
    const updatedUser = { ...user, name };
    this.userUpdated.emit(updatedUser);
  }
}
```

## ベストプラクティス一覧

1. **小さく保つ**: テンプレート100行以内
2. **OnPushを使用**: パフォーマンス向上
3. **型安全**: すべてに型定義
4. **DRY原則**: コードの重複を避ける
5. **適切な命名**: 明確で一貫した名前
6. **ドキュメント**: コメントで意図を明示

## 注意点

- 過度な最適化は避ける
- 可読性を優先
- テストを書く
- Angular Style Guideに従う

## 関連技術
- Change Detection
- Performance Optimization
- Code Quality
- Design Patterns
