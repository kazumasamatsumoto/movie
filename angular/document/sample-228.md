# #228 「動的 Component の削除」

## 概要
動的に生成したコンポーネントは、不要になったら適切に削除する必要があります。ComponentRef.destroy()による個別削除、ViewContainerRef.clear()による全削除、remove()によるインデックス指定削除など、状況に応じた削除方法を選択できます。

## 学習目標
- 動的コンポーネントの削除方法を習得する
- メモリリーク防止の重要性を理解する
- 適切な削除タイミングを判断できる

## 技術ポイント
- **destroy()**: ComponentRefからの個別削除
- **clear()**: ViewContainerRef内の全削除
- **remove()**: インデックス指定での削除

## 📺 画面表示用コード

### destroy() での削除
```typescript
const componentRef = this.container.createComponent(AlertComponent);

// 使用後に削除
componentRef.destroy();
```

### clear() での全削除
```typescript
// コンテナ内の全コンポーネントを削除
this.container.clear();
```

### remove() でのインデックス削除
```typescript
// インデックス0のコンポーネントを削除
this.container.remove(0);

// インデックス1のコンポーネントを削除
this.container.remove(1);
```

## 実践的な活用例

### 自動削除通知システム
```typescript
@Injectable()
export class NotificationService {
  private container = inject(ViewContainerRef);

  show(message: string, duration = 3000) {
    const notificationRef = this.container.createComponent(NotificationComponent);
    notificationRef.setInput('message', message);

    // 指定時間後に自動削除
    setTimeout(() => {
      notificationRef.destroy();
      console.log('通知を削除しました');
    }, duration);

    return notificationRef;
  }
}
```

### 参照を保持して削除
```typescript
export class ManagedListComponent {
  private container = inject(ViewContainerRef);
  private items: ComponentRef<ListItemComponent>[] = [];

  addItem(data: any) {
    const itemRef = this.container.createComponent(ListItemComponent);
    itemRef.setInput('data', data);
    this.items.push(itemRef);
  }

  removeItem(index: number) {
    const itemRef = this.items[index];
    if (itemRef) {
      itemRef.destroy();
      this.items.splice(index, 1);
    }
  }

  removeAll() {
    // 全てのアイテムを削除
    this.items.forEach(item => item.destroy());
    this.items = [];
    // または
    // this.container.clear();
  }
}
```

### モーダルの完全な実装
```typescript
@Injectable()
export class ModalService {
  private container = inject(ViewContainerRef);
  private modalRefs: ComponentRef<any>[] = [];

  open<T>(component: Type<T>, data?: any): ComponentRef<T> {
    const modalRef = this.container.createComponent(component);

    if (data) {
      Object.entries(data).forEach(([key, value]) => {
        modalRef.setInput(key, value);
      });
    }

    // クローズイベントを購読
    if ('closed' in modalRef.instance) {
      (modalRef.instance as any).closed.subscribe(() => {
        this.close(modalRef);
      });
    }

    this.modalRefs.push(modalRef);
    return modalRef;
  }

  close(modalRef: ComponentRef<any>) {
    const index = this.modalRefs.indexOf(modalRef);
    if (index !== -1) {
      this.modalRefs.splice(index, 1);
      modalRef.destroy();
    }
  }

  closeAll() {
    this.modalRefs.forEach(ref => ref.destroy());
    this.modalRefs = [];
  }
}
```

### コンポーネント破棄時のクリーンアップ
```typescript
@Component({
  selector: 'app-dynamic-host',
  template: '<ng-container #container></ng-container>'
})
export class DynamicHostComponent implements OnDestroy {
  @ViewChild('container', { read: ViewContainerRef })
  container!: ViewContainerRef;

  private componentRefs: ComponentRef<any>[] = [];

  addComponent(componentType: Type<any>) {
    const ref = this.container.createComponent(componentType);
    this.componentRefs.push(ref);
    return ref;
  }

  ngOnDestroy() {
    // コンポーネント破棄時に全ての動的コンポーネントを削除
    this.componentRefs.forEach(ref => ref.destroy());
    this.componentRefs = [];

    // または ViewContainerRef で一括削除
    // this.container.clear();
  }
}
```

### 条件付き削除
```typescript
export class ConditionalRemovalComponent {
  private container = inject(ViewContainerRef);
  private componentRefs = new Map<string, ComponentRef<any>>();

  add(id: string, component: Type<any>) {
    // 既存のコンポーネントがあれば削除
    this.remove(id);

    const ref = this.container.createComponent(component);
    this.componentRefs.set(id, ref);
  }

  remove(id: string) {
    const ref = this.componentRefs.get(id);
    if (ref) {
      ref.destroy();
      this.componentRefs.delete(id);
    }
  }

  removeAll() {
    this.componentRefs.forEach(ref => ref.destroy());
    this.componentRefs.clear();
  }

  has(id: string): boolean {
    return this.componentRefs.has(id);
  }
}
```

### イベントベースの削除
```typescript
@Component({
  selector: 'app-closable-panel',
  template: `
    <div class="panel">
      <button (click)="close()">閉じる</button>
      <ng-content></ng-content>
    </div>
  `
})
export class ClosablePanelComponent {
  closed = output<void>();

  close() {
    this.closed.emit();
  }
}

export class PanelHostComponent {
  private container = inject(ViewContainerRef);
  private destroyRef = inject(DestroyRef);

  addPanel() {
    const panelRef = this.container.createComponent(ClosablePanelComponent);

    // クローズイベントで削除
    panelRef.instance.closed
      .pipe(takeUntilDestroyed(this.destroyRef))
      .subscribe(() => {
        panelRef.destroy();
      });
  }
}
```

### インデックスベースの削除
```typescript
export class IndexBasedRemovalComponent {
  private container = inject(ViewContainerRef);

  removeAtIndex(index: number) {
    if (index >= 0 && index < this.container.length) {
      this.container.remove(index);
    } else {
      console.error('無効なインデックス:', index);
    }
  }

  removeFirst() {
    if (this.container.length > 0) {
      this.container.remove(0);
    }
  }

  removeLast() {
    const lastIndex = this.container.length - 1;
    if (lastIndex >= 0) {
      this.container.remove(lastIndex);
    }
  }

  getComponentCount(): number {
    return this.container.length;
  }
}
```

## ベストプラクティス

### 削除の確実な実行
```typescript
// ✅ ngOnDestroy で確実に削除
ngOnDestroy() {
  this.componentRefs.forEach(ref => ref.destroy());
}

// ✅ 削除後に参照もクリア
removeComponent(ref: ComponentRef<any>) {
  ref.destroy();
  this.componentRefs = this.componentRefs.filter(r => r !== ref);
}
```

### 削除前のチェック
```typescript
// ✅ 存在確認してから削除
removeIfExists(ref: ComponentRef<any>) {
  if (ref && !ref.hostView.destroyed) {
    ref.destroy();
  }
}

// ✅ インデックス範囲チェック
removeAtIndex(index: number) {
  if (index >= 0 && index < this.container.length) {
    this.container.remove(index);
  }
}
```

### 削除のロギング
```typescript
// デバッグ用のログ付き削除
removeWithLog(ref: ComponentRef<any>, reason: string) {
  console.log(`コンポーネント削除: ${reason}`);
  ref.destroy();
}
```

## 注意点

### メモリリークの防止
動的に生成したコンポーネントは、使用後必ず削除してください。特にループ内での生成や、長時間実行されるアプリケーションでは重要です。

### destroy() の冪等性
すでに破棄されたComponentRefに対して`destroy()`を呼んでもエラーにはなりませんが、推奨されません。

### イベント購読の解除
`destroy()`を呼ぶと、そのコンポーネントのイベントEmitterも停止しますが、親コンポーネント側の購読は明示的に解除する必要があります。

### ViewContainerRef.clear() の影響範囲
`clear()`は、そのコンテナ内の全てのコンポーネントを削除します。部分的な削除が必要な場合は`remove()`や個別の`destroy()`を使用してください。

## 関連技術
- **ComponentRef**: コンポーネント参照
- **ViewContainerRef**: コンテナ管理
- **OnDestroy**: ライフサイクルフック
- **メモリ管理**: リソースの適切な解放
- **DestroyRef**: 破棄イベントの検知
