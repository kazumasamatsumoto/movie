# #231 「ng-template + ViewContainerRef」

## 概要
ng-templateとViewContainerRefを組み合わせることで、テンプレートを動的に挿入できます。createEmbeddedView()メソッドを使い、コンポーネントよりも軽量で柔軟なUI構築が可能です。コンテキストを渡すことでテンプレート内でデータを利用できます。

## 学習目標
- ng-templateの動的挿入方法を習得する
- createEmbeddedView()の使い方を理解する
- テンプレートコンテキストの活用方法を学ぶ

## 技術ポイント
- **createEmbeddedView()**: テンプレートの動的挿入
- **TemplateRef**: テンプレート参照の取得
- **コンテキスト**: テンプレートへのデータ渡し

## 📺 画面表示用コード

### 基本的な使い方
```typescript
@Component({
  template: `
    <ng-template #myTemplate>
      <p>動的に挿入されるテンプレート</p>
    </ng-template>
    <ng-container #container></ng-container>
  `
})
export class TemplateComponent {
  @ViewChild('myTemplate') template!: TemplateRef<any>;
  @ViewChild('container', { read: ViewContainerRef })
  container!: ViewContainerRef;

  ngAfterViewInit() {
    this.container.createEmbeddedView(this.template);
  }
}
```

### コンテキスト付き挿入
```typescript
@Component({
  template: `
    <ng-template #userTemplate let-name let-age="age">
      <p>{{ name }} ({{ age }}歳)</p>
    </ng-template>
  `
})
export class ContextComponent {
  insertTemplate() {
    this.container.createEmbeddedView(this.template, {
      $implicit: 'John',
      age: 25
    });
  }
}
```

### 複数テンプレートの切り替え
```typescript
@Component({
  template: `
    <ng-template #templateA><p>テンプレートA</p></ng-template>
    <ng-template #templateB><p>テンプレートB</p></ng-template>
    <ng-container #container></ng-container>
  `
})
export class SwitchComponent {
  switchTemplate(template: TemplateRef<any>) {
    this.container.clear();
    this.container.createEmbeddedView(template);
  }
}
```

## 実践的な活用例

### カスタム構造ディレクティブ
```typescript
@Directive({
  selector: '[appRepeat]',
  standalone: true
})
export class RepeatDirective {
  private viewContainer = inject(ViewContainerRef);

  @Input() set appRepeat(count: number) {
    this.viewContainer.clear();

    for (let i = 0; i < count; i++) {
      this.viewContainer.createEmbeddedView(this.templateRef, {
        $implicit: i,
        index: i,
        count: count
      });
    }
  }

  constructor(private templateRef: TemplateRef<any>) {}
}

// 使用例
@Component({
  template: `
    <div *appRepeat="5; let i; let idx = index">
      {{ idx }}: アイテム {{ i }}
    </div>
  `
})
export class AppComponent {}
```

### 条件付きテンプレート表示
```typescript
@Component({
  selector: 'app-conditional-template',
  template: `
    <button (click)="toggleView()">切り替え</button>

    <ng-template #loading>
      <div class="spinner">読み込み中...</div>
    </ng-template>

    <ng-template #content let-data>
      <div class="content">{{ data }}</div>
    </ng-template>

    <ng-template #error let-message>
      <div class="error">エラー: {{ message }}</div>
    </ng-template>

    <ng-container #container></ng-container>
  `
})
export class ConditionalTemplateComponent {
  @ViewChild('loading') loadingTemplate!: TemplateRef<any>;
  @ViewChild('content') contentTemplate!: TemplateRef<any>;
  @ViewChild('error') errorTemplate!: TemplateRef<any>;
  @ViewChild('container', { read: ViewContainerRef })
  container!: ViewContainerRef;

  private state: 'loading' | 'content' | 'error' = 'loading';

  ngAfterViewInit() {
    this.updateView();
  }

  toggleView() {
    const states: Array<'loading' | 'content' | 'error'> =
      ['loading', 'content', 'error'];
    const currentIndex = states.indexOf(this.state);
    this.state = states[(currentIndex + 1) % states.length];
    this.updateView();
  }

  private updateView() {
    this.container.clear();

    switch (this.state) {
      case 'loading':
        this.container.createEmbeddedView(this.loadingTemplate);
        break;
      case 'content':
        this.container.createEmbeddedView(this.contentTemplate, {
          $implicit: 'データが読み込まれました'
        });
        break;
      case 'error':
        this.container.createEmbeddedView(this.errorTemplate, {
          $implicit: 'データの取得に失敗しました'
        });
        break;
    }
  }
}
```

### 動的リストレンダリング
```typescript
interface ListItem {
  id: number;
  name: string;
  type: 'text' | 'image' | 'video';
}

@Component({
  selector: 'app-dynamic-list',
  template: `
    <ng-template #textTemplate let-item>
      <div class="text-item">📄 {{ item.name }}</div>
    </ng-template>

    <ng-template #imageTemplate let-item>
      <div class="image-item">🖼️ {{ item.name }}</div>
    </ng-template>

    <ng-template #videoTemplate let-item>
      <div class="video-item">🎬 {{ item.name }}</div>
    </ng-template>

    <div #listContainer></div>
  `
})
export class DynamicListComponent {
  @ViewChild('textTemplate') textTemplate!: TemplateRef<any>;
  @ViewChild('imageTemplate') imageTemplate!: TemplateRef<any>;
  @ViewChild('videoTemplate') videoTemplate!: TemplateRef<any>;
  @ViewChild('listContainer', { read: ViewContainerRef })
  container!: ViewContainerRef;

  items: ListItem[] = [
    { id: 1, name: 'Document.pdf', type: 'text' },
    { id: 2, name: 'Photo.jpg', type: 'image' },
    { id: 3, name: 'Video.mp4', type: 'video' }
  ];

  ngAfterViewInit() {
    this.renderList();
  }

  renderList() {
    this.container.clear();

    this.items.forEach(item => {
      const template = this.getTemplate(item.type);
      this.container.createEmbeddedView(template, { $implicit: item });
    });
  }

  private getTemplate(type: string): TemplateRef<any> {
    switch (type) {
      case 'text': return this.textTemplate;
      case 'image': return this.imageTemplate;
      case 'video': return this.videoTemplate;
      default: return this.textTemplate;
    }
  }
}
```

### テンプレートアウトレットパターン
```typescript
@Component({
  selector: 'app-card',
  template: `
    <div class="card">
      <div class="header">
        <ng-container #headerOutlet></ng-container>
      </div>
      <div class="body">
        <ng-container #bodyOutlet></ng-container>
      </div>
      <div class="footer">
        <ng-container #footerOutlet></ng-container>
      </div>
    </div>
  `
})
export class CardComponent {
  @ViewChild('headerOutlet', { read: ViewContainerRef })
  headerContainer!: ViewContainerRef;

  @ViewChild('bodyOutlet', { read: ViewContainerRef })
  bodyContainer!: ViewContainerRef;

  @ViewChild('footerOutlet', { read: ViewContainerRef })
  footerContainer!: ViewContainerRef;

  @Input() set headerTemplate(template: TemplateRef<any> | null) {
    if (template) {
      this.headerContainer.clear();
      this.headerContainer.createEmbeddedView(template);
    }
  }

  @Input() set bodyTemplate(template: TemplateRef<any> | null) {
    if (template) {
      this.bodyContainer.clear();
      this.bodyContainer.createEmbeddedView(template);
    }
  }

  @Input() set footerTemplate(template: TemplateRef<any> | null) {
    if (template) {
      this.footerContainer.clear();
      this.footerContainer.createEmbeddedView(template);
    }
  }
}

// 使用例
@Component({
  template: `
    <app-card
      [headerTemplate]="header"
      [bodyTemplate]="body"
      [footerTemplate]="footer">
    </app-card>

    <ng-template #header><h2>カードタイトル</h2></ng-template>
    <ng-template #body><p>カードの内容</p></ng-template>
    <ng-template #footer><button>アクション</button></ng-template>
  `
})
export class AppComponent {}
```

### 動的フォームフィールド
```typescript
interface FieldConfig {
  type: 'text' | 'select' | 'checkbox';
  label: string;
  name: string;
  options?: string[];
}

@Component({
  selector: 'app-dynamic-form',
  template: `
    <ng-template #textField let-config>
      <label>{{ config.label }}</label>
      <input type="text" [name]="config.name">
    </ng-template>

    <ng-template #selectField let-config>
      <label>{{ config.label }}</label>
      <select [name]="config.name">
        @for (option of config.options; track option) {
          <option>{{ option }}</option>
        }
      </select>
    </ng-template>

    <ng-template #checkboxField let-config>
      <label>
        <input type="checkbox" [name]="config.name">
        {{ config.label }}
      </label>
    </ng-template>

    <form #formContainer></form>
  `
})
export class DynamicFormComponent {
  @ViewChild('textField') textTemplate!: TemplateRef<any>;
  @ViewChild('selectField') selectTemplate!: TemplateRef<any>;
  @ViewChild('checkboxField') checkboxTemplate!: TemplateRef<any>;
  @ViewChild('formContainer', { read: ViewContainerRef })
  formContainer!: ViewContainerRef;

  fields: FieldConfig[] = [
    { type: 'text', label: '名前', name: 'name' },
    { type: 'select', label: '国', name: 'country',
      options: ['日本', 'アメリカ', 'イギリス'] },
    { type: 'checkbox', label: '利用規約に同意', name: 'agree' }
  ];

  ngAfterViewInit() {
    this.buildForm();
  }

  buildForm() {
    this.fields.forEach(field => {
      const template = this.getFieldTemplate(field.type);
      this.formContainer.createEmbeddedView(template, { $implicit: field });
    });
  }

  private getFieldTemplate(type: string): TemplateRef<any> {
    switch (type) {
      case 'text': return this.textTemplate;
      case 'select': return this.selectTemplate;
      case 'checkbox': return this.checkboxTemplate;
      default: return this.textTemplate;
    }
  }
}
```

## ベストプラクティス

### コンテキストの型定義
```typescript
interface TemplateContext {
  $implicit: string;
  index: number;
  count: number;
}

@ViewChild('template')
template!: TemplateRef<TemplateContext>;

insertTemplate() {
  this.container.createEmbeddedView(this.template, {
    $implicit: 'value',
    index: 0,
    count: 10
  });
}
```

### テンプレート参照の管理
```typescript
// ✅ EmbeddedViewRef を保持
private viewRef?: EmbeddedViewRef<any>;

insertTemplate() {
  this.viewRef = this.container.createEmbeddedView(this.template);
}

ngOnDestroy() {
  this.viewRef?.destroy();
}
```

### 条件によるテンプレート選択
```typescript
getTemplate(condition: string): TemplateRef<any> {
  const templateMap = new Map([
    ['A', this.templateA],
    ['B', this.templateB],
    ['C', this.templateC]
  ]);
  return templateMap.get(condition) || this.defaultTemplate;
}
```

## 注意点

### コンテキストの$implicit
`let-variable`のように変数名だけ指定した場合、`$implicit`プロパティの値が割り当てられます。

### メモリ管理
createEmbeddedView()で作成したビューは、不要になったら`destroy()`またはコンテナの`clear()`で削除してください。

### 変更検知
テンプレートコンテキストの値を変更しても、自動的には反映されません。必要に応じて`markForCheck()`を呼び出してください。

### テンプレート参照のタイミング
`@ViewChild`で取得したTemplateRefは、`ngAfterViewInit()`以降でないと利用できません。

## 関連技術
- **TemplateRef**: テンプレート参照
- **ViewContainerRef**: コンテナ管理
- **EmbeddedViewRef**: 埋め込みビュー参照
- **ng-template**: テンプレート定義
- **ngTemplateOutlet**: テンプレートアウトレット
- **構造ディレクティブ**: カスタムディレクティブ
