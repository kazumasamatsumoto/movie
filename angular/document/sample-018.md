# #018 「Component のベストプラクティス」台本

四国めたん「Component のベストプラクティスについて解説します！」
ずんだもん「ベストプラクティスって何？」
四国めたん「Componentを効率的に開発・保守するための推奨される方法やパターンです」
ずんだもん「どんなものがあるの？」
四国めたん「単一責任の原則、再利用性、パフォーマンス、テスト容易性などがあります」
ずんだもん「なぜ重要なの？」
四国めたん「コードの品質向上、開発効率の向上、バグの削減に繋がります」

---

## 📺 画面表示用コード

// 単一責任の原則
```typescript
// ✅ 良い例：単一の責任を持つComponent
@Component({
  selector: 'app-user-list',
  standalone: true,
  template: `
    <div>
      <h2>ユーザー一覧</h2>
      <ul>
        <li *ngFor="let user of users">{{user.name}}</li>
      </ul>
    </div>
  `
})
export class UserListComponent {
  @Input() users: User[] = [];
  
  // ユーザー一覧の表示のみに責任を持つ
}

// ❌ 悪い例：複数の責任を持つComponent
@Component({
  selector: 'app-user-management',
  template: `
    <div>
      <h2>ユーザー管理</h2>
      <ul>
        <li *ngFor="let user of users">{{user.name}}</li>
      </ul>
      <form>
        <input [(ngModel)]="newUser.name">
        <button (click)="addUser()">追加</button>
      </form>
      <button (click)="exportUsers()">エクスポート</button>
    </div>
  `
})
export class UserManagementComponent {
  // 表示、追加、エクスポートの複数の責任を持つ
}
```

// 再利用性の向上
```typescript
// ✅ 良い例：再利用可能なComponent
@Component({
  selector: 'app-button',
  standalone: true,
  template: `
    <button 
      [class]="buttonClass"
      [disabled]="disabled"
      (click)="onClick.emit()">
      <ng-content></ng-content>
    </button>
  `
})
export class ButtonComponent {
  @Input() buttonClass = 'btn-primary';
  @Input() disabled = false;
  @Output() onClick = new EventEmitter<void>();
}

// 使用例
@Component({
  selector: 'app-usage',
  standalone: true,
  imports: [ButtonComponent],
  template: `
    <app-button buttonClass="btn-primary">保存</app-button>
    <app-button buttonClass="btn-secondary" [disabled]="true">キャンセル</app-button>
  `
})
export class UsageComponent { }
```

// パフォーマンスの最適化
```typescript
// ✅ 良い例：OnPush変更検知戦略
@Component({
  selector: 'app-optimized',
  standalone: true,
  changeDetection: ChangeDetectionStrategy.OnPush,
  template: `
    <div>
      <h2>{{title}}</h2>
      <p>{{description}}</p>
    </div>
  `
})
export class OptimizedComponent {
  @Input() title = '';
  @Input() description = '';
  
  // OnPushにより変更検知が最適化される
}

// ✅ 良い例：trackBy関数の使用
@Component({
  selector: 'app-list',
  standalone: true,
  template: `
    <ul>
      <li *ngFor="let item of items; trackBy: trackByFn">
        {{item.name}}
      </li>
    </ul>
  `
})
export class ListComponent {
  items: Item[] = [];
  
  trackByFn(index: number, item: Item): number {
    return item.id;
  }
}
```

// テンプレートの最適化
```typescript
// ✅ 良い例：テンプレートの最適化
@Component({
  selector: 'app-template-optimized',
  standalone: true,
  template: `
    <div>
      <h2>{{title}}</h2>
      <div *ngIf="isLoading; else content">
        <p>読み込み中...</p>
      </div>
      <ng-template #content>
        <p>{{data}}</p>
      </ng-template>
    </div>
  `
})
export class TemplateOptimizedComponent {
  title = '最適化されたテンプレート';
  isLoading = false;
  data = 'データ';
}

// ❌ 悪い例：非効率なテンプレート
@Component({
  selector: 'app-template-bad',
  template: `
    <div>
      <h2>{{title}}</h2>
      <p *ngIf="isLoading">読み込み中...</p>
      <p *ngIf="!isLoading">{{data}}</p>
    </div>
  `
})
export class TemplateBadComponent {
  // 条件分岐が複雑
}
```

// 型安全性の確保
```typescript
// ✅ 良い例：型安全なComponent
interface User {
  id: number;
  name: string;
  email: string;
}

@Component({
  selector: 'app-type-safe',
  standalone: true,
  template: `
    <div>
      <h2>{{user.name}}</h2>
      <p>{{user.email}}</p>
    </div>
  `
})
export class TypeSafeComponent {
  @Input() user!: User;  // 型を明示
  
  // 型安全性によりエラーを防ぐ
}

// ❌ 悪い例：型が不明確
@Component({
  selector: 'app-type-unsafe',
  template: `
    <div>
      <h2>{{user.name}}</h2>
      <p>{{user.email}}</p>
    </div>
  `
})
export class TypeUnsafeComponent {
  @Input() user: any;  // 型が不明確
  
  // 実行時エラーのリスク
}
```

// エラーハンドリング
```typescript
// ✅ 良い例：エラーハンドリング
@Component({
  selector: 'app-error-handling',
  standalone: true,
  template: `
    <div>
      <h2>データ表示</h2>
      <div *ngIf="error; else dataContent">
        <p class="error">エラーが発生しました: {{error}}</p>
        <button (click)="retry()">再試行</button>
      </div>
      <ng-template #dataContent>
        <p>{{data}}</p>
      </ng-template>
    </div>
  `
})
export class ErrorHandlingComponent {
  data = '';
  error: string | null = null;
  
  async loadData() {
    try {
      this.error = null;
      this.data = await this.dataService.getData();
    } catch (err) {
      this.error = 'データの読み込みに失敗しました';
    }
  }
  
  retry() {
    this.loadData();
  }
}
```

// アクセシビリティの考慮
```typescript
// ✅ 良い例：アクセシビリティを考慮したComponent
@Component({
  selector: 'app-accessible',
  standalone: true,
  template: `
    <div>
      <h2>アクセシビリティ対応</h2>
      <button 
        (click)="toggle()"
        [attr.aria-expanded]="isExpanded"
        [attr.aria-label]="isExpanded ? '閉じる' : '開く'">
        {{isExpanded ? '閉じる' : '開く'}}
      </button>
      <div 
        *ngIf="isExpanded"
        [attr.aria-hidden]="!isExpanded">
        <p>コンテンツ</p>
      </div>
    </div>
  `
})
export class AccessibleComponent {
  isExpanded = false;
  
  toggle() {
    this.isExpanded = !this.isExpanded;
  }
}
```

// テスト容易性
```typescript
// ✅ 良い例：テストしやすいComponent
@Component({
  selector: 'app-testable',
  standalone: true,
  template: `
    <div>
      <h2>{{title}}</h2>
      <button (click)="increment()">カウント: {{count}}</button>
    </div>
  `
})
export class TestableComponent {
  @Input() title = '';
  count = 0;
  
  increment() {
    this.count++;
  }
  
  // シンプルでテストしやすい
}

// テスト例
describe('TestableComponent', () => {
  let component: TestableComponent;
  let fixture: ComponentFixture<TestableComponent>;
  
  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [TestableComponent]
    });
    fixture = TestBed.createComponent(TestableComponent);
    component = fixture.componentInstance;
  });
  
  it('should increment count', () => {
    component.increment();
    expect(component.count).toBe(1);
  });
});
```

// ベストプラクティスのまとめ
```typescript
@Component({
  selector: 'app-summary',
  standalone: true,
  template: `
    <div>
      <h2>Component ベストプラクティス</h2>
      <ul>
        <li>単一責任の原則</li>
        <li>再利用性の向上</li>
        <li>パフォーマンスの最適化</li>
        <li>型安全性の確保</li>
        <li>エラーハンドリング</li>
        <li>アクセシビリティの考慮</li>
        <li>テスト容易性</li>
        <li>命名規則の統一</li>
        <li>ドキュメントの整備</li>
      </ul>
    </div>
  `
})
export class SummaryComponent {
  // これらのベストプラクティスを適用して
  // 高品質なComponentを開発しましょう
}
```
