# #006 「templateUrl - 外部テンプレートファイル」

## 概要
templateUrlを使用すると、HTMLを別ファイルに分離できます。大規模なComponentで可読性と保守性が向上します。

## 学習目標
- templateUrlの使い方を習得する
- templateとの使い分けを理解する
- 相対パス指定の方法を学ぶ

## 技術ポイント
- **templateUrl**: 外部HTMLファイル参照
- **相対パス**: ./から始まるパス指定
- **エディタサポート**: HTMLの補完・シンタックスハイライト

## 📺 画面表示用コード（動画用）
**表示ルール**: 最大3個、各10行以内、動画で見せる部分のみ

```typescript
// templateUrlの基本
@Component({
  selector: 'app-user',
  templateUrl: './user.component.html',
  styleUrls: ['./user.component.css']
})
export class UserComponent {}
```

```html
<!-- user.component.html -->
<div class="user-profile">
  <h2>{{user.name}}</h2>
  <p>{{user.email}}</p>
  <button (click)="editProfile()">Edit</button>
</div>
```

```typescript
// Standalone Componentでの使用
@Component({
  selector: 'app-dashboard',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './dashboard.component.html'
})
export class DashboardComponent {}
```

## 💻 詳細実装例（学習用）

### 基本的な外部テンプレート
```typescript
// user-profile.component.ts
import { Component } from '@angular/core';

@Component({
  selector: 'app-user-profile',
  standalone: true,
  templateUrl: './user-profile.component.html',
  styleUrls: ['./user-profile.component.css']
})
export class UserProfileComponent {
  user = {
    name: 'John Doe',
    email: 'john@example.com',
    role: 'Developer',
    avatar: 'https://via.placeholder.com/100'
  };

  editProfile() {
    console.log('Editing profile');
  }

  deleteAccount() {
    console.log('Deleting account');
  }
}
```

```html
<!-- user-profile.component.html -->
<div class="profile-container">
  <div class="profile-header">
    <img [src]="user.avatar" [alt]="user.name" class="avatar">
    <div class="user-info">
      <h2>{{user.name}}</h2>
      <p class="email">{{user.email}}</p>
      <span class="role-badge">{{user.role}}</span>
    </div>
  </div>

  <div class="profile-actions">
    <button class="btn btn-primary" (click)="editProfile()">
      Edit Profile
    </button>
    <button class="btn btn-danger" (click)="deleteAccount()">
      Delete Account
    </button>
  </div>
</div>
```

```css
/* user-profile.component.css */
.profile-container {
  max-width: 600px;
  margin: 20px auto;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 8px;
}

.profile-header {
  display: flex;
  gap: 20px;
  margin-bottom: 20px;
}

.avatar {
  width: 100px;
  height: 100px;
  border-radius: 50%;
}

.user-info h2 {
  margin: 0 0 8px 0;
  color: #333;
}

.email {
  color: #666;
  margin: 4px 0;
}

.role-badge {
  display: inline-block;
  padding: 4px 12px;
  background: #007bff;
  color: white;
  border-radius: 12px;
  font-size: 12px;
}

.profile-actions {
  display: flex;
  gap: 12px;
}

.btn {
  padding: 10px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-weight: bold;
}

.btn-primary {
  background: #007bff;
  color: white;
}

.btn-danger {
  background: #dc3545;
  color: white;
}
```

### 複雑なテンプレート構造
```typescript
// dashboard.component.ts
import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

interface DashboardData {
  stats: {
    users: number;
    revenue: number;
    orders: number;
  };
  recentActivities: Activity[];
}

interface Activity {
  id: number;
  type: 'user' | 'order' | 'payment';
  message: string;
  timestamp: Date;
}

@Component({
  selector: 'app-dashboard',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {
  data: DashboardData = {
    stats: {
      users: 0,
      revenue: 0,
      orders: 0
    },
    recentActivities: []
  };

  ngOnInit() {
    this.loadDashboardData();
  }

  loadDashboardData() {
    this.data = {
      stats: {
        users: 1234,
        revenue: 50000,
        orders: 856
      },
      recentActivities: [
        {
          id: 1,
          type: 'user',
          message: 'New user registered',
          timestamp: new Date()
        },
        {
          id: 2,
          type: 'order',
          message: 'Order #1234 completed',
          timestamp: new Date()
        }
      ]
    };
  }

  refreshData() {
    console.log('Refreshing dashboard data');
    this.loadDashboardData();
  }
}
```

```html
<!-- dashboard.component.html -->
<div class="dashboard">
  <header class="dashboard-header">
    <h1>Dashboard</h1>
    <button class="refresh-btn" (click)="refreshData()">
      Refresh
    </button>
  </header>

  <section class="stats-grid">
    <div class="stat-card">
      <h3>Total Users</h3>
      <p class="stat-value">{{data.stats.users | number}}</p>
    </div>

    <div class="stat-card">
      <h3>Revenue</h3>
      <p class="stat-value">¥{{data.stats.revenue | number}}</p>
    </div>

    <div class="stat-card">
      <h3>Orders</h3>
      <p class="stat-value">{{data.stats.orders | number}}</p>
    </div>
  </section>

  <section class="activities">
    <h2>Recent Activities</h2>

    @if (data.recentActivities.length > 0) {
      <ul class="activity-list">
        @for (activity of data.recentActivities; track activity.id) {
          <li [class]="'activity-item activity-' + activity.type">
            <span class="activity-icon">
              @switch (activity.type) {
                @case ('user') { 👤 }
                @case ('order') { 📦 }
                @case ('payment') { 💳 }
              }
            </span>
            <div class="activity-content">
              <p>{{activity.message}}</p>
              <small>{{activity.timestamp | date:'short'}}</small>
            </div>
          </li>
        }
      </ul>
    } @else {
      <p class="no-activities">No recent activities</p>
    }
  </section>
</div>
```

### フォームを含むテンプレート
```typescript
// contact-form.component.ts
import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-contact-form',
  standalone: true,
  imports: [FormsModule, CommonModule],
  templateUrl: './contact-form.component.html',
  styleUrls: ['./contact-form.component.css']
})
export class ContactFormComponent {
  formData = {
    name: '',
    email: '',
    subject: '',
    message: ''
  };

  submitted = false;

  onSubmit() {
    console.log('Form submitted:', this.formData);
    this.submitted = true;

    setTimeout(() => {
      this.resetForm();
    }, 3000);
  }

  resetForm() {
    this.formData = {
      name: '',
      email: '',
      subject: '',
      message: ''
    };
    this.submitted = false;
  }
}
```

```html
<!-- contact-form.component.html -->
<div class="contact-form-container">
  <h2>Contact Us</h2>

  @if (submitted) {
    <div class="success-message">
      <p>✅ Thank you! Your message has been sent.</p>
    </div>
  } @else {
    <form (ngSubmit)="onSubmit()" #contactForm="ngForm">
      <div class="form-group">
        <label for="name">Name *</label>
        <input
          type="text"
          id="name"
          name="name"
          [(ngModel)]="formData.name"
          required
          #nameInput="ngModel"
        >
        @if (nameInput.invalid && nameInput.touched) {
          <span class="error">Name is required</span>
        }
      </div>

      <div class="form-group">
        <label for="email">Email *</label>
        <input
          type="email"
          id="email"
          name="email"
          [(ngModel)]="formData.email"
          required
          email
          #emailInput="ngModel"
        >
        @if (emailInput.invalid && emailInput.touched) {
          <span class="error">Valid email is required</span>
        }
      </div>

      <div class="form-group">
        <label for="subject">Subject *</label>
        <input
          type="text"
          id="subject"
          name="subject"
          [(ngModel)]="formData.subject"
          required
        >
      </div>

      <div class="form-group">
        <label for="message">Message *</label>
        <textarea
          id="message"
          name="message"
          rows="5"
          [(ngModel)]="formData.message"
          required
        ></textarea>
      </div>

      <div class="form-actions">
        <button type="submit" [disabled]="contactForm.invalid">
          Send Message
        </button>
        <button type="button" (click)="resetForm()">
          Reset
        </button>
      </div>
    </form>
  }
</div>
```

### パス指定のバリエーション
```typescript
// 相対パス（推奨）
@Component({
  selector: 'app-example1',
  templateUrl: './example1.component.html'  // 同じディレクトリ
})
export class Example1Component {}

// サブディレクトリのテンプレート
@Component({
  selector: 'app-example2',
  templateUrl: './templates/example2.component.html'
})
export class Example2Component {}

// 親ディレクトリのテンプレート
@Component({
  selector: 'app-example3',
  templateUrl: '../shared/template.component.html'
})
export class Example3Component {}

// ❌ 絶対パスは非推奨
@Component({
  selector: 'app-bad',
  templateUrl: '/src/app/bad.component.html'  // 避けるべき
})
export class BadComponent {}
```

### テンプレートとインラインの使い分け
```typescript
// ✅ 小さなComponent: インライン
@Component({
  selector: 'app-badge',
  standalone: true,
  template: `<span class="badge">{{text}}</span>`
})
export class BadgeComponent {
  text = 'New';
}

// ✅ 中〜大規模Component: 外部ファイル
@Component({
  selector: 'app-product-list',
  standalone: true,
  templateUrl: './product-list.component.html',
  styleUrls: ['./product-list.component.css']
})
export class ProductListComponent {}

// ✅ 複雑なロジックを含むComponent: 外部ファイル
@Component({
  selector: 'app-data-table',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './data-table.component.html',
  styleUrls: ['./data-table.component.css']
})
export class DataTableComponent {}
```

## ベストプラクティス

1. **相対パスを使用**: `./`から始まるパス指定
2. **大規模テンプレートは外部化**: 10行以上はtemplateUrlを推奨
3. **ファイル名の統一**: component.component.html形式
4. **HTMLエディタの活用**: シンタックスハイライトと補完を活用

## 注意点

- templateとtemplateUrlは同時に使用不可
- パスは相対パスが推奨（絶対パスは避ける）
- ファイルの存在を確認（ビルドエラーの原因になる）
- CLIで生成すると自動的にtemplateUrlが設定される

## 関連技術
- File System
- Module Resolution
- HTML Templates
- Build Process
