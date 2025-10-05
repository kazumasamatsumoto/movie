# #019 「Component 作成時のよくあるエラー」台本

四国めたん「Component 作成時のよくあるエラーについて解説します！」
ずんだもん「どんなエラーがよくあるの？」
四国めたん「セレクタの重複、テンプレートの構文エラー、依存関係の不足などがあります」
ずんだもん「エラーの原因は？」
四国めたん「命名規則の不統一、Angularの構文ミス、必要なモジュールの未インポートなどです」
ずんだもん「どうやって防ぐの？」
四国めたん「IDEの補完機能を活用し、Angularの公式ドキュメントを参照することが重要です」

---

## 📺 画面表示用コード

// エラー1: セレクタの重複
```typescript
// ❌ エラー例：同じセレクタを使用
@Component({
  selector: 'app-button',  // 重複
  template: '<button>ボタン1</button>'
})
export class ButtonComponent1 { }

@Component({
  selector: 'app-button',  // 重複
  template: '<button>ボタン2</button>'
})
export class ButtonComponent2 { }

// ✅ 解決方法：一意なセレクタを使用
@Component({
  selector: 'app-primary-button',
  template: '<button>プライマリボタン</button>'
})
export class PrimaryButtonComponent { }

@Component({
  selector: 'app-secondary-button',
  template: '<button>セカンダリボタン</button>'
})
export class SecondaryButtonComponent { }
```

// エラー2: テンプレートの構文エラー
```typescript
// ❌ エラー例：不正なテンプレート構文
@Component({
  selector: 'app-syntax-error',
  template: `
    <div>
      <h1>{{title</h1>  <!-- 閉じ括弧が不足 -->
      <p *ngIf="isVisible" *ngFor="let item of items">  <!-- 複数の構造ディレクティブ -->
        {{item}}
      </p>
    </div>
  `
})
export class SyntaxErrorComponent {
  title = 'タイトル';
  isVisible = true;
  items = ['項目1', '項目2'];
}

// ✅ 解決方法：正しい構文を使用
@Component({
  selector: 'app-syntax-correct',
  template: `
    <div>
      <h1>{{title}}</h1>  <!-- 正しい補間 -->
      <div *ngIf="isVisible">
        <p *ngFor="let item of items">  <!-- 構造ディレクティブを分離 -->
          {{item}}
        </p>
      </div>
    </div>
  `
})
export class SyntaxCorrectComponent {
  title = 'タイトル';
  isVisible = true;
  items = ['項目1', '項目2'];
}
```

// エラー3: 依存関係の不足
```typescript
// ❌ エラー例：必要なモジュールがインポートされていない
@Component({
  selector: 'app-missing-deps',
  standalone: true,
  template: `
    <div>
      <p *ngIf="isVisible">表示中</p>  <!-- CommonModuleが必要 -->
      <input [(ngModel)]="name">  <!-- FormsModuleが必要 -->
    </div>
  `
})
export class MissingDepsComponent {
  isVisible = true;
  name = '';
}

// ✅ 解決方法：必要なモジュールをインポート
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-correct-deps',
  standalone: true,
  imports: [CommonModule, FormsModule],  // 必要なモジュールをインポート
  template: `
    <div>
      <p *ngIf="isVisible">表示中</p>
      <input [(ngModel)]="name">
    </div>
  `
})
export class CorrectDepsComponent {
  isVisible = true;
  name = '';
}
```

// エラー4: 型の不一致
```typescript
// ❌ エラー例：型の不一致
interface User {
  id: number;
  name: string;
}

@Component({
  selector: 'app-type-error',
  template: `
    <div>
      <h2>{{user.name}}</h2>
      <p>{{user.age}}</p>  <!-- ageプロパティが存在しない -->
    </div>
  `
})
export class TypeErrorComponent {
  @Input() user: User = { id: 1, name: '田中太郎' };
  
  // user.ageは存在しないプロパティ
}

// ✅ 解決方法：正しい型定義を使用
interface User {
  id: number;
  name: string;
  age: number;  // ageプロパティを追加
}

@Component({
  selector: 'app-type-correct',
  template: `
    <div>
      <h2>{{user.name}}</h2>
      <p>{{user.age}}歳</p>
    </div>
  `
})
export class TypeCorrectComponent {
  @Input() user: User = { id: 1, name: '田中太郎', age: 30 };
}
```

// エラー5: 循環依存
```typescript
// ❌ エラー例：循環依存
// user.component.ts
import { UserService } from './user.service';

@Component({
  selector: 'app-user',
  template: '<div>{{user.name}}</div>'
})
export class UserComponent {
  constructor(private userService: UserService) {}
  user = this.userService.getUser();
}

// user.service.ts
import { UserComponent } from './user.component';  // 循環依存

@Injectable()
export class UserService {
  constructor(private userComponent: UserComponent) {}  // 循環依存
}

// ✅ 解決方法：依存関係を整理
// user.service.ts
@Injectable()
export class UserService {
  getUser() {
    return { id: 1, name: '田中太郎' };
  }
}

// user.component.ts
import { UserService } from './user.service';

@Component({
  selector: 'app-user',
  template: '<div>{{user.name}}</div>'
})
export class UserComponent {
  constructor(private userService: UserService) {}
  user = this.userService.getUser();
}
```

// エラー6: 未定義のプロパティ
```typescript
// ❌ エラー例：未定義のプロパティ
@Component({
  selector: 'app-undefined',
  template: `
    <div>
      <h2>{{title}}</h2>
      <p>{{description}}</p>  <!-- descriptionが未定義 -->
    </div>
  `
})
export class UndefinedComponent {
  title = 'タイトル';
  // descriptionが定義されていない
}

// ✅ 解決方法：プロパティを定義
@Component({
  selector: 'app-defined',
  template: `
    <div>
      <h2>{{title}}</h2>
      <p>{{description}}</p>
    </div>
  `
})
export class DefinedComponent {
  title = 'タイトル';
  description = '説明文';  // プロパティを定義
}
```

// エラー7: 不正なイベントバインディング
```typescript
// ❌ エラー例：不正なイベントバインディング
@Component({
  selector: 'app-event-error',
  template: `
    <div>
      <button (click)="onClick()">クリック</button>
      <input (input)="onInput($event)">  <!-- メソッドが未定義 -->
    </div>
  `
})
export class EventErrorComponent {
  onClick() {
    console.log('クリックされました');
  }
  // onInputメソッドが定義されていない
}

// ✅ 解決方法：メソッドを定義
@Component({
  selector: 'app-event-correct',
  template: `
    <div>
      <button (click)="onClick()">クリック</button>
      <input (input)="onInput($event)">
    </div>
  `
})
export class EventCorrectComponent {
  onClick() {
    console.log('クリックされました');
  }
  
  onInput(event: any) {  // メソッドを定義
    console.log('入力されました:', event.target.value);
  }
}
```

// エラーの予防方法
```typescript
@Component({
  selector: 'app-prevention',
  template: `
    <div>
      <h2>エラーの予防方法</h2>
      <ul>
        <li>IDEの補完機能を活用</li>
        <li>TypeScriptの型チェックを有効化</li>
        <li>Angularの公式ドキュメントを参照</li>
        <li>命名規則を統一</li>
        <li>段階的に開発</li>
        <li>テストを書く</li>
        <li>コードレビューを実施</li>
        <li>エラーメッセージをよく読む</li>
      </ul>
    </div>
  `
})
export class PreventionComponent {
  // エラーを防ぐためのベストプラクティス
}
```
