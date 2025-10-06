# #226 「動的 Component への入力渡し」

## 概要
動的に生成したコンポーネントへの入力値の受け渡しには、ComponentRef.setInput()メソッドを使用します。v14以降ではこの方法が推奨され、通常の@Input()プロパティだけでなく、Signal入力にも対応しています。

## 学習目標
- setInput()メソッドの使い方を習得する
- instance経由の直接代入との違いを理解する
- Signal入力への対応方法を学ぶ

## 技術ポイント
- **setInput()**: v14以降の推奨方法
- **型安全な入力**: TypeScriptの型チェックが効く
- **Signal対応**: input()、input.required()にも使用可能

## 📺 画面表示用コード

### setInput() の基本
```typescript
const componentRef = this.container.createComponent(AlertComponent);
componentRef.setInput('message', 'エラーが発生しました');
componentRef.setInput('type', 'error');
```

### instance 経由（従来の方法）
```typescript
const componentRef = this.container.createComponent(AlertComponent);
componentRef.instance.message = 'エラーが発生しました';
componentRef.instance.type = 'error';
```

### Signal 入力への対応
```typescript
// コンポーネント定義
export class UserCardComponent {
  user = input.required<User>();
  showDetails = input(false);
}

// 動的生成時
const ref = this.container.createComponent(UserCardComponent);
ref.setInput('user', { id: 1, name: 'John' });
ref.setInput('showDetails', true);
```

## 実践的な活用例

### 通知コンポーネントへの入力
```typescript
interface NotificationData {
  message: string;
  type: 'success' | 'error' | 'warning' | 'info';
  duration?: number;
}

@Injectable()
export class NotificationService {
  private container = inject(ViewContainerRef);

  show(data: NotificationData) {
    const ref = this.container.createComponent(NotificationComponent);

    // 複数の入力値を設定
    ref.setInput('message', data.message);
    ref.setInput('type', data.type);
    ref.setInput('duration', data.duration ?? 3000);

    return ref;
  }
}

// NotificationComponent の定義
@Component({
  selector: 'app-notification',
  template: `
    <div [class]="'notification ' + type()">
      {{ message() }}
    </div>
  `
})
export class NotificationComponent {
  message = input.required<string>();
  type = input<'success' | 'error' | 'warning' | 'info'>('info');
  duration = input<number>(3000);
}
```

### 複雑なオブジェクトの受け渡し
```typescript
interface ModalConfig {
  title: string;
  content: string;
  buttons: Array<{ label: string; action: () => void }>;
  width?: string;
  closable?: boolean;
}

export class ModalService {
  private container = inject(ViewContainerRef);

  open(config: ModalConfig) {
    const modalRef = this.container.createComponent(ModalComponent);

    // 構造化されたデータを渡す
    modalRef.setInput('title', config.title);
    modalRef.setInput('content', config.content);
    modalRef.setInput('buttons', config.buttons);
    modalRef.setInput('width', config.width ?? '500px');
    modalRef.setInput('closable', config.closable ?? true);

    return modalRef;
  }
}
```

### データの動的更新
```typescript
export class LiveUpdateComponent {
  private chartRef?: ComponentRef<ChartComponent>;
  private container = inject(ViewContainerRef);

  createChart() {
    this.chartRef = this.container.createComponent(ChartComponent);
    this.chartRef.setInput('data', this.getInitialData());
  }

  updateChartData(newData: number[]) {
    // 既存のコンポーネントの入力値を更新
    this.chartRef?.setInput('data', newData);
    this.chartRef?.setInput('lastUpdated', new Date());
  }

  private getInitialData(): number[] {
    return [10, 20, 30, 40, 50];
  }
}
```

### ヘルパー関数による入力設定
```typescript
export class DynamicComponentHelper {
  private container = inject(ViewContainerRef);

  createWithInputs<T>(
    component: Type<T>,
    inputs: Record<string, any>
  ): ComponentRef<T> {
    const componentRef = this.container.createComponent(component);

    // オブジェクトから全ての入力値を設定
    Object.entries(inputs).forEach(([key, value]) => {
      componentRef.setInput(key, value);
    });

    return componentRef;
  }
}

// 使用例
this.helper.createWithInputs(UserProfileComponent, {
  userId: 123,
  showAvatar: true,
  editable: false,
  theme: 'dark'
});
```

### 型安全な入力設定
```typescript
// 型定義
interface ComponentInputs<T> {
  [K in keyof T]?: T[K];
}

export class TypeSafeCreator {
  private container = inject(ViewContainerRef);

  create<T>(
    component: Type<T>,
    inputs: ComponentInputs<T>
  ): ComponentRef<T> {
    const ref = this.container.createComponent(component);

    // 型安全に入力値を設定
    (Object.keys(inputs) as Array<keyof T>).forEach(key => {
      ref.setInput(key as string, inputs[key]);
    });

    return ref;
  }
}

// 使用例（型チェックが効く）
this.creator.create(AlertComponent, {
  message: 'Hello',  // ✅ OK
  type: 'error',     // ✅ OK
  // unknownProp: 'value'  // ❌ コンパイルエラー
});
```

### リアクティブな入力更新
```typescript
export class ReactiveInputComponent {
  private componentRef?: ComponentRef<StatusComponent>;
  private container = inject(ViewContainerRef);

  // Signalを使った状態管理
  status = signal<'loading' | 'success' | 'error'>('loading');
  message = signal('処理中...');

  ngOnInit() {
    this.componentRef = this.container.createComponent(StatusComponent);

    // Signalの変更を監視して入力を更新
    effect(() => {
      this.componentRef?.setInput('status', this.status());
      this.componentRef?.setInput('message', this.message());
    });
  }

  updateStatus(newStatus: 'loading' | 'success' | 'error', newMessage: string) {
    this.status.set(newStatus);
    this.message.set(newMessage);
    // effect が自動的に setInput を呼び出す
  }
}
```

## ベストプラクティス

### setInput() を優先
```typescript
// ✅ 推奨: setInput() を使用
const ref = this.container.createComponent(MyComponent);
ref.setInput('title', 'Hello');

// ⚠️ 非推奨: instance 直接アクセス（レガシーコード用）
ref.instance.title = 'Hello';
```

### 必須入力のチェック
```typescript
// コンポーネント定義
export class UserComponent {
  user = input.required<User>();  // 必須
  showAvatar = input(true);        // オプション
}

// 生成時に必須入力を確実に設定
const ref = this.container.createComponent(UserComponent);
ref.setInput('user', userData);  // 必須！
ref.setInput('showAvatar', false);  // オプション
```

### 複数入力の一括設定
```typescript
function setInputs<T>(
  ref: ComponentRef<T>,
  inputs: Record<string, any>
): void {
  Object.entries(inputs).forEach(([key, value]) => {
    ref.setInput(key, value);
  });
}

// 使用
const ref = this.container.createComponent(MyComponent);
setInputs(ref, {
  title: 'Title',
  description: 'Description',
  visible: true
});
```

## 注意点

### 入力プロパティの存在確認
存在しない入力プロパティ名を指定してもエラーにならない場合があります。TypeScriptの型チェックを活用してください。

### タイミングの考慮
`setInput()`は生成直後でも、後からでも呼び出せます。ただし、コンポーネントのライフサイクルフックのタイミングを考慮してください。

### Signal入力の反応性
Signal入力に`setInput()`で値を設定すると、自動的にSignalが更新され、依存する computed や effect が実行されます。

### パフォーマンスへの影響
頻繁に`setInput()`を呼び出すと変更検知が発生します。大量の更新を行う場合は、まとめて設定することを検討してください。

## 関連技術
- **ComponentRef**: コンポーネント参照
- **@Input()**: 入力プロパティデコレータ
- **input()**: Signal入力（v17+）
- **Signal**: リアクティブな状態管理
- **effect()**: Signalの変更監視
