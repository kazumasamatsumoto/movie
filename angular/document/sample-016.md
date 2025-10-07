# #016 「Component の export と再利用」

## 概要
Componentをexportすることで、アプリケーション全体で再利用できます。Standalone Componentは特にシンプルに再利用できます。

## 学習目標
- Componentのexport方法を理解する
- 他のComponentでのimport方法を習得する
- 再利用可能なComponentの設計を学ぶ

## 技術ポイント
- **export**: Componentを外部公開
- **import**: 他のComponentで使用
- **再利用性**: DRY原則の実践

## 📺 画面表示用コード（動画用）
**表示ルール**: 最大3個、各10行以内、動画で見せる部分のみ

```typescript
// Componentのexport
export class ButtonComponent {
  @Input() label = 'Click';
}

// 他のComponentでimport
import { ButtonComponent } from './button.component';

@Component({
  imports: [ButtonComponent]
})
export class AppComponent {}
```

```typescript
// 再利用可能なComponent作成
@Component({
  selector: 'app-card',
  standalone: true,
  template: `
    <div class="card">
      <ng-content></ng-content>
    </div>
  `
})
export class CardComponent {}
```

```typescript
// 複数の場所で使用
@Component({
  imports: [CardComponent],
  template: `
    <app-card>Card 1</app-card>
    <app-card>Card 2</app-card>
  `
})
export class DashboardComponent {}
```

## 💻 詳細実装例（学習用）

### 基本的なexportとimport

```typescript
// button.component.ts
import { Component, Input, Output, EventEmitter } from '@angular/core';

@Component({
  selector: 'app-button',
  standalone: true,
  template: `
    <button [class]="variant" (click)="handleClick()">
      {{label}}
    </button>
  `,
  styles: [`
    button {
      padding: 10px 20px;
      border: none;
      border-radius: 4px;
      cursor: pointer;
    }
    .primary { background: #007bff; color: white; }
    .secondary { background: #6c757d; color: white; }
  `]
})
export class ButtonComponent {  // export で公開
  @Input() label = 'Click me';
  @Input() variant: 'primary' | 'secondary' = 'primary';
  @Output() clicked = new EventEmitter<void>();

  handleClick() {
    this.clicked.emit();
  }
}

// app.component.ts
import { Component } from '@angular/core';
import { ButtonComponent } from './button.component';  // import

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [ButtonComponent],  // importsに追加
  template: `
    <app-button
      label="Save"
      variant="primary"
      (clicked)="onSave()"
    ></app-button>
    <app-button
      label="Cancel"
      variant="secondary"
      (clicked)="onCancel()"
    ></app-button>
  `
})
export class AppComponent {
  onSave() {
    console.log('Saved!');
  }

  onCancel() {
    console.log('Cancelled');
  }
}
```

### Barrel Exportsパターン

```typescript
// components/index.ts（Barrel export）
export { ButtonComponent } from './button.component';
export { CardComponent } from './card.component';
export { ModalComponent } from './modal.component';
export { AlertComponent } from './alert.component';

// app.component.ts
import {
  ButtonComponent,
  CardComponent,
  ModalComponent,
  AlertComponent
} from './components';  // 一括import

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [
    ButtonComponent,
    CardComponent,
    ModalComponent,
    AlertComponent
  ],
  template: `...`
})
export class AppComponent {}
```

### 共有Componentライブラリ

```typescript
// shared/components/ui/index.ts
export { ButtonComponent } from './button/button.component';
export { InputComponent } from './input/input.component';
export { SelectComponent } from './select/select.component';
export { CheckboxComponent } from './checkbox/checkbox.component';

// features/user/user-form.component.ts
import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import {
  ButtonComponent,
  InputComponent,
  SelectComponent,
  CheckboxComponent
} from '../../../shared/components/ui';

@Component({
  selector: 'app-user-form',
  standalone: true,
  imports: [
    FormsModule,
    ButtonComponent,
    InputComponent,
    SelectComponent,
    CheckboxComponent
  ],
  template: `
    <form>
      <app-input
        [(ngModel)]="user.name"
        label="Name"
      ></app-input>

      <app-select
        [(ngModel)]="user.role"
        [options]="roles"
        label="Role"
      ></app-select>

      <app-checkbox
        [(ngModel)]="user.active"
        label="Active"
      ></app-checkbox>

      <app-button
        label="Save"
        (clicked)="onSave()"
      ></app-button>
    </form>
  `
})
export class UserFormComponent {
  user = {
    name: '',
    role: '',
    active: false
  };

  roles = ['Admin', 'User', 'Guest'];

  onSave() {
    console.log('User:', this.user);
  }
}
```

### レイアウトComponentの再利用

```typescript
// layout/page-layout.component.ts
import { Component } from '@angular/core';
import { HeaderComponent } from './header.component';
import { FooterComponent } from './footer.component';
import { SidebarComponent } from './sidebar.component';

@Component({
  selector: 'app-page-layout',
  standalone: true,
  imports: [HeaderComponent, FooterComponent, SidebarComponent],
  template: `
    <div class="page-layout">
      <app-header></app-header>
      <div class="content-wrapper">
        <app-sidebar></app-sidebar>
        <main>
          <ng-content></ng-content>
        </main>
      </div>
      <app-footer></app-footer>
    </div>
  `,
  styles: [`
    .page-layout {
      display: flex;
      flex-direction: column;
      min-height: 100vh;
    }
    .content-wrapper {
      display: flex;
      flex: 1;
    }
    main {
      flex: 1;
      padding: 20px;
    }
  `]
})
export class PageLayoutComponent {}

// 複数のページで再利用
// home.component.ts
@Component({
  selector: 'app-home',
  standalone: true,
  imports: [PageLayoutComponent],
  template: `
    <app-page-layout>
      <h1>Home Page</h1>
      <p>Welcome to our application</p>
    </app-page-layout>
  `
})
export class HomeComponent {}

// about.component.ts
@Component({
  selector: 'app-about',
  standalone: true,
  imports: [PageLayoutComponent],
  template: `
    <app-page-layout>
      <h1>About Page</h1>
      <p>About our company</p>
    </app-page-layout>
  `
})
export class AboutComponent {}
```

### プロジェクト間での再利用（ライブラリ化）

```bash
# ライブラリを作成
ng generate library ui-components

# projects/ui-components/src/lib/
```

```typescript
// projects/ui-components/src/lib/button/button.component.ts
import { Component, Input, Output, EventEmitter } from '@angular/core';

@Component({
  selector: 'lib-button',  // ライブラリ用プレフィックス
  standalone: true,
  template: `
    <button [class]="variant" (click)="onClick()">
      {{label}}
    </button>
  `,
  styles: [`...`]
})
export class ButtonComponent {
  @Input() label = 'Click';
  @Input() variant = 'primary';
  @Output() clicked = new EventEmitter<void>();

  onClick() {
    this.clicked.emit();
  }
}

// projects/ui-components/src/public-api.ts
export { ButtonComponent } from './lib/button/button.component';
export { CardComponent } from './lib/card/card.component';
export { ModalComponent } from './lib/modal/modal.component';

// アプリケーションで使用
// app.component.ts
import { Component } from '@angular/core';
import { ButtonComponent, CardComponent } from 'ui-components';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [ButtonComponent, CardComponent],
  template: `
    <lib-button label="Click" (clicked)="handleClick()"></lib-button>
  `
})
export class AppComponent {
  handleClick() {
    console.log('Clicked!');
  }
}
```

### Componentの合成パターン

```typescript
// list-item.component.ts
@Component({
  selector: 'app-list-item',
  standalone: true,
  template: `
    <div class="list-item">
      <ng-content select="[slot=icon]"></ng-content>
      <div class="content">
        <ng-content select="[slot=title]"></ng-content>
        <ng-content select="[slot=description]"></ng-content>
      </div>
      <ng-content select="[slot=actions]"></ng-content>
    </div>
  `
})
export class ListItemComponent {}

// list.component.ts
@Component({
  selector: 'app-list',
  standalone: true,
  imports: [CommonModule, ListItemComponent],
  template: `
    <div class="list">
      <ng-content></ng-content>
    </div>
  `
})
export class ListComponent {}

// 使用例
@Component({
  selector: 'app-user-list',
  standalone: true,
  imports: [ListComponent, ListItemComponent, CommonModule],
  template: `
    <app-list>
      <app-list-item *ngFor="let user of users">
        <span slot="icon">👤</span>
        <h3 slot="title">{{user.name}}</h3>
        <p slot="description">{{user.email}}</p>
        <button slot="actions" (click)="editUser(user)">Edit</button>
      </app-list-item>
    </app-list>
  `
})
export class UserListComponent {
  users = [
    { id: 1, name: 'John', email: 'john@example.com' },
    { id: 2, name: 'Jane', email: 'jane@example.com' }
  ];

  editUser(user: any) {
    console.log('Edit:', user);
  }
}
```

### Higher-Order Component パターン

```typescript
// with-loading.component.ts
import { Component, Input } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-with-loading',
  standalone: true,
  imports: [CommonModule],
  template: `
    @if (loading) {
      <div class="loading-spinner">Loading...</div>
    } @else {
      <ng-content></ng-content>
    }
  `
})
export class WithLoadingComponent {
  @Input() loading = false;
}

// 使用例
@Component({
  selector: 'app-user-data',
  standalone: true,
  imports: [WithLoadingComponent, CommonModule],
  template: `
    <app-with-loading [loading]="isLoading">
      <ul>
        <li *ngFor="let user of users">{{user.name}}</li>
      </ul>
    </app-with-loading>
  `
})
export class UserDataComponent {
  isLoading = true;
  users: any[] = [];

  ngOnInit() {
    // データ取得
    setTimeout(() => {
      this.users = [{ name: 'John' }, { name: 'Jane' }];
      this.isLoading = false;
    }, 1000);
  }
}
```

### Dynamic Componentの再利用

```typescript
// dynamic-component-loader.component.ts
import {
  Component,
  ViewContainerRef,
  ComponentRef,
  Type
} from '@angular/core';

@Component({
  selector: 'app-dynamic-loader',
  standalone: true,
  template: `<ng-container #container></ng-container>`
})
export class DynamicLoaderComponent {
  constructor(private viewContainer: ViewContainerRef) {}

  loadComponent<T>(component: Type<T>): ComponentRef<T> {
    this.viewContainer.clear();
    return this.viewContainer.createComponent(component);
  }

  clearComponent() {
    this.viewContainer.clear();
  }
}

// 使用例
@Component({
  selector: 'app-dashboard',
  standalone: true,
  imports: [DynamicLoaderComponent],
  template: `
    <button (click)="loadUserComponent()">Load Users</button>
    <button (click)="loadProductComponent()">Load Products</button>
    <app-dynamic-loader></app-dynamic-loader>
  `
})
export class DashboardComponent {
  @ViewChild(DynamicLoaderComponent)
  loader!: DynamicLoaderComponent;

  async loadUserComponent() {
    const { UserListComponent } = await import('./user-list.component');
    this.loader.loadComponent(UserListComponent);
  }

  async loadProductComponent() {
    const { ProductListComponent } = await import('./product-list.component');
    this.loader.loadComponent(ProductListComponent);
  }
}
```

## ベストプラクティス

1. **Standalone Componentを使用**: シンプルな再利用
2. **Barrel Exportsの活用**: importを整理
3. **明確なAPI設計**: @Input/@Outputを適切に定義
4. **ドキュメント化**: 使用方法を文書化

## 注意点

- exportを忘れるとimportできない
- 循環参照を避ける
- 適切なカプセル化を維持
- パブリックAPIのみを公開

## 関連技術
- Module System
- Barrel Exports
- Component Composition
- Library Development
