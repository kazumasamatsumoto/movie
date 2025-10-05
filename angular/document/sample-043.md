# #043 「(input) 入力イベント」台本

四国めたん「(input) 入力イベントについて学びましょう！」
ずんだもん「入力のたびに処理が実行されるの？」
四国めたん「はい！文字を入力する度にリアルタイムで処理が実行されます」
ずんだもん「どんな場面で使うの？」
四国めたん「リアルタイム検索、入力バリデーション、文字数カウントなどです」
ずんだもん「パフォーマンスは大丈夫？」
四国めたん「debounceTimeオペレーターを使って制御するのがベストプラクティスです」

---

## 📺 画面表示用コード

// 基本的な入力イベント
```typescript
@Component({
  selector: 'app-input-basic',
  standalone: true,
  template: `
    <div class="input-demo">
      <h2>基本的な入力イベント</h2>
      <input (input)="onInput($event)" placeholder="入力してください">
      <p>入力値: {{inputValue}}</p>
      <p>文字数: {{inputValue.length}}</p>
    </div>
  `,
  styles: [`
    .input-demo {
      padding: 20px;
    }
    input {
      padding: 8px;
      margin: 10px 0;
      width: 300px;
    }
  `]
})
export class InputBasicComponent {
  inputValue = '';
  
  onInput(event: Event) {
    const target = event.target as HTMLInputElement;
    this.inputValue = target.value;
    console.log('入力中:', this.inputValue);
  }
}
```

// リアルタイム検索
```typescript
@Component({
  selector: 'app-realtime-search',
  standalone: true,
  template: `
    <div class="search-demo">
      <h2>リアルタイム検索</h2>
      <input (input)="onSearch($event)" placeholder="検索キーワード">
      <div class="results">
        <div *ngFor="let item of filteredItems">
          {{item}}
        </div>
      </div>
    </div>
  `,
  styles: [`
    .search-demo {
      padding: 20px;
    }
    input {
      padding: 8px;
      margin: 10px 0;
      width: 300px;
    }
    .results {
      margin-top: 10px;
    }
    .results div {
      padding: 5px;
      border-bottom: 1px solid #eee;
    }
  `]
})
export class RealtimeSearchComponent {
  searchTerm = '';
  items = ['Angular', 'React', 'Vue', 'TypeScript', 'JavaScript'];
  filteredItems: string[] = [];
  
  onSearch(event: Event) {
    const target = event.target as HTMLInputElement;
    this.searchTerm = target.value.toLowerCase();
    
    this.filteredItems = this.items.filter(item =>
      item.toLowerCase().includes(this.searchTerm)
    );
  }
}
```

// 入力バリデーション
```typescript
@Component({
  selector: 'app-input-validation',
  standalone: true,
  template: `
    <div class="validation-demo">
      <h2>入力バリデーション</h2>
      <input (input)="validateEmail($event)" 
             placeholder="メールアドレス"
             [class.error]="isEmailInvalid">
      <p *ngIf="isEmailInvalid" class="error-message">
        有効なメールアドレスを入力してください
      </p>
      <p *ngIf="!isEmailInvalid && email" class="success-message">
        有効なメールアドレスです
      </p>
    </div>
  `,
  styles: [`
    .validation-demo {
      padding: 20px;
    }
    input {
      padding: 8px;
      margin: 10px 0;
      width: 300px;
      border: 2px solid #ccc;
    }
    input.error {
      border-color: #dc3545;
    }
    .error-message {
      color: #dc3545;
      font-size: 14px;
    }
    .success-message {
      color: #28a745;
      font-size: 14px;
    }
  `]
})
export class InputValidationComponent {
  email = '';
  isEmailInvalid = false;
  
  validateEmail(event: Event) {
    const target = event.target as HTMLInputElement;
    this.email = target.value;
    
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    this.isEmailInvalid = this.email.length > 0 && !emailRegex.test(this.email);
  }
}
```
