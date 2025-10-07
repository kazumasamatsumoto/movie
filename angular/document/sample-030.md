# #030 「Component 設計の基本原則」

## 概要
高品質なComponentを設計するための基本原則を学びます。

## 学習目標
- SOLID原則を理解する
- Angular特有の設計パターンを習得する
- 保守性の高い設計手法を学ぶ

## 技術ポイント
- **単一責任**: 1つのComponentは1つの役割
- **疎結合**: Input/Outputで通信
- **高凝集**: 関連する機能をまとめる

## 📺 画面表示用コード（動画用）

```typescript
// 単一責任の原則
@Component({
  selector: 'app-user-card',
  template: `<div>{{user.name}}</div>`
})
export class UserCardComponent {
  @Input() user!: User;  // 表示のみ
}
```

```typescript
// 疎結合: Input/Outputで通信
@Component({
  selector: 'app-user-list',
  template: `
    <app-user-card
      [user]="user"
      (selected)="onSelect($event)"
    ></app-user-card>
  `
})
export class UserListComponent {
  onSelect(user: User) { /* ... */ }
}
```

```typescript
// ロジックはサービスに分離
@Injectable()
export class UserService {
  getUsers() { /* ... */ }
  updateUser() { /* ... */ }
}

@Component({
  template: `...`
})
export class UserComponent {
  constructor(private userService: UserService) {}
}
```

## SOLID原則の適用

1. **S**: 単一責任 - 1つの役割に集中
2. **O**: 開放閉鎖 - 拡張に開き、修正に閉じる
3. **L**: リスコフ置換 - 継承の適切な使用
4. **I**: インターフェース分離 - 小さなインターフェース
5. **D**: 依存性逆転 - 抽象に依存

## Angular特有のパターン

- Presentational/Container分離
- Smart/Dumb Component
- OnPush変更検知戦略

## 注意点

- 原則に固執しすぎない
- 実用性とのバランス
- チームで共有

## 関連技術
- SOLID Principles
- Design Patterns
- Software Architecture
- Best Practices
