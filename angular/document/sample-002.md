# #002 「CLI で Component 作成 - ng generate component」台本

四国めたん「CLI で Component 作成 - ng generate componentについて解説します！」
ずんだもん「手動で作るのと何が違うの？」
四国めたん「CLIを使うことで、必要なファイルとコードが自動生成され、設定も正しく行われます」
ずんだもん「どんなファイルが作られるの？」
四国めたん「Componentクラス、テンプレート、スタイル、テストファイルが生成されます」
ずんだもん「設定も自動でやってくれるんだね！」
四国めたん「はい！NgModuleへの登録も自動で行われ、すぐに使用できます」

---

## 📺 画面表示用コード

// CLIコマンドの基本構文
```bash
ng generate component component-name
# または短縮形
ng g c component-name
```

// 具体的な生成例
```bash
ng g c user-profile
```

// 生成されるファイル構造
```
src/app/user-profile/
├── user-profile.component.ts      # Componentクラス
├── user-profile.component.html    # テンプレート
├── user-profile.component.css     # スタイル
└── user-profile.component.spec.ts # テストファイル
```

// 自動生成されるComponentクラス
```typescript
import { Component } from '@angular/core';

@Component({
  selector: 'app-user-profile',
  templateUrl: './user-profile.component.html',
  styleUrls: ['./user-profile.component.css']
})
export class UserProfileComponent {

}
```

// 自動生成されるテンプレート
```html
<p>user-profile works!</p>
```

// オプション付きの生成
```bash
# インラインテンプレートで生成
ng g c user-card --inline-template

# インラインスタイルで生成
ng g c user-card --inline-style

# 両方インラインで生成
ng g c user-card --inline-template --inline-style

# テストファイルなしで生成
ng g c user-card --skip-tests
```

// Standalone Componentの生成（v14+）
```bash
ng g c user-profile --standalone
```

// 生成されるStandalone Component
```typescript
import { Component } from '@angular/core';

@Component({
  selector: 'app-user-profile',
  standalone: true,
  imports: [],
  templateUrl: './user-profile.component.html',
  styleUrls: ['./user-profile.component.css']
})
export class UserProfileComponent {

}
```

// 特定のモジュールに生成
```bash
ng g c user-profile --module=user
```

// フラット構造で生成（フォルダを作らない）
```bash
ng g c user-profile --flat
```
