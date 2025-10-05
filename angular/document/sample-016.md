# #016 「Component の export と再利用」台本

四国めたん「Component の export と再利用について解説します！」
ずんだもん「exportって何をするの？」
四国めたん「Componentを他のファイルから使用できるように公開する機能です」
ずんだもん「どんな時に使うの？」
四国めたん「共有Componentや、複数の場所で使用するComponentを作成する時です」
ずんだもん「再利用のメリットは？」
四国めたん「コードの重複を避け、保守性と一貫性を向上させます」

---

## 📺 画面表示用コード

// 基本的なexport
```typescript
// button.component.ts
import { Component } from '@angular/core';

@Component({
  selector: 'app-button',
  standalone: true,
  template: `
    <button class="btn" [class]="buttonClass">
      <ng-content></ng-content>
    </button>
  `,
  styles: [`
    .btn {
      padding: 8px 16px;
      border: none;
      border-radius: 4px;
      cursor: pointer;
    }
    .btn-primary { background-color: #007bff; color: white; }
    .btn-secondary { background-color: #6c757d; color: white; }
  `]
})
export class ButtonComponent {  // exportで公開
  @Input() buttonClass = 'btn-primary';
}
```

// 他のComponentでインポートして使用
```typescript
// user-form.component.ts
import { Component } from '@angular/core';
import { ButtonComponent } from './button/button.component';

@Component({
  selector: 'app-user-form',
  standalone: true,
  imports: [ButtonComponent],
  template: `
    <form>
      <input placeholder="名前">
      <app-button buttonClass="btn-primary">送信</app-button>
      <app-button buttonClass="btn-secondary">キャンセル</app-button>
    </form>
  `
})
export class UserFormComponent {
  // ButtonComponentを再利用
}
```

// 複数のComponentをexport
```typescript
// ui-components/index.ts
export { ButtonComponent } from './button/button.component';
export { CardComponent } from './card/card.component';
export { ModalComponent } from './modal/modal.component';
export { InputComponent } from './input/input.component';

// 使用側
import { 
  ButtonComponent, 
  CardComponent, 
  ModalComponent 
} from './ui-components';
```

// 再利用可能なCardComponent
```typescript
// card.component.ts
import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-card',
  standalone: true,
  template: `
    <div class="card">
      <div class="card-header" *ngIf="title">
        <h3>{{title}}</h3>
      </div>
      <div class="card-body">
        <ng-content></ng-content>
      </div>
      <div class="card-footer" *ngIf="footer">
        {{footer}}
      </div>
    </div>
  `,
  styles: [`
    .card {
      border: 1px solid #ddd;
      border-radius: 8px;
      box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .card-header { padding: 16px; background-color: #f8f9fa; }
    .card-body { padding: 16px; }
    .card-footer { padding: 16px; background-color: #f8f9fa; }
  `]
})
export class CardComponent {
  @Input() title?: string;
  @Input() footer?: string;
}
```

// CardComponentの使用例
```typescript
// product-list.component.ts
import { Component } from '@angular/core';
import { CardComponent } from './card/card.component';

@Component({
  selector: 'app-product-list',
  standalone: true,
  imports: [CardComponent],
  template: `
    <div class="product-list">
      <app-card title="商品1" footer="¥1,000">
        <p>商品1の説明</p>
      </app-card>
      <app-card title="商品2" footer="¥2,000">
        <p>商品2の説明</p>
      </app-card>
    </div>
  `
})
export class ProductListComponent {
  // CardComponentを複数回再利用
}
```

// 共有サービスのexport
```typescript
// shared/services/index.ts
export { UserService } from './user.service';
export { ApiService } from './api.service';
export { StorageService } from './storage.service';

// user.service.ts
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class UserService {
  private users: any[] = [];
  
  getUsers() {
    return this.users;
  }
  
  addUser(user: any) {
    this.users.push(user);
  }
}
```

// 再利用可能なModalComponent
```typescript
// modal.component.ts
import { Component, Input, Output, EventEmitter } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-modal',
  standalone: true,
  imports: [CommonModule],
  template: `
    <div class="modal-overlay" *ngIf="isVisible" (click)="close()">
      <div class="modal-content" (click)="$event.stopPropagation()">
        <div class="modal-header">
          <h2>{{title}}</h2>
          <button class="close-btn" (click)="close()">×</button>
        </div>
        <div class="modal-body">
          <ng-content></ng-content>
        </div>
        <div class="modal-footer">
          <button (click)="close()">キャンセル</button>
          <button (click)="confirm()">確認</button>
        </div>
      </div>
    </div>
  `,
  styles: [`
    .modal-overlay {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background-color: rgba(0,0,0,0.5);
      display: flex;
      justify-content: center;
      align-items: center;
    }
    .modal-content {
      background: white;
      border-radius: 8px;
      max-width: 500px;
      width: 90%;
    }
  `]
})
export class ModalComponent {
  @Input() isVisible = false;
  @Input() title = '';
  @Output() onClose = new EventEmitter<void>();
  @Output() onConfirm = new EventEmitter<void>();
  
  close() {
    this.isVisible = false;
    this.onClose.emit();
  }
  
  confirm() {
    this.onConfirm.emit();
    this.close();
  }
}
```

// ModalComponentの使用例
```typescript
// user-management.component.ts
import { Component } from '@angular/core';
import { ModalComponent } from './modal/modal.component';

@Component({
  selector: 'app-user-management',
  standalone: true,
  imports: [ModalComponent],
  template: `
    <div>
      <button (click)="showModal = true">ユーザー追加</button>
      
      <app-modal 
        [isVisible]="showModal"
        title="ユーザー追加"
        (onClose)="showModal = false"
        (onConfirm)="addUser()">
        <p>新しいユーザーを追加しますか？</p>
      </app-modal>
    </div>
  `
})
export class UserManagementComponent {
  showModal = false;
  
  addUser() {
    console.log('ユーザーを追加しました');
  }
}
```

// 再利用のベストプラクティス
```typescript
// reusable-input.component.ts
import { Component, Input, Output, EventEmitter } from '@angular/core';

@Component({
  selector: 'app-reusable-input',
  standalone: true,
  template: `
    <div class="input-group">
      <label *ngIf="label">{{label}}</label>
      <input 
        [type]="type"
        [placeholder]="placeholder"
        [value]="value"
        (input)="onInput($event)"
        [class.error]="hasError">
      <span *ngIf="hasError" class="error-message">{{errorMessage}}</span>
    </div>
  `,
  styles: [`
    .input-group { margin-bottom: 16px; }
    .error { border-color: red; }
    .error-message { color: red; font-size: 12px; }
  `]
})
export class ReusableInputComponent {
  @Input() label?: string;
  @Input() type = 'text';
  @Input() placeholder = '';
  @Input() value = '';
  @Input() hasError = false;
  @Input() errorMessage = '';
  @Output() valueChange = new EventEmitter<string>();
  
  onInput(event: any) {
    this.value = event.target.value;
    this.valueChange.emit(this.value);
  }
}
```

// 再利用のメリット
```typescript
@Component({
  selector: 'app-benefits',
  standalone: true,
  template: `
    <div>
      <h2>再利用のメリット</h2>
      <ul>
        <li>コードの重複を避ける</li>
        <li>保守性の向上</li>
        <li>一貫性の確保</li>
        <li>開発効率の向上</li>
        <li>テストの簡素化</li>
        <li>デザインシステムの構築</li>
      </ul>
    </div>
  `
})
export class BenefitsComponent {
  // 再利用可能なComponentの設計が重要
}
```
