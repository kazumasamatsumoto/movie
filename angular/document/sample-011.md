# #011 「Component のファイル構成」台本

四国めたん「Component のファイル構成について学びましょう！」
ずんだもん「Componentにはどんなファイルが必要なの？」
四国めたん「TypeScriptファイル、HTMLテンプレート、CSSスタイル、テストファイルの4つが基本です」
ずんだもん「ファイル名の規則はあるの？」
四国めたん「Component名.component.拡張子の形式で統一します」
ずんだもん「フォルダ構成はどうするの？」
四国めたん「Componentごとにフォルダを作成し、関連ファイルをまとめて管理します」

---

## 📺 画面表示用コード

// 基本的なファイル構成
```
src/app/user-profile/
├── user-profile.component.ts      # Componentクラス
├── user-profile.component.html    # テンプレート
├── user-profile.component.css     # スタイル
└── user-profile.component.spec.ts # テストファイル
```

// Componentクラスファイル
```typescript
// user-profile.component.ts
import { Component } from '@angular/core';

@Component({
  selector: 'app-user-profile',
  templateUrl: './user-profile.component.html',
  styleUrls: ['./user-profile.component.css']
})
export class UserProfileComponent {
  user = {
    name: '田中太郎',
    email: 'tanaka@example.com',
    avatar: '/assets/avatar.jpg'
  };
}
```

// HTMLテンプレートファイル
```html
<!-- user-profile.component.html -->
<div class="user-profile">
  <div class="avatar">
    <img [src]="user.avatar" [alt]="user.name">
  </div>
  <div class="info">
    <h2>{{user.name}}</h2>
    <p>{{user.email}}</p>
  </div>
</div>
```

// CSSスタイルファイル
```css
/* user-profile.component.css */
.user-profile {
  display: flex;
  align-items: center;
  padding: 20px;
  background-color: #f8f9fa;
  border-radius: 8px;
}

.avatar img {
  width: 60px;
  height: 60px;
  border-radius: 50%;
  margin-right: 16px;
}

.info h2 {
  margin: 0 0 8px 0;
  color: #333;
}

.info p {
  margin: 0;
  color: #666;
}
```

// テストファイル
```typescript
// user-profile.component.spec.ts
import { ComponentFixture, TestBed } from '@angular/core/testing';
import { UserProfileComponent } from './user-profile.component';

describe('UserProfileComponent', () => {
  let component: UserProfileComponent;
  let fixture: ComponentFixture<UserProfileComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [UserProfileComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(UserProfileComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
```

// 複雑なComponentのファイル構成
```
src/app/product-detail/
├── product-detail.component.ts
├── product-detail.component.html
├── product-detail.component.css
├── product-detail.component.spec.ts
├── product-detail.service.ts        # 関連サービス
├── product-detail.interface.ts      # 型定義
└── product-detail.module.ts         # 機能モジュール
```

// 関連ファイルの例
```typescript
// product-detail.interface.ts
export interface Product {
  id: number;
  name: string;
  price: number;
  description: string;
  images: string[];
}

export interface ProductReview {
  id: number;
  userId: number;
  rating: number;
  comment: string;
  createdAt: Date;
}
```

// サービスファイル
```typescript
// product-detail.service.ts
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Product } from './product-detail.interface';

@Injectable({
  providedIn: 'root'
})
export class ProductDetailService {
  constructor(private http: HttpClient) {}
  
  getProduct(id: number): Observable<Product> {
    return this.http.get<Product>(`/api/products/${id}`);
  }
}
```

// ファイル命名規則
```typescript
// ✅ 推奨される命名
user-profile.component.ts
user-profile.component.html
user-profile.component.css
user-profile.component.spec.ts

// ❌ 避けるべき命名
UserProfile.component.ts
userProfile.component.ts
user_profile.component.ts
userprofile.component.ts
```

// フォルダ構成のベストプラクティス
```
src/app/
├── shared/                    # 共有Component
│   ├── header/
│   ├── footer/
│   └── button/
├── features/                  # 機能別Component
│   ├── user-management/
│   │   ├── user-list/
│   │   ├── user-detail/
│   │   └── user-form/
│   └── product-catalog/
│       ├── product-list/
│       ├── product-detail/
│       └── product-form/
└── core/                      # コア機能
    ├── services/
    ├── guards/
    └── interceptors/
```

// インデックスファイルの活用
```typescript
// user-management/index.ts
export { UserListComponent } from './user-list/user-list.component';
export { UserDetailComponent } from './user-detail/user-detail.component';
export { UserFormComponent } from './user-form/user-form.component';
export { UserManagementModule } from './user-management.module';
```

// インポートの簡略化
```typescript
// インデックスファイルを使用
import { 
  UserListComponent, 
  UserDetailComponent, 
  UserFormComponent 
} from './user-management';

// 個別インポート（長い）
import { UserListComponent } from './user-management/user-list/user-list.component';
import { UserDetailComponent } from './user-management/user-detail/user-detail.component';
import { UserFormComponent } from './user-management/user-form/user-form.component';
```
