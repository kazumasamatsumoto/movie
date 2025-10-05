# #045 「(submit) フォーム送信イベント」台本

四国めたん「(submit) フォーム送信イベントについて学びましょう！」
ずんだもん「フォームの送信を制御できるの？」
四国めたん「はい！フォームの送信処理をカスタマイズできます」
ずんだもん「デフォルトの送信を防げるの？」
四国めたん「preventDefault()でデフォルトの送信を防いで、独自の処理を実行できます」
ずんだもん「バリデーションも組み合わせられる？」
四国めたん「はい！送信前にバリデーションを行い、エラーがあれば送信を停止できます」

---

## 📺 画面表示用コード

// 基本的なフォーム送信
```typescript
@Component({
  selector: 'app-submit-basic',
  standalone: true,
  template: `
    <div class="submit-demo">
      <h2>基本的なフォーム送信</h2>
      <form (submit)="onSubmit($event)">
        <input type="text" placeholder="名前" required>
        <button type="submit">送信</button>
      </form>
      <p>送信回数: {{submitCount}}</p>
    </div>
  `,
  styles: [`
    .submit-demo {
      padding: 20px;
    }
    form {
      display: flex;
      gap: 10px;
      margin: 10px 0;
    }
    input, button {
      padding: 8px;
    }
  `]
})
export class SubmitBasicComponent {
  submitCount = 0;
  
  onSubmit(event: Event) {
    event.preventDefault(); // デフォルト送信を防ぐ
    this.submitCount++;
    console.log('フォームが送信されました');
  }
}
```

// バリデーション付きフォーム
```typescript
@Component({
  selector: 'app-validation-form',
  standalone: true,
  imports: [FormsModule],
  template: `
    <div class="validation-form-demo">
      <h2>バリデーション付きフォーム</h2>
      <form (submit)="onSubmit($event)">
        <input [(ngModel)]="name" 
               name="name" 
               placeholder="名前" 
               required>
        <input [(ngModel)]="email" 
               name="email" 
               type="email" 
               placeholder="メールアドレス" 
               required>
        <button type="submit" [disabled]="!isFormValid()">
          送信
        </button>
      </form>
      <p *ngIf="showError" class="error">すべての項目を入力してください</p>
    </div>
  `,
  styles: [`
    .validation-form-demo {
      padding: 20px;
    }
    form {
      display: flex;
      flex-direction: column;
      gap: 10px;
      margin: 10px 0;
    }
    input, button {
      padding: 8px;
    }
    .error {
      color: #dc3545;
    }
  `]
})
export class ValidationFormComponent {
  name = '';
  email = '';
  showError = false;
  
  isFormValid(): boolean {
    return this.name.trim().length > 0 && this.email.trim().length > 0;
  }
  
  onSubmit(event: Event) {
    event.preventDefault();
    
    if (!this.isFormValid()) {
      this.showError = true;
      return;
    }
    
    this.showError = false;
    console.log('フォーム送信:', { name: this.name, email: this.email });
  }
}
```

// 非同期送信フォーム
```typescript
@Component({
  selector: 'app-async-submit',
  standalone: true,
  imports: [FormsModule],
  template: `
    <div class="async-submit-demo">
      <h2>非同期送信フォーム</h2>
      <form (submit)="onSubmit($event)">
        <input [(ngModel)]="message" 
               name="message" 
               placeholder="メッセージ" 
               required>
        <button type="submit" [disabled]="isSubmitting">
          {{isSubmitting ? '送信中...' : '送信'}}
        </button>
      </form>
      <p *ngIf="submitResult" class="result">{{submitResult}}</p>
    </div>
  `,
  styles: [`
    .async-submit-demo {
      padding: 20px;
    }
    form {
      display: flex;
      gap: 10px;
      margin: 10px 0;
    }
    input, button {
      padding: 8px;
    }
    .result {
      color: #28a745;
      font-weight: bold;
    }
  `]
})
export class AsyncSubmitComponent {
  message = '';
  isSubmitting = false;
  submitResult = '';
  
  async onSubmit(event: Event) {
    event.preventDefault();
    
    if (!this.message.trim()) return;
    
    this.isSubmitting = true;
    this.submitResult = '';
    
    try {
      // 模擬的なAPI送信
      await new Promise(resolve => setTimeout(resolve, 2000));
      this.submitResult = '送信が完了しました！';
      this.message = '';
    } catch (error) {
      this.submitResult = '送信に失敗しました';
    } finally {
      this.isSubmitting = false;
    }
  }
}
```
