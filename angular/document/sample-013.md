# #013 「Standalone Component - standalone: true」台本

四国めたん「Standalone Component - standalone: trueについて学びましょう！」
ずんだもん「Standalone Componentって何？」
四国めたん「NgModuleに依存せず、独立して動作するComponentです」
ずんだもん「従来のComponentと何が違うの？」
四国めたん「NgModuleの宣言が不要で、必要な依存関係を直接インポートできます」
ずんだもん「どんなメリットがあるの？」
四国めたん「シンプルな構成、遅延ロードの改善、マイクロフロントエンド対応が可能です」

---

## 📺 画面表示用コード

// 基本的なStandalone Component
```typescript
import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-standalone',
  standalone: true,
  imports: [CommonModule],
  template: `
    <div>
      <h1>{{title}}</h1>
      <p *ngIf="isVisible">表示中</p>
      <button (click)="toggle()">切り替え</button>
    </div>
  `
})
export class StandaloneComponent {
  title = 'Standalone Component';
  isVisible = true;
  
  toggle() {
    this.isVisible = !this.isVisible;
  }
}
```

// 従来のComponent（NgModule必要）
```typescript
// ❌ 従来の方法
@Component({
  selector: 'app-traditional',
  template: '<div>従来のComponent</div>'
})
export class TraditionalComponent {
  // NgModuleで宣言が必要
}

// 対応するNgModule
@NgModule({
  declarations: [TraditionalComponent],
  exports: [TraditionalComponent]
})
export class TraditionalModule { }
```

// Standalone Component（NgModule不要）
```typescript
// ✅ Standalone Component
@Component({
  selector: 'app-standalone-simple',
  standalone: true,
  template: '<div>Standalone Component</div>'
})
export class StandaloneSimpleComponent {
  // NgModuleの宣言が不要
}
```

// 複数の依存関係をインポート
```typescript
import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { RouterModule } from '@angular/router';

@Component({
  selector: 'app-standalone-complex',
  standalone: true,
  imports: [
    CommonModule,
    FormsModule,
    RouterModule
  ],
  template: `
    <div>
      <h2>複雑なStandalone Component</h2>
      <form>
        <input [(ngModel)]="name" placeholder="名前">
        <button type="submit">送信</button>
      </form>
      <a routerLink="/home">ホーム</a>
    </div>
  `
})
export class StandaloneComplexComponent {
  name = '';
}
```

// 他のStandalone Componentをインポート
```typescript
import { Component } from '@angular/core';
import { HeaderComponent } from './header/header.component';
import { FooterComponent } from './footer/footer.component';

@Component({
  selector: 'app-layout',
  standalone: true,
  imports: [HeaderComponent, FooterComponent],
  template: `
    <div class="layout">
      <app-header></app-header>
      <main>
        <h1>メインコンテンツ</h1>
      </main>
      <app-footer></app-footer>
    </div>
  `
})
export class LayoutComponent {
  // 他のStandalone Componentを組み合わせ
}
```

// 遅延ロードでの使用
```typescript
// ルーティング設定
const routes: Routes = [
  {
    path: 'standalone',
    loadComponent: () => import('./standalone/standalone.component')
      .then(m => m.StandaloneComponent)
  }
];

// 従来の方法（NgModule必要）
const traditionalRoutes: Routes = [
  {
    path: 'traditional',
    loadChildren: () => import('./traditional/traditional.module')
      .then(m => m.TraditionalModule)
  }
];
```

// マイクロフロントエンドでの使用
```typescript
import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-micro-frontend',
  standalone: true,
  imports: [CommonModule],
  template: `
    <div class="micro-frontend">
      <h3>マイクロフロントエンド</h3>
      <p>独立したアプリケーションとして動作</p>
    </div>
  `,
  styles: [`
    .micro-frontend {
      border: 2px solid #007bff;
      padding: 20px;
      margin: 10px;
    }
  `]
})
export class MicroFrontendComponent {
  // 他のアプリケーションから独立して動作
}
```

// サービス注入
```typescript
import { Component, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { UserService } from './user.service';

@Component({
  selector: 'app-standalone-service',
  standalone: true,
  imports: [CommonModule],
  template: `
    <div>
      <h2>ユーザー情報</h2>
      <p *ngIf="user">{{user.name}}</p>
    </div>
  `
})
export class StandaloneServiceComponent {
  private userService = inject(UserService);
  user: any = null;
  
  ngOnInit() {
    this.user = this.userService.getCurrentUser();
  }
}
```

// Standalone Componentの利点
```typescript
@Component({
  selector: 'app-benefits',
  standalone: true,
  template: `
    <div>
      <h2>Standalone Componentの利点</h2>
      <ul>
        <li>NgModuleの宣言が不要</li>
        <li>必要な依存関係のみインポート</li>
        <li>遅延ロードが簡単</li>
        <li>マイクロフロントエンド対応</li>
        <li>バンドルサイズの最適化</li>
        <li>開発体験の向上</li>
      </ul>
    </div>
  `
})
export class BenefitsComponent {
  // Angular v14+の新機能
}
```
