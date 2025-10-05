# #012 「Component の命名規則」台本

四国めたん「Component の命名規則について解説します！」
ずんだもん「命名規則ってなぜ重要なの？」
四国めたん「一貫性のある命名により、コードの可読性と保守性が向上します」
ずんだもん「どんな規則があるの？」
四国めたん「PascalCase、kebab-case、camelCaseを適切に使い分けます」
ずんだもん「ファイル名とクラス名は違うの？」
四国めたん「はい！ファイル名はkebab-case、クラス名はPascalCaseです」

---

## 📺 画面表示用コード

// ファイル名の命名規則（kebab-case）
```
user-profile.component.ts      ✅ 正しい
user-profile.component.html    ✅ 正しい
user-profile.component.css     ✅ 正しい
user-profile.component.spec.ts ✅ 正しい

UserProfile.component.ts       ❌ 間違い
userProfile.component.ts       ❌ 間違い
user_profile.component.ts      ❌ 間違い
```

// クラス名の命名規則（PascalCase）
```typescript
// ✅ 正しい命名
export class UserProfileComponent {
  // Componentクラス
}

export class UserProfileService {
  // サービスクラス
}

export class UserProfileInterface {
  // インターフェース
}

// ❌ 間違った命名
export class userProfileComponent {  // camelCase
export class user_profile_component { // snake_case
export class userprofilecomponent {   // 区切りなし
```

// セレクタの命名規則（kebab-case）
```typescript
@Component({
  selector: 'app-user-profile',    // ✅ 正しい
  // selector: 'appUserProfile',   // ❌ camelCase
  // selector: 'app_user_profile', // ❌ snake_case
  template: '<div>User Profile</div>'
})
export class UserProfileComponent {
  // app-プレフィックス + kebab-case
}
```

// プロパティの命名規則（camelCase）
```typescript
@Component({
  selector: 'app-naming',
  template: `
    <div>
      <h1>{{pageTitle}}</h1>
      <p>{{userCount}}</p>
      <p>{{isLoading}}</p>
    </div>
  `
})
export class NamingComponent {
  // ✅ 正しいプロパティ命名
  pageTitle: string = 'ページタイトル';
  userCount: number = 0;
  isLoading: boolean = false;
  userList: User[] = [];
  
  // ❌ 間違ったプロパティ命名
  // page_title: string;     // snake_case
  // PageTitle: string;      // PascalCase
  // page-title: string;     // kebab-case
}
```

// メソッドの命名規則（camelCase）
```typescript
@Component({
  selector: 'app-methods',
  template: `
    <div>
      <button (click)="onButtonClick()">クリック</button>
      <button (click)="handleUserSubmit()">送信</button>
    </div>
  `
})
export class MethodsComponent {
  // ✅ 正しいメソッド命名
  onButtonClick() {
    console.log('ボタンがクリックされました');
  }
  
  handleUserSubmit() {
    console.log('ユーザー送信処理');
  }
  
  calculateTotalPrice() {
    return 1000;
  }
  
  // ❌ 間違ったメソッド命名
  // on_button_click() { }     // snake_case
  // OnButtonClick() { }       // PascalCase
  // on-button-click() { }     // kebab-case
}
```

// 定数の命名規則（UPPER_SNAKE_CASE）
```typescript
@Component({
  selector: 'app-constants',
  template: '<div>{{API_URL}}</div>'
})
export class ConstantsComponent {
  // ✅ 正しい定数命名
  readonly API_URL = 'https://api.example.com';
  readonly MAX_RETRY_COUNT = 3;
  readonly DEFAULT_TIMEOUT = 5000;
  
  // ❌ 間違った定数命名
  // readonly apiUrl = 'https://api.example.com';  // camelCase
  // readonly ApiUrl = 'https://api.example.com';  // PascalCase
}
```

// インターフェースの命名規則（PascalCase）
```typescript
// ✅ 正しいインターフェース命名
interface UserProfile {
  id: number;
  name: string;
  email: string;
}

interface ApiResponse<T> {
  data: T;
  status: number;
}

// ❌ 間違ったインターフェース命名
// interface userProfile { }        // camelCase
// interface user_profile { }       // snake_case
// interface user-profile { }       // kebab-case
```

// 型エイリアスの命名規則（PascalCase）
```typescript
// ✅ 正しい型エイリアス命名
type UserStatus = 'active' | 'inactive' | 'pending';
type ThemeMode = 'light' | 'dark';

// ❌ 間違った型エイリアス命名
// type userStatus = 'active' | 'inactive';  // camelCase
// type user_status = 'active' | 'inactive'; // snake_case
```

// ファイル構成での命名例
```
src/app/
├── user-management/           # kebab-case
│   ├── user-list/            # kebab-case
│   │   ├── user-list.component.ts
│   │   ├── user-list.component.html
│   │   └── user-list.component.css
│   └── user-detail/          # kebab-case
│       ├── user-detail.component.ts
│       └── user-detail.service.ts
└── shared/                   # kebab-case
    ├── header/
    └── footer/
```

// インポート文での命名
```typescript
// ✅ 正しいインポート
import { UserListComponent } from './user-list/user-list.component';
import { UserDetailService } from './user-detail/user-detail.service';

// ❌ 間違ったインポート
// import { userListComponent } from './user-list/user-list.component';
// import { UserListComponent } from './user-list/UserList.component';
```

// 命名規則のまとめ
```typescript
@Component({
  selector: 'app-naming-summary',
  template: `
    <div>
      <h2>命名規則まとめ</h2>
      <ul>
        <li>ファイル名: kebab-case</li>
        <li>クラス名: PascalCase</li>
        <li>セレクタ: kebab-case</li>
        <li>プロパティ: camelCase</li>
        <li>メソッド: camelCase</li>
        <li>定数: UPPER_SNAKE_CASE</li>
        <li>インターフェース: PascalCase</li>
      </ul>
    </div>
  `
})
export class NamingSummaryComponent {
  // 一貫性のある命名が重要
}
```
