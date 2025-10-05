# #017 「Component のディレクトリ構成」台本

四国めたん「Component のディレクトリ構成について学びましょう！」
ずんだもん「ディレクトリ構成ってなぜ重要なの？」
四国めたん「プロジェクトの規模が大きくなっても、ファイルを見つけやすく管理しやすくします」
ずんだもん「どんな構成がおすすめなの？」
四国めたん「機能別、共有別、コア別に分けて整理するのが一般的です」
ずんだもん「命名規則はあるの？」
四国めたん「kebab-caseで統一し、意味のある名前を付けることが重要です」

---

## 📺 画面表示用コード

// 基本的なディレクトリ構成
```
src/app/
├── core/                    # コア機能
│   ├── services/
│   ├── guards/
│   ├── interceptors/
│   └── models/
├── shared/                  # 共有Component
│   ├── components/
│   ├── directives/
│   ├── pipes/
│   └── services/
├── features/                # 機能別Component
│   ├── user-management/
│   ├── product-catalog/
│   └── order-management/
└── app.component.ts
```

// 機能別ディレクトリ構成
```
src/app/features/user-management/
├── components/
│   ├── user-list/
│   │   ├── user-list.component.ts
│   │   ├── user-list.component.html
│   │   ├── user-list.component.css
│   │   └── user-list.component.spec.ts
│   ├── user-detail/
│   │   ├── user-detail.component.ts
│   │   ├── user-detail.component.html
│   │   ├── user-detail.component.css
│   │   └── user-detail.component.spec.ts
│   └── user-form/
│       ├── user-form.component.ts
│       ├── user-form.component.html
│       ├── user-form.component.css
│       └── user-form.component.spec.ts
├── services/
│   └── user.service.ts
├── models/
│   └── user.model.ts
└── user-management.module.ts
```

// 共有Componentの構成
```
src/app/shared/
├── components/
│   ├── button/
│   │   ├── button.component.ts
│   │   ├── button.component.html
│   │   ├── button.component.css
│   │   └── button.component.spec.ts
│   ├── card/
│   │   ├── card.component.ts
│   │   ├── card.component.html
│   │   ├── card.component.css
│   │   └── card.component.spec.ts
│   └── modal/
│       ├── modal.component.ts
│       ├── modal.component.html
│       ├── modal.component.css
│       └── modal.component.spec.ts
├── directives/
│   ├── highlight.directive.ts
│   └── tooltip.directive.ts
├── pipes/
│   ├── currency.pipe.ts
│   └── date.pipe.ts
└── services/
    ├── api.service.ts
    └── storage.service.ts
```

// インデックスファイルの活用
```typescript
// src/app/shared/components/index.ts
export { ButtonComponent } from './button/button.component';
export { CardComponent } from './card/card.component';
export { ModalComponent } from './modal/modal.component';

// src/app/shared/directives/index.ts
export { HighlightDirective } from './highlight.directive';
export { TooltipDirective } from './tooltip.directive';

// src/app/shared/pipes/index.ts
export { CurrencyPipe } from './currency.pipe';
export { DatePipe } from './date.pipe';

// src/app/shared/services/index.ts
export { ApiService } from './api.service';
export { StorageService } from './storage.service';

// メインのインデックスファイル
// src/app/shared/index.ts
export * from './components';
export * from './directives';
export * from './pipes';
export * from './services';
```

// インポートの簡略化
```typescript
// インデックスファイルを使用
import { 
  ButtonComponent, 
  CardComponent, 
  ModalComponent 
} from '../shared';

// 個別インポート（長い）
import { ButtonComponent } from '../shared/components/button/button.component';
import { CardComponent } from '../shared/components/card/card.component';
import { ModalComponent } from '../shared/components/modal/modal.component';
```

// 機能別モジュールの構成
```typescript
// src/app/features/user-management/user-management.module.ts
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { UserListComponent } from './components/user-list/user-list.component';
import { UserDetailComponent } from './components/user-detail/user-detail.component';
import { UserFormComponent } from './components/user-form/user-form.component';

@NgModule({
  declarations: [
    UserListComponent,
    UserDetailComponent,
    UserFormComponent
  ],
  imports: [
    CommonModule,
    FormsModule
  ],
  exports: [
    UserListComponent,
    UserDetailComponent,
    UserFormComponent
  ]
})
export class UserManagementModule { }
```

// 大規模プロジェクトの構成
```
src/app/
├── core/                    # アプリケーションのコア機能
│   ├── services/
│   │   ├── auth.service.ts
│   │   ├── api.service.ts
│   │   └── storage.service.ts
│   ├── guards/
│   │   ├── auth.guard.ts
│   │   └── role.guard.ts
│   ├── interceptors/
│   │   ├── auth.interceptor.ts
│   │   └── error.interceptor.ts
│   └── models/
│       ├── user.model.ts
│       └── api-response.model.ts
├── shared/                  # 共有リソース
│   ├── components/
│   │   ├── ui/              # UI Component
│   │   │   ├── button/
│   │   │   ├── input/
│   │   │   ├── modal/
│   │   │   └── table/
│   │   └── layout/          # レイアウトComponent
│   │       ├── header/
│   │       ├── footer/
│   │       └── sidebar/
│   ├── directives/
│   ├── pipes/
│   └── services/
├── features/                # 機能別モジュール
│   ├── authentication/
│   ├── user-management/
│   ├── product-catalog/
│   ├── shopping-cart/
│   └── order-management/
└── app.component.ts
```

// 命名規則の例
```
src/app/
├── user-management/         ✅ kebab-case
├── product-catalog/         ✅ kebab-case
├── shopping-cart/           ✅ kebab-case
├── order-management/        ✅ kebab-case

// ❌ 避けるべき命名
├── UserManagement/          ❌ PascalCase
├── userManagement/          ❌ camelCase
├── user_management/         ❌ snake_case
├── usermanagement/          ❌ 区切りなし
```

// ファイル命名の例
```
user-list/
├── user-list.component.ts      ✅ kebab-case
├── user-list.component.html    ✅ kebab-case
├── user-list.component.css     ✅ kebab-case
├── user-list.component.spec.ts ✅ kebab-case

// ❌ 避けるべき命名
├── UserList.component.ts       ❌ PascalCase
├── userList.component.ts       ❌ camelCase
├── user_list.component.ts      ❌ snake_case
```

// ディレクトリ構成のベストプラクティス
```typescript
@Component({
  selector: 'app-best-practices',
  template: `
    <div>
      <h2>ディレクトリ構成のベストプラクティス</h2>
      <ul>
        <li>機能別にディレクトリを分ける</li>
        <li>kebab-caseで命名を統一</li>
        <li>インデックスファイルを活用</li>
        <li>関連ファイルを同じディレクトリに配置</li>
        <li>共有リソースはsharedディレクトリに</li>
        <li>コア機能はcoreディレクトリに</li>
        <li>意味のある名前を付ける</li>
        <li>階層を深くしすぎない</li>
      </ul>
    </div>
  `
})
export class BestPracticesComponent {
  // プロジェクトの規模に応じて構成を調整
}
```
