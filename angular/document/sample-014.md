# #014 「Standalone vs Module-based 比較」台本

四国めたん「Standalone vs Module-based 比較について解説します！」
ずんだもん「どっちを使うべきなの？」
四国めたん「用途に応じて使い分けます。新規開発はStandalone、既存プロジェクトは段階的移行がおすすめです」
ずんだもん「具体的な違いは？」
四国めたん「NgModuleの必要性、依存関係の管理、バンドルサイズなどが異なります」
ずんだもん「移行は簡単なの？」
四国めたん「既存のComponentにstandalone: trueを追加するだけで移行できます」

---

## 📺 画面表示用コード

// Module-based Component（従来の方法）
```typescript
// user.component.ts
@Component({
  selector: 'app-user',
  template: `
    <div>
      <h2>{{user.name}}</h2>
      <p>{{user.email}}</p>
    </div>
  `
})
export class UserComponent {
  user = { name: '田中太郎', email: 'tanaka@example.com' };
}

// user.module.ts
@NgModule({
  declarations: [UserComponent],
  imports: [CommonModule],
  exports: [UserComponent]
})
export class UserModule { }
```

// Standalone Component（新しい方法）
```typescript
// user.component.ts
import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-user',
  standalone: true,
  imports: [CommonModule],
  template: `
    <div>
      <h2>{{user.name}}</h2>
      <p>{{user.email}}</p>
    </div>
  `
})
export class UserComponent {
  user = { name: '田中太郎', email: 'tanaka@example.com' };
}
```

// 依存関係の管理比較
```typescript
// Module-based: モジュールレベルで管理
@NgModule({
  declarations: [UserListComponent, UserDetailComponent],
  imports: [
    CommonModule,
    FormsModule,
    RouterModule
  ],
  exports: [UserListComponent, UserDetailComponent]
})
export class UserModule { }

// Standalone: Componentレベルで管理
@Component({
  selector: 'app-user-list',
  standalone: true,
  imports: [CommonModule, FormsModule],
  template: '<div>ユーザー一覧</div>'
})
export class UserListComponent { }

@Component({
  selector: 'app-user-detail',
  standalone: true,
  imports: [CommonModule, RouterModule],
  template: '<div>ユーザー詳細</div>'
})
export class UserDetailComponent { }
```

// 遅延ロードの比較
```typescript
// Module-based: モジュール全体をロード
const moduleRoutes: Routes = [
  {
    path: 'users',
    loadChildren: () => import('./user/user.module')
      .then(m => m.UserModule)
  }
];

// Standalone: 必要なComponentのみロード
const standaloneRoutes: Routes = [
  {
    path: 'users',
    loadComponent: () => import('./user/user.component')
      .then(m => m.UserComponent)
  }
];
```

// バンドルサイズの比較
```typescript
// Module-based: モジュール全体がバンドルに含まれる
@NgModule({
  declarations: [
    UserListComponent,    // 使用しない場合も含まれる
    UserDetailComponent,  // 使用しない場合も含まれる
    UserFormComponent     // 使用しない場合も含まれる
  ],
  imports: [
    CommonModule,         // 全体が含まれる
    FormsModule,          // 全体が含まれる
    RouterModule          // 全体が含まれる
  ]
})
export class UserModule { }

// Standalone: 必要なもののみバンドルに含まれる
@Component({
  selector: 'app-user-list',
  standalone: true,
  imports: [CommonModule], // 必要な部分のみ
  template: '<div>ユーザー一覧</div>'
})
export class UserListComponent { }
```

// 移行の例
```typescript
// 移行前（Module-based）
@Component({
  selector: 'app-legacy',
  template: '<div>レガシーComponent</div>'
})
export class LegacyComponent { }

// 移行後（Standalone）
@Component({
  selector: 'app-legacy',
  standalone: true,  // この行を追加するだけ
  template: '<div>レガシーComponent</div>'
})
export class LegacyComponent { }
```

// 段階的移行の例
```typescript
// 1. 既存のModule-based Component
@Component({
  selector: 'app-existing',
  template: '<div>既存Component</div>'
})
export class ExistingComponent { }

// 2. 新しいStandalone Component
@Component({
  selector: 'app-new',
  standalone: true,
  imports: [ExistingComponent], // 既存Componentをインポート
  template: '<app-existing></app-existing>'
})
export class NewComponent { }
```

// パフォーマンス比較
```typescript
// Module-based: 初期バンドルサイズが大きい
@NgModule({
  declarations: [LargeComponent],
  imports: [HeavyModule] // 重いモジュール全体が含まれる
})
export class LargeModule { }

// Standalone: 必要な部分のみ
@Component({
  selector: 'app-optimized',
  standalone: true,
  imports: [LightweightModule], // 軽量な部分のみ
  template: '<div>最適化されたComponent</div>'
})
export class OptimizedComponent { }
```

// 開発体験の比較
```typescript
// Module-based: 複数ファイルの管理が必要
// user.component.ts
@Component({
  selector: 'app-user',
  template: '<div>ユーザー</div>'
})
export class UserComponent { }

// user.module.ts
@NgModule({
  declarations: [UserComponent],
  imports: [CommonModule],
  exports: [UserComponent]
})
export class UserModule { }

// app.module.ts
@NgModule({
  imports: [UserModule], // モジュールをインポート
  declarations: [AppComponent]
})
export class AppModule { }

// Standalone: 単一ファイルで完結
@Component({
  selector: 'app-user',
  standalone: true,
  imports: [CommonModule],
  template: '<div>ユーザー</div>'
})
export class UserComponent { }

// app.component.ts
@Component({
  selector: 'app-root',
  standalone: true,
  imports: [UserComponent], // Componentを直接インポート
  template: '<app-user></app-user>'
})
export class AppComponent { }
```

// 使い分けの指針
```typescript
@Component({
  selector: 'app-guidelines',
  standalone: true,
  template: `
    <div>
      <h2>使い分けの指針</h2>
      <h3>Standalone Componentを使う場合:</h3>
      <ul>
        <li>新規開発</li>
        <li>シンプルなComponent</li>
        <li>マイクロフロントエンド</li>
        <li>パフォーマンス重視</li>
      </ul>
      <h3>Module-basedを使う場合:</h3>
      <ul>
        <li>既存の大規模プロジェクト</li>
        <li>複雑な依存関係</li>
        <li>段階的移行中</li>
      </ul>
    </div>
  `
})
export class GuidelinesComponent {
  // プロジェクトの要件に応じて選択
}
```
