# #095 「@Input() エイリアス指定」

## 概要
Angular v20における@Input()でのエイリアス指定を学びます。外部APIと内部実装を分離し、より柔軟で保守性の高いコンポーネントAPIを実現する方法について解説します。

## 学習目標
- エイリアス指定の基本構文を理解する
- エイリアスの使用場面とメリットを把握する
- 適切なエイリアス命名規則を習得する

## 📺 画面表示用コード

```typescript
// エイリアス指定の基本
@Component({
  selector: 'app-alias-example',
  standalone: true,
  template: `<p>{{internalName}}</p>`
})
export class AliasExampleComponent {
  @Input('external-name') internalName: string = '';
}
```

```html
<!-- 親コンポーネントでの使用 -->
<app-alias-example [external-name]="'エイリアス名'"></app-alias-example>
```

```typescript
// 複数のエイリアス指定
export class MultipleAliasComponent {
  @Input('user-data') userData: User = {};
  @Input('config-options') configOptions: Config = {};
  @Input('event-handlers') eventHandlers: EventHandlers = {};
}
```

## 技術ポイント

### 1. エイリアス指定の基本構文
```typescript
@Input('external-name') internalName: Type;
```
- `'external-name'`: 外部で使用される名前（親コンポーネントで使用）
- `internalName`: 内部で使用される名前（子コンポーネント内で使用）

### 2. エイリアスの使用場面
- **APIの一貫性**: 外部APIの命名規則を統一
- **内部実装の変更**: 内部実装を変更しても外部APIを維持
- **レガシー対応**: 既存のAPIとの互換性を保つ
- **可読性向上**: より分かりやすい外部API名を使用

### 3. エイリアスの命名規則
- **ケバブケース**: HTML属性では`kebab-case`を使用
- **キャメルケース**: TypeScriptプロパティでは`camelCase`を使用
- **意味のある名前**: 外部API名は用途が明確になるように命名

## 実践的な活用例

### 1. データテーブルコンポーネントのエイリアス
```typescript
// data-table.component.ts
@Component({
  selector: 'app-data-table',
  standalone: true,
  template: `
    <table>
      <thead>
        <tr>
          <th *ngFor="let column of tableColumns">{{column.title}}</th>
        </tr>
      </thead>
      <tbody>
        <tr *ngFor="let row of tableData">
          <td *ngFor="let column of tableColumns">
            {{row[column.key]}}
          </td>
        </tr>
      </tbody>
    </table>
  `
})
export class DataTableComponent {
  // エイリアスを使用してAPIの一貫性を保持
  @Input('table-data') tableData: any[] = [];
  @Input('table-columns') tableColumns: TableColumn[] = [];
  @Input('table-config') tableConfig: TableConfig = {
    sortable: true,
    filterable: false,
    pageSize: 10
  };
}
```

### 2. フォームコンポーネントのエイリアス
```typescript
// form-builder.component.ts
@Component({
  selector: 'app-form-builder',
  standalone: true,
  template: `
    <form [formGroup]="form">
      <div *ngFor="let field of formFields" class="form-field">
        <label [for]="field.id">{{field.label}}</label>
        <input 
          [id]="field.id"
          [type]="field.type"
          [formControlName]="field.name"
          [placeholder]="field.placeholder">
      </div>
      <button type="submit" (click)="onSubmit()">送信</button>
    </form>
  `
})
export class FormBuilderComponent {
  @Input('form-fields') formFields: FormField[] = [];
  @Input('form-validation') formValidation: ValidationConfig = {};
  @Input('submit-handler') submitHandler: (data: any) => void = () => {};
  
  form: FormGroup;
  
  ngOnInit() {
    this.buildForm();
  }
  
  private buildForm() {
    const controls: any = {};
    this.formFields.forEach(field => {
      controls[field.name] = new FormControl('', field.validators || []);
    });
    this.form = new FormGroup(controls);
  }
  
  onSubmit() {
    if (this.form.valid) {
      this.submitHandler(this.form.value);
    }
  }
}
```

### 3. チャートコンポーネントのエイリアス
```typescript
// chart.component.ts
@Component({
  selector: 'app-chart',
  standalone: true,
  template: `
    <div class="chart-container">
      <canvas #chartCanvas></canvas>
    </div>
  `
})
export class ChartComponent implements AfterViewInit {
  @ViewChild('chartCanvas') canvas?: ElementRef<HTMLCanvasElement>;
  
  @Input('chart-data') chartData: ChartData[] = [];
  @Input('chart-options') chartOptions: ChartOptions = {};
  @Input('chart-type') chartType: 'line' | 'bar' | 'pie' = 'line';
  @Input('update-trigger') updateTrigger: any;
  
  ngAfterViewInit() {
    this.renderChart();
  }
  
  ngOnChanges() {
    if (this.canvas) {
      this.renderChart();
    }
  }
  
  private renderChart() {
    // チャートの描画処理
    if (this.canvas) {
      const ctx = this.canvas.nativeElement.getContext('2d');
      // チャートライブラリを使用して描画
    }
  }
}
```

### 4. モーダルコンポーネントのエイリアス
```typescript
// modal.component.ts
@Component({
  selector: 'app-modal',
  standalone: true,
  template: `
    <div *ngIf="isVisible" class="modal-overlay" (click)="onClose()">
      <div class="modal-content" (click)="$event.stopPropagation()">
        <div class="modal-header">
          <h3>{{modalTitle}}</h3>
          <button (click)="onClose()">×</button>
        </div>
        <div class="modal-body">
          <ng-content></ng-content>
        </div>
        <div class="modal-footer">
          <button (click)="onConfirm()">確認</button>
          <button (click)="onCancel()">キャンセル</button>
        </div>
      </div>
    </div>
  `
})
export class ModalComponent {
  @Input('modal-title') modalTitle: string = 'モーダル';
  @Input('modal-visible') isVisible: boolean = false;
  @Input('modal-data') modalData: any = {};
  @Input('confirm-text') confirmText: string = '確認';
  @Input('cancel-text') cancelText: string = 'キャンセル';
  
  @Output('modal-close') close = new EventEmitter<void>();
  @Output('modal-confirm') confirm = new EventEmitter<any>();
  @Output('modal-cancel') cancel = new EventEmitter<void>();
  
  onClose() {
    this.close.emit();
  }
  
  onConfirm() {
    this.confirm.emit(this.modalData);
  }
  
  onCancel() {
    this.cancel.emit();
  }
}
```

## ベストプラクティス

1. **一貫性**: プロジェクト全体でエイリアスの命名規則を統一
2. **意味のある名前**: 外部API名は用途が明確になるように命名
3. **ドキュメント**: エイリアスの対応関係を明確に文書化
4. **段階的移行**: 既存APIから新しいAPIへの段階的な移行を考慮

## 注意点

- エイリアスは外部APIと内部実装の分離に使用する
- 過度なエイリアス使用はコードの可読性を損なう可能性がある
- エイリアス名はHTML属性として使用されるため、有効な属性名である必要がある

## 関連技術
- プロパティバインディング
- コンポーネントAPI設計
- 命名規則
- レガシー対応
