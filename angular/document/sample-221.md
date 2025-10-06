# #221 「Dynamic Components とは?」

## 概要
Dynamic Componentsは、実行時にプログラム的にコンポーネントを生成・挿入する機能です。テンプレート内に静的に記述するのではなく、TypeScriptコードから動的にコンポーネントのインスタンスを作成できます。

## 学習目標
- Dynamic Componentsの概念を理解する
- 動的コンポーネント生成が必要な場面を判断できる
- 静的コンポーネントとの違いを説明できる

## 技術ポイント
- **実行時生成**: テンプレートに書かずにコードから生成
- **柔軟なUI構築**: ユーザー操作に応じた動的なUI変更
- **ViewContainerRef**: コンポーネントを挿入するコンテナ

## 📺 画面表示用コード

### 静的コンポーネント（従来）
```typescript
// テンプレートに固定で記述
<app-alert [message]="errorMessage"></app-alert>
```

### Dynamic Component（動的生成）
```typescript
// TypeScriptから動的に生成
const componentRef = viewContainer.createComponent(AlertComponent);
componentRef.setInput('message', 'エラーが発生しました');
```

### 使用例：モーダルの動的生成
```typescript
openModal() {
  const modalRef = this.viewContainer.createComponent(ModalComponent);
  modalRef.setInput('title', '確認');
  modalRef.setInput('content', '本当に削除しますか?');
}
```

## 実践的な活用例

### モーダルダイアログシステム
```typescript
@Injectable()
export class ModalService {
  private viewContainer = inject(ViewContainerRef);

  open(component: Type<any>, data?: any): ComponentRef<any> {
    const componentRef = this.viewContainer.createComponent(component);
    if (data) {
      Object.entries(data).forEach(([key, value]) => {
        componentRef.setInput(key, value);
      });
    }
    return componentRef;
  }
}
```

### タブの動的追加
```typescript
@Component({
  template: `
    <button (click)="addTab()">タブを追加</button>
    <div #tabContainer></div>
  `
})
export class TabContainerComponent {
  @ViewChild('tabContainer', { read: ViewContainerRef })
  container!: ViewContainerRef;

  addTab() {
    const tabRef = this.container.createComponent(TabComponent);
    tabRef.setInput('title', `タブ ${this.container.length}`);
  }
}
```

### 通知システム
```typescript
@Injectable()
export class NotificationService {
  private container = inject(ViewContainerRef);

  showNotification(message: string, type: 'success' | 'error') {
    const notificationRef = this.container.createComponent(NotificationComponent);
    notificationRef.setInput('message', message);
    notificationRef.setInput('type', type);

    // 3秒後に自動削除
    setTimeout(() => notificationRef.destroy(), 3000);
  }
}
```

## ベストプラクティス

### 適切な使用場面の判断
```typescript
// ✅ Dynamic Components が適している場面
// - モーダル、ダイアログ、トースト通知
// - ユーザー操作で追加/削除されるUI要素
// - プラグインシステム、拡張可能なUI

// ❌ 不要な場面（静的コンポーネントで十分）
// - 固定のレイアウト要素
// - 常に表示されるコンポーネント
// - *ngIf や @if で十分な条件表示
```

### メモリ管理
```typescript
export class DynamicHostComponent implements OnDestroy {
  private componentRefs: ComponentRef<any>[] = [];

  createComponent(component: Type<any>) {
    const ref = this.container.createComponent(component);
    this.componentRefs.push(ref);
    return ref;
  }

  ngOnDestroy() {
    // コンポーネント破棄時に全ての動的コンポーネントを削除
    this.componentRefs.forEach(ref => ref.destroy());
  }
}
```

### 型安全な実装
```typescript
interface ModalData {
  title: string;
  content: string;
}

openTypedModal(data: ModalData) {
  const modalRef = this.container.createComponent(ModalComponent);
  modalRef.setInput('title', data.title);
  modalRef.setInput('content', data.content);
  return modalRef;
}
```

## 注意点

### メモリリーク防止
動的に生成したコンポーネントは、不要になったら必ず`destroy()`を呼び出してメモリリークを防ぎます。

### パフォーマンスへの影響
頻繁に生成・削除を繰り返すとパフォーマンスに影響する可能性があります。必要な場面でのみ使用しましょう。

### テンプレート参照の制限
動的に生成されたコンポーネントは、親コンポーネントのテンプレート内には存在しないため、`@ViewChild`などでは参照できません。

### Change Detection
動的コンポーネントの変更検知は自動で行われますが、必要に応じて`ChangeDetectorRef.detectChanges()`を呼び出す場合があります。

## 関連技術
- **ViewContainerRef**: コンポーネント挿入先の管理
- **ComponentRef**: 生成されたコンポーネントの参照
- **Injector**: 依存性注入のカスタマイズ
- **ngTemplateOutlet**: テンプレートの動的表示（軽量な代替手段）
- **Portal (CDK)**: より高度な動的コンテンツ管理
