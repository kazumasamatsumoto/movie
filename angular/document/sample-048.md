# #048 「(focus) / (blur) フォーカスイベント」台本

四国めたん「(focus) / (blur) フォーカスイベントについて解説します！」
ずんだもん「フォーカスって何？」
四国めたん「要素が選択された状態のことです。input要素やbutton要素などで使用できます」
ずんだもん「focusとblurの違いは？」
四国めたん「focusは要素が選択された時、blurは選択が外れた時に発生します」
ずんだもん「どんな場面で使うの？」
四国めたん「バリデーション、ヘルプ表示、アクセシビリティ対応などに使用します」

---

## 📺 画面表示用コード

// 基本的なフォーカスイベント
```typescript
@Component({
  selector: 'app-focus-basic',
  standalone: true,
  template: `
    <div class="focus-demo">
      <h2>基本的なフォーカスイベント</h2>
      <input (focus)="onFocus()" 
             (blur)="onBlur()" 
             placeholder="フォーカスしてください">
      <p>フォーカス状態: {{isFocused ? 'フォーカス中' : 'フォーカス外'}}</p>
    </div>
  `,
  styles: [`
    .focus-demo {
      padding: 20px;
    }
    input {
      padding: 8px;
      margin: 10px 0;
      width: 300px;
      border: 2px solid #ccc;
    }
    input:focus {
      border-color: #007bff;
      outline: none;
    }
  `]
})
export class FocusBasicComponent {
  isFocused = false;
  
  onFocus() {
    this.isFocused = true;
    console.log('要素にフォーカスされました');
  }
  
  onBlur() {
    this.isFocused = false;
    console.log('要素からフォーカスが外れました');
  }
}
```

// フォーカス時のヘルプ表示
```typescript
@Component({
  selector: 'app-focus-help',
  standalone: true,
  template: `
    <div class="help-demo">
      <h2>フォーカス時のヘルプ表示</h2>
      <input (focus)="showHelp()" 
             (blur)="hideHelp()" 
             placeholder="パスワード">
      <div *ngIf="showHelpFlag" class="help-text">
        パスワードは8文字以上で入力してください
      </div>
    </div>
  `,
  styles: [`
    .help-demo {
      padding: 20px;
    }
    input {
      padding: 8px;
      margin: 10px 0;
      width: 300px;
    }
    .help-text {
      background-color: #e7f3ff;
      border: 1px solid #007bff;
      padding: 8px;
      margin: 5px 0;
      border-radius: 4px;
      font-size: 14px;
      color: #004085;
    }
  `]
})
export class FocusHelpComponent {
  showHelpFlag = false;
  
  showHelp() {
    this.showHelpFlag = true;
  }
  
  hideHelp() {
    this.showHelpFlag = false;
  }
}
```

// フォーカス管理
```typescript
@Component({
  selector: 'app-focus-management',
  standalone: true,
  template: `
    <div class="management-demo">
      <h2>フォーカス管理</h2>
      <input #input1 (focus)="onFocus('input1')" placeholder="入力1">
      <input #input2 (focus)="onFocus('input2')" placeholder="入力2">
      <input #input3 (focus)="onFocus('input3')" placeholder="入力3">
      <button (click)="focusNext()">次の入力欄にフォーカス</button>
      <p>現在フォーカス中: {{currentFocused}}</p>
    </div>
  `,
  styles: [`
    .management-demo {
      padding: 20px;
    }
    input, button {
      display: block;
      margin: 5px 0;
      padding: 8px;
    }
    input {
      width: 300px;
    }
  `]
})
export class FocusManagementComponent {
  @ViewChild('input1') input1!: ElementRef;
  @ViewChild('input2') input2!: ElementRef;
  @ViewChild('input3') input3!: ElementRef;
  
  currentFocused = '';
  currentIndex = 0;
  
  onFocus(inputName: string) {
    this.currentFocused = inputName;
  }
  
  focusNext() {
    const inputs = [this.input1, this.input2, this.input3];
    this.currentIndex = (this.currentIndex + 1) % inputs.length;
    inputs[this.currentIndex].nativeElement.focus();
  }
}
```
