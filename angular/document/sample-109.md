# #109 「@Output() エイリアス指定」

## 概要
Angular v20における@Output()でのエイリアス指定を学びます。EventEmitterのプロパティ名を変更し、より直感的で保守性の高いコンポーネントAPIを実現する方法について解説します。

## 学習目標
- @Output()エイリアス指定の方法を理解する
- コンポーネントAPIの設計を習得する
- 保守性の高いイベント名の命名方法を身につける

## 📺 画面表示用コード

```typescript
// エイリアス指定の基本
@Component({
  selector: 'app-alias-output',
  standalone: true,
  template: `
    <div class="alias-output">
      <button (click)="save()">保存</button>
      <button (click)="cancel()">キャンセル</button>
    </div>
  `
})
export class AliasOutputComponent {
  @Output('onSave') saveEvent = new EventEmitter<void>();
  @Output('onCancel') cancelEvent = new EventEmitter<void>();
  
  save() {
    this.saveEvent.emit();
  }
  
  cancel() {
    this.cancelEvent.emit();
  }
}
```

```html
<!-- 親コンポーネントでの使用 -->
<app-alias-output 
  (onSave)="handleSave()" 
  (onCancel)="handleCancel()">
</app-alias-output>
```

```typescript
// 親でのイベント処理
export class ParentComponent {
  handleSave() {
    console.log('保存処理');
  }
  
  handleCancel() {
    console.log('キャンセル処理');
  }
}
```

## 技術ポイント

### 1. エイリアス指定の基本構文
```typescript
// 基本的なエイリアス指定
@Output('customEventName') internalPropertyName = new EventEmitter<T>();

// 複数のエイリアス指定
@Output('onUserClick') userClickEvent = new EventEmitter<UserData>();
@Output('onUserHover') userHoverEvent = new EventEmitter<UserData>();
```

### 2. エイリアスの利点
- **直感的な命名**: 外部から見て分かりやすい名前
- **内部実装の隠蔽**: 内部プロパティ名と外部API名の分離
- **後方互換性**: 内部実装変更時の外部API維持

### 3. 命名規則
- **on接頭辞**: イベントハンドラーを示す
- **動詞 + 名詞**: 動作を明確に表現
- **一貫性**: プロジェクト全体での統一

## 実践的な活用例

### 1. フォームコンポーネントのエイリアス指定
```typescript
// form-with-aliases.component.ts
@Component({
  selector: 'app-form-with-aliases',
  standalone: true,
  template: `
    <div class="form-with-aliases">
      <h3>{{title}}</h3>
      
      <form (ngSubmit)="onSubmit()">
        <div class="form-group">
          <label>名前:</label>
          <input [(ngModel)]="formData.name" name="name" required>
        </div>
        
        <div class="form-group">
          <label>メール:</label>
          <input [(ngModel)]="formData.email" name="email" type="email" required>
        </div>
        
        <div class="form-actions">
          <button type="submit">送信</button>
          <button type="button" (click)="onCancel()">キャンセル</button>
          <button type="button" (click)="onReset()">リセット</button>
          <button type="button" (click)="onValidate()">検証</button>
        </div>
      </form>
    </div>
  `,
  imports: [FormsModule]
})
export class FormWithAliasesComponent {
  @Input() title: string = 'フォーム';
  
  // エイリアス指定で直感的なイベント名を提供
  @Output('onFormSubmit') formSubmitEvent = new EventEmitter<any>();
  @Output('onFormCancel') formCancelEvent = new EventEmitter<void>();
  @Output('onFormReset') formResetEvent = new EventEmitter<void>();
  @Output('onFormValidate') formValidateEvent = new EventEmitter<any>();
  
  formData = {
    name: '',
    email: ''
  };
  
  onSubmit() {
    this.formSubmitEvent.emit(this.formData);
  }
  
  onCancel() {
    this.formCancelEvent.emit();
  }
  
  onReset() {
    this.formData = { name: '', email: '' };
    this.formResetEvent.emit();
  }
  
  onValidate() {
    const validation = this.validateForm();
    this.formValidateEvent.emit({
      isValid: validation.isValid,
      errors: validation.errors,
      formData: this.formData
    });
  }
  
  private validateForm() {
    const errors: string[] = [];
    
    if (!this.formData.name.trim()) {
      errors.push('名前は必須です');
    }
    
    if (!this.formData.email.trim()) {
      errors.push('メールアドレスは必須です');
    } else if (!this.isValidEmail(this.formData.email)) {
      errors.push('有効なメールアドレスを入力してください');
    }
    
    return {
      isValid: errors.length === 0,
      errors
    };
  }
  
  private isValidEmail(email: string): boolean {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
  }
}
```

### 2. データテーブルのエイリアス指定
```typescript
// data-table-with-aliases.component.ts
@Component({
  selector: 'app-data-table-with-aliases',
  standalone: true,
  template: `
    <div class="data-table">
      <h3>{{title}}</h3>
      
      <div class="table-controls">
        <input 
          [(ngModel)]="searchTerm" 
          placeholder="検索..."
          (input)="onSearch()">
        <select [(ngModel)]="sortBy" (change)="onSort()">
          <option value="name">名前順</option>
          <option value="date">日付順</option>
          <option value="value">値順</option>
        </select>
      </div>
      
      <table>
        <thead>
          <tr>
            <th *ngFor="let column of columns">{{column.title}}</th>
            <th>アクション</th>
          </tr>
        </thead>
        <tbody>
          <tr 
            *ngFor="let row of filteredData; let i = index"
            (click)="onRowSelect(row, i)"
            [class.selected]="selectedRowIndex === i">
            <td *ngFor="let column of columns">{{row[column.key]}}</td>
            <td>
              <button (click)="onRowEdit(row, i); $event.stopPropagation()">編集</button>
              <button (click)="onRowDelete(row, i); $event.stopPropagation()">削除</button>
            </td>
          </tr>
        </tbody>
      </table>
      
      <div class="pagination">
        <button 
          *ngFor="let page of pageNumbers" 
          (click)="onPageChange(page)"
          [class.active]="page === currentPage">
          {{page}}
        </button>
      </div>
    </div>
  `,
  imports: [FormsModule]
})
export class DataTableWithAliasesComponent {
  @Input() title: string = 'データテーブル';
  @Input() data: any[] = [];
  @Input() columns: Array<{ key: string; title: string }> = [];
  
  // テーブル操作のエイリアス指定
  @Output('onRowSelect') rowSelectEvent = new EventEmitter<{row: any, index: number}>();
  @Output('onRowEdit') rowEditEvent = new EventEmitter<{row: any, index: number}>();
  @Output('onRowDelete') rowDeleteEvent = new EventEmitter<{row: any, index: number}>();
  @Output('onSearch') searchEvent = new EventEmitter<string>();
  @Output('onSort') sortEvent = new EventEmitter<string>();
  @Output('onPageChange') pageChangeEvent = new EventEmitter<number>();
  
  searchTerm: string = '';
  sortBy: string = 'name';
  selectedRowIndex: number = -1;
  currentPage: number = 1;
  itemsPerPage: number = 10;
  
  get filteredData(): any[] {
    let result = [...this.data];
    
    if (this.searchTerm) {
      result = result.filter(row =>
        this.columns.some(column =>
          String(row[column.key]).toLowerCase().includes(this.searchTerm.toLowerCase())
        )
      );
    }
    
    result.sort((a, b) => {
      const aVal = a[this.sortBy];
      const bVal = b[this.sortBy];
      
      if (aVal < bVal) return -1;
      if (aVal > bVal) return 1;
      return 0;
    });
    
    const start = (this.currentPage - 1) * this.itemsPerPage;
    return result.slice(start, start + this.itemsPerPage);
  }
  
  get pageNumbers(): number[] {
    const totalPages = Math.ceil(this.data.length / this.itemsPerPage);
    return Array.from({ length: totalPages }, (_, i) => i + 1);
  }
  
  onRowSelect(row: any, index: number) {
    this.selectedRowIndex = index;
    this.rowSelectEvent.emit({ row, index });
  }
  
  onRowEdit(row: any, index: number) {
    this.rowEditEvent.emit({ row, index });
  }
  
  onRowDelete(row: any, index: number) {
    this.rowDeleteEvent.emit({ row, index });
  }
  
  onSearch() {
    this.searchEvent.emit(this.searchTerm);
  }
  
  onSort() {
    this.sortEvent.emit(this.sortBy);
  }
  
  onPageChange(page: number) {
    this.currentPage = page;
    this.pageChangeEvent.emit(page);
  }
}
```

### 3. モーダルコンポーネントのエイリアス指定
```typescript
// modal-with-aliases.component.ts
@Component({
  selector: 'app-modal-with-aliases',
  standalone: true,
  template: `
    <div class="modal-overlay" *ngIf="isVisible" (click)="onOverlayClick($event)">
      <div class="modal-content" (click)="$event.stopPropagation()">
        <div class="modal-header">
          <h3>{{title}}</h3>
          <button (click)="onClose()" class="close-button">×</button>
        </div>
        
        <div class="modal-body">
          <ng-content></ng-content>
        </div>
        
        <div class="modal-footer">
          <button (click)="onConfirm()" [disabled]="!canConfirm">確認</button>
          <button (click)="onCancel()">キャンセル</button>
        </div>
      </div>
    </div>
  `
})
export class ModalWithAliasesComponent {
  @Input() title: string = 'モーダル';
  @Input() isVisible: boolean = false;
  @Input() canConfirm: boolean = true;
  
  // モーダル操作のエイリアス指定
  @Output('onModalConfirm') confirmEvent = new EventEmitter<void>();
  @Output('onModalCancel') cancelEvent = new EventEmitter<void>();
  @Output('onModalClose') closeEvent = new EventEmitter<void>();
  @Output('onModalShow') showEvent = new EventEmitter<void>();
  @Output('onModalHide') hideEvent = new EventEmitter<void>();
  
  onConfirm() {
    if (this.canConfirm) {
      this.confirmEvent.emit();
      this.closeModal();
    }
  }
  
  onCancel() {
    this.cancelEvent.emit();
    this.closeModal();
  }
  
  onClose() {
    this.closeEvent.emit();
    this.closeModal();
  }
  
  onOverlayClick(event: MouseEvent) {
    if (event.target === event.currentTarget) {
      this.onClose();
    }
  }
  
  private closeModal() {
    this.hideEvent.emit();
  }
  
  // モーダル表示時のイベント発火
  ngOnChanges(changes: SimpleChanges) {
    if (changes['isVisible']) {
      if (changes['isVisible'].currentValue) {
        this.showEvent.emit();
      } else {
        this.hideEvent.emit();
      }
    }
  }
}
```

### 4. カスタムボタンコンポーネントのエイリアス指定
```typescript
// custom-button-with-aliases.component.ts
@Component({
  selector: 'app-custom-button-with-aliases',
  standalone: true,
  template: `
    <button 
      [class]="buttonClasses"
      [disabled]="disabled"
      (click)="onClick()"
      (mouseenter)="onMouseEnter()"
      (mouseleave)="onMouseLeave()"
      (focus)="onFocus()"
      (blur)="onBlur()">
      <span *ngIf="loading" class="spinner"></span>
      {{buttonText}}
    </button>
  `
})
export class CustomButtonWithAliasesComponent {
  @Input() text: string = 'ボタン';
  @Input() variant: 'primary' | 'secondary' | 'danger' | 'success' = 'primary';
  @Input() size: 'small' | 'medium' | 'large' = 'medium';
  @Input() disabled: boolean = false;
  @Input() loading: boolean = false;
  @Input() fullWidth: boolean = false;
  
  // ボタン操作のエイリアス指定
  @Output('onButtonClick') clickEvent = new EventEmitter<MouseEvent>();
  @Output('onButtonHover') hoverEvent = new EventEmitter<boolean>();
  @Output('onButtonFocus') focusEvent = new EventEmitter<FocusEvent>();
  @Output('onButtonBlur') blurEvent = new EventEmitter<FocusEvent>();
  
  get buttonText(): string {
    return this.loading ? '処理中...' : this.text;
  }
  
  get buttonClasses(): string {
    const classes = [
      'custom-button',
      `button-${this.variant}`,
      `button-${this.size}`
    ];
    
    if (this.disabled) classes.push('button-disabled');
    if (this.loading) classes.push('button-loading');
    if (this.fullWidth) classes.push('button-full-width');
    
    return classes.join(' ');
  }
  
  onClick() {
    if (!this.disabled && !this.loading) {
      this.clickEvent.emit();
    }
  }
  
  onMouseEnter() {
    this.hoverEvent.emit(true);
  }
  
  onMouseLeave() {
    this.hoverEvent.emit(false);
  }
  
  onFocus() {
    this.focusEvent.emit();
  }
  
  onBlur() {
    this.blurEvent.emit();
  }
}
```

### 5. 親コンポーネントでの使用例
```typescript
// parent-component-usage.component.ts
@Component({
  selector: 'app-parent-component-usage',
  standalone: true,
  imports: [FormWithAliasesComponent, DataTableWithAliasesComponent, ModalWithAliasesComponent, CustomButtonWithAliasesComponent],
  template: `
    <div class="parent-component">
      <h2>エイリアス指定の使用例</h2>
      
      <!-- フォームコンポーネント -->
      <app-form-with-aliases
        title="ユーザー登録フォーム"
        (onFormSubmit)="handleFormSubmit($event)"
        (onFormCancel)="handleFormCancel()"
        (onFormReset)="handleFormReset()"
        (onFormValidate)="handleFormValidate($event)">
      </app-form-with-aliases>
      
      <!-- データテーブルコンポーネント -->
      <app-data-table-with-aliases
        title="ユーザー一覧"
        [data]="userData"
        [columns]="tableColumns"
        (onRowSelect)="handleRowSelect($event)"
        (onRowEdit)="handleRowEdit($event)"
        (onRowDelete)="handleRowDelete($event)"
        (onSearch)="handleSearch($event)"
        (onSort)="handleSort($event)"
        (onPageChange)="handlePageChange($event)">
      </app-data-table-with-aliases>
      
      <!-- モーダルコンポーネント -->
      <app-modal-with-aliases
        title="確認ダイアログ"
        [isVisible]="showModal"
        [canConfirm]="true"
        (onModalConfirm)="handleModalConfirm()"
        (onModalCancel)="handleModalCancel()"
        (onModalClose)="handleModalClose()"
        (onModalShow)="handleModalShow()"
        (onModalHide)="handleModalHide()">
        <p>この操作を実行しますか？</p>
      </app-modal-with-aliases>
      
      <!-- カスタムボタンコンポーネント -->
      <app-custom-button-with-aliases
        text="保存"
        variant="primary"
        size="medium"
        [loading]="isSaving"
        (onButtonClick)="handleSave()"
        (onButtonHover)="handleButtonHover($event)"
        (onButtonFocus)="handleButtonFocus()"
        (onButtonBlur)="handleButtonBlur()">
      </app-custom-button-with-aliases>
    </div>
  `
})
export class ParentComponentUsageComponent {
  showModal = false;
  isSaving = false;
  userData = [
    { id: 1, name: '田中太郎', email: 'tanaka@example.com' },
    { id: 2, name: '佐藤花子', email: 'sato@example.com' }
  ];
  
  tableColumns = [
    { key: 'name', title: '名前' },
    { key: 'email', title: 'メール' }
  ];
  
  // フォームイベントハンドラー
  handleFormSubmit(formData: any) {
    console.log('フォーム送信:', formData);
    this.isSaving = true;
    
    // 保存処理のシミュレーション
    setTimeout(() => {
      this.isSaving = false;
      console.log('保存完了');
    }, 2000);
  }
  
  handleFormCancel() {
    console.log('フォームキャンセル');
  }
  
  handleFormReset() {
    console.log('フォームリセット');
  }
  
  handleFormValidate(validation: any) {
    console.log('フォーム検証:', validation);
  }
  
  // テーブルイベントハンドラー
  handleRowSelect(event: {row: any, index: number}) {
    console.log('行選択:', event);
  }
  
  handleRowEdit(event: {row: any, index: number}) {
    console.log('行編集:', event);
  }
  
  handleRowDelete(event: {row: any, index: number}) {
    console.log('行削除:', event);
    this.showModal = true;
  }
  
  handleSearch(searchTerm: string) {
    console.log('検索:', searchTerm);
  }
  
  handleSort(sortBy: string) {
    console.log('ソート:', sortBy);
  }
  
  handlePageChange(page: number) {
    console.log('ページ変更:', page);
  }
  
  // モーダルイベントハンドラー
  handleModalConfirm() {
    console.log('モーダル確認');
    this.showModal = false;
  }
  
  handleModalCancel() {
    console.log('モーダルキャンセル');
    this.showModal = false;
  }
  
  handleModalClose() {
    console.log('モーダル閉じる');
    this.showModal = false;
  }
  
  handleModalShow() {
    console.log('モーダル表示');
  }
  
  handleModalHide() {
    console.log('モーダル非表示');
  }
  
  // ボタンイベントハンドラー
  handleSave() {
    console.log('保存ボタンクリック');
    this.isSaving = true;
    
    setTimeout(() => {
      this.isSaving = false;
    }, 2000);
  }
  
  handleButtonHover(isHovering: boolean) {
    console.log('ボタンホバー:', isHovering);
  }
  
  handleButtonFocus() {
    console.log('ボタンフォーカス');
  }
  
  handleButtonBlur() {
    console.log('ボタンブラー');
  }
}
```

## ベストプラクティス

1. **直感的な命名**: 外部から見て分かりやすいイベント名
2. **一貫性**: プロジェクト全体での統一された命名規則
3. **on接頭辞**: イベントハンドラーを示す接頭辞の使用
4. **動詞 + 名詞**: 動作を明確に表現する命名

## 注意点

- エイリアス名は外部APIとして公開されるため慎重に設計
- 内部プロパティ名とエイリアス名の関係を明確に文書化
- 後方互換性を考慮したエイリアス名の変更

## 関連技術
- EventEmitter
- コンポーネントAPI設計
- 命名規則
- 保守性
