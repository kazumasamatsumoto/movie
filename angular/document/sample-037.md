# #037 「[disabled] 属性バインディング」台本

四国めたん「[disabled] 属性バインディングについて学びましょう！」
ずんだもん「disabled属性って何？」
四国めたん「フォーム要素を無効化する属性です。ユーザーが操作できない状態にできます」
ずんだもん「どんな場面で使うの？」
四国めたん「バリデーションエラー時、送信中、権限がない場合などです」
ずんだもん「どうやって制御するの？」
四国めたん「プロパティバインディングでtrue/falseを設定します」

---

## 📺 画面表示用コード

// 基本的なdisabled属性
```typescript
@Component({
  selector: 'app-disabled-basic',
  standalone: true,
  template: `
    <div class="disabled-demo">
      <h2>基本的なdisabled属性</h2>
      <button [disabled]="isDisabled">ボタン</button>
      <input [disabled]="isDisabled" placeholder="入力欄">
      <p>状態: {{isDisabled ? '無効' : '有効'}}</p>
      <button (click)="toggle()">切り替え</button>
    </div>
  `,
  styles: [`
    .disabled-demo {
      padding: 20px;
    }
    button, input {
      margin: 5px;
      padding: 8px 16px;
    }
  `]
})
export class DisabledBasicComponent {
  isDisabled = false;
  
  toggle() {
    this.isDisabled = !this.isDisabled;
  }
}
```

// フォームバリデーションでの使用
```typescript
@Component({
  selector: 'app-form-validation',
  standalone: true,
  imports: [FormsModule],
  template: `
    <div class="validation-demo">
      <h2>フォームバリデーションでの使用</h2>
      <form>
        <input [(ngModel)]="email" 
               type="email" 
               name="email"
               placeholder="メールアドレス">
        <button [disabled]="!isFormValid()" 
                (click)="submit()">
          送信
        </button>
      </form>
      <p>有効: {{isFormValid()}}</p>
    </div>
  `,
  styles: [`
    .validation-demo {
      padding: 20px;
    }
    input, button {
      margin: 5px;
      padding: 8px;
    }
  `]
})
export class FormValidationComponent {
  email = '';
  
  isFormValid(): boolean {
    return this.email.includes('@') && this.email.length > 5;
  }
  
  submit() {
    console.log('送信:', this.email);
  }
}
```

// 送信状態での制御
```typescript
@Component({
  selector: 'app-submit-state',
  standalone: true,
  template: `
    <div class="submit-demo">
      <h2>送信状態での制御</h2>
      <button [disabled]="isSubmitting" 
              (click)="handleSubmit()">
        {{isSubmitting ? '送信中...' : '送信'}}
      </button>
      <div *ngIf="isSubmitting" class="loading">
        処理中...
      </div>
    </div>
  `,
  styles: [`
    .submit-demo {
      padding: 20px;
    }
    button {
      padding: 10px 20px;
      margin: 10px;
    }
    .loading {
      color: #007bff;
      font-weight: bold;
    }
  `]
})
export class SubmitStateComponent {
  isSubmitting = false;
  
  async handleSubmit() {
    this.isSubmitting = true;
    
    // 模擬的な非同期処理
    await new Promise(resolve => setTimeout(resolve, 2000));
    
    this.isSubmitting = false;
    alert('送信完了！');
  }
}
```
