# #008 「styleUrls - 外部スタイルファイル」台本

四国めたん「styleUrls - 外部スタイルファイルについて解説します！」
ずんだもん「外部スタイルファイルのメリットは？」
四国めたん「CSSエディタの機能が使え、複雑なスタイルも管理しやすくなります」
ずんだもん「どんな時に使うの？」
四国めたん「複雑なスタイルや、チーム開発でCSSとTypeScriptを分離したい場合です」
ずんだもん「複数のファイルも使えるの？」
四国めたん「はい！複数のCSSファイルを組み合わせて使用できます」

---

## 📺 画面表示用コード

// 基本的な外部スタイルファイルの使用
```typescript
@Component({
  selector: 'app-external-style',
  templateUrl: './external-style.component.html',
  styleUrls: ['./external-style.component.css']
})
export class ExternalStyleComponent {
  title = '外部スタイル';
  message = '外部CSSファイルを使用しています';
}
```

// ファイル構造例
```
src/app/external-style/
├── external-style.component.ts
├── external-style.component.html
├── external-style.component.css
└── external-style.component.spec.ts
```

// 外部CSSファイルの内容例
```css
/* external-style.component.css */
.container {
  padding: 20px;
  background-color: #f8f9fa;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.title {
  color: #007bff;
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 16px;
}

.message {
  color: #6c757d;
  line-height: 1.6;
  margin-bottom: 0;
}
```

// 複数のスタイルファイル
```typescript
@Component({
  selector: 'app-multiple-styles',
  templateUrl: './multiple-styles.component.html',
  styleUrls: [
    './multiple-styles.component.css',
    './multiple-styles.theme.css',
    './multiple-styles.responsive.css'
  ]
})
export class MultipleStylesComponent {
  // 複数のCSSファイルを組み合わせ
}
```

// テーマ用CSSファイル
```css
/* multiple-styles.theme.css */
.container {
  --primary-color: #007bff;
  --secondary-color: #6c757d;
  --background-color: #ffffff;
}

.container.dark-theme {
  --primary-color: #0d6efd;
  --secondary-color: #adb5bd;
  --background-color: #212529;
  background-color: var(--background-color);
  color: var(--secondary-color);
}
```

// レスポンシブ用CSSファイル
```css
/* multiple-styles.responsive.css */
@media (max-width: 768px) {
  .container {
    padding: 10px;
    margin: 5px;
  }
  
  .title {
    font-size: 20px;
  }
}

@media (min-width: 1200px) {
  .container {
    padding: 30px;
    max-width: 1200px;
    margin: 0 auto;
  }
}
```

// 複雑なスタイルの例
```typescript
@Component({
  selector: 'app-complex-styles',
  templateUrl: './complex-styles.component.html',
  styleUrls: ['./complex-styles.component.css']
})
export class ComplexStylesComponent {
  users = [
    { name: '田中太郎', role: 'admin', status: 'active' },
    { name: '佐藤花子', role: 'user', status: 'inactive' }
  ];
}
```

// 複雑なCSSファイル
```css
/* complex-styles.component.css */
.user-management {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
}

.user-table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 20px;
  background-color: white;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.user-table th,
.user-table td {
  padding: 12px 16px;
  text-align: left;
  border-bottom: 1px solid #e9ecef;
}

.user-table th {
  background-color: #f8f9fa;
  font-weight: 600;
  color: #495057;
}

.user-table tr:hover {
  background-color: #f8f9fa;
}

.role-admin {
  color: #dc3545;
  font-weight: bold;
}

.role-user {
  color: #28a745;
}

.status-active {
  color: #28a745;
}

.status-inactive {
  color: #6c757d;
}

.status-badge {
  display: inline-block;
  padding: 4px 8px;
  border-radius: 12px;
  font-size: 12px;
  font-weight: 500;
}

.status-active .status-badge {
  background-color: #d4edda;
  color: #155724;
}

.status-inactive .status-badge {
  background-color: #f8d7da;
  color: #721c24;
}
```

// 外部スタイルファイルの利点
```typescript
@Component({
  selector: 'app-benefits',
  templateUrl: './benefits.component.html',
  styleUrls: ['./benefits.component.css']
})
export class BenefitsComponent {
  benefits = [
    'CSSエディタの機能が使える',
    'シンタックスハイライト',
    '自動補完',
    'エラーチェック',
    'フォーマット機能',
    '可読性の向上',
    '保守性の向上',
    '複数ファイルの管理'
  ];
}
```

// 外部スタイルファイルの注意点
```typescript
@Component({
  selector: 'app-considerations',
  templateUrl: './considerations.component.html',
  styleUrls: ['./considerations.component.css']
})
export class ConsiderationsComponent {
  // 注意点:
  // 1. ファイルパスが正しいか確認
  // 2. ファイルが存在するか確認
  // 3. CSSの読み込み順序
  // 4. ビルド時のパス解決
  // 5. スタイルの競合
}
```
