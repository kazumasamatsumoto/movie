# #177 「[ngClass] オブジェクト構文」

## 概要
Angular v20における[ngClass]のオブジェクト構文の使用方法。{クラス名: 条件}の形式で複数のクラスを条件付きで適用し、効率的な動的クラス制御を実現する方法を学ぶ。

## 学習目標
- [ngClass]オブジェクト構文の使い方を理解する
- 複数条件の管理を学ぶ
- 効率的なクラス制御を把握する

## 技術ポイント
- オブジェクト構文の基本形式
- 複数条件の組み合わせ
- 論理演算子の活用
- 動的なクラス適用

## 📺 画面表示用コード

### オブジェクト構文の基本的な使用
```typescript
@Component({
  selector: 'app-ngclass-object',
  template: `
    <div class="container">
      <h2>オブジェクト構文によるクラス制御</h2>
      
      <div class="form-section">
        <h3>フォーム要素</h3>
        <input type="text" 
               [(ngModel)]="userInput"
               [ngClass]="{
                 'form-control': true,
                 'valid': isValid,
                 'invalid': isInvalid,
                 'required': isRequired,
                 'focused': isFocused
               }"
               (focus)="isFocused = true"
               (blur)="isFocused = false"
               placeholder="テキストを入力してください">
        
        <div class="validation-message" 
             [ngClass]="{
               'message': true,
               'success': isValid,
               'error': isInvalid,
               'hidden': !isValid && !isInvalid
             }">
          {{ validationMessage }}
        </div>
      </div>
      
      <div class="card-section">
        <h3>カード要素</h3>
        <div class="card" 
             [ngClass]="{
               'card': true,
               'selected': isSelected,
               'hovered': isHovered,
               'loading': isLoading,
               'disabled': isDisabled
             }"
             (mouseenter)="isHovered = true"
             (mouseleave)="isHovered = false"
             (click)="toggleSelection()">
          
          <div class="card-header">
            <h4>カードタイトル</h4>
            <div class="card-actions">
              <button (click)="toggleLoading()" 
                      [ngClass]="{'btn': true, 'loading': isLoading}">
                {{ isLoading ? '読み込み中...' : 'アクション' }}
              </button>
            </div>
          </div>
          
          <div class="card-body">
            <p>カードの内容です。状態に応じてスタイルが変わります。</p>
          </div>
        </div>
      </div>
      
      <div class="controls">
        <button (click)="validateInput()">検証実行</button>
        <button (click)="toggleDisabled()">無効化切り替え</button>
        <button (click)="resetStates()">リセット</button>
      </div>
    </div>
  `,
  styles: [`
    .container {
      padding: 20px;
      max-width: 800px;
      margin: 0 auto;
    }
    
    .form-control {
      width: 100%;
      padding: 12px;
      border: 2px solid #ddd;
      border-radius: 6px;
      font-size: 16px;
      transition: all 0.3s ease;
      margin-bottom: 10px;
    }
    
    .form-control.valid {
      border-color: #28a745;
      background-color: rgba(40, 167, 69, 0.1);
    }
    
    .form-control.invalid {
      border-color: #dc3545;
      background-color: rgba(220, 53, 69, 0.1);
    }
    
    .form-control.required {
      border-left: 4px solid #ffc107;
    }
    
    .form-control.focused {
      box-shadow: 0 0 0 3px rgba(0, 123, 255, 0.1);
      border-color: #007bff;
    }
    
    .validation-message {
      padding: 8px 12px;
      border-radius: 4px;
      margin-bottom: 15px;
      font-size: 14px;
      transition: all 0.3s ease;
    }
    
    .validation-message.success {
      background-color: #d4edda;
      color: #155724;
      border: 1px solid #c3e6cb;
    }
    
    .validation-message.error {
      background-color: #f8d7da;
      color: #721c24;
      border: 1px solid #f5c6cb;
    }
    
    .validation-message.hidden {
      opacity: 0;
      height: 0;
      padding: 0;
      margin: 0;
      overflow: hidden;
    }
    
    .card {
      border: 2px solid #ddd;
      border-radius: 10px;
      padding: 20px;
      margin: 15px 0;
      transition: all 0.3s ease;
      cursor: pointer;
    }
    
    .card.selected {
      border-color: #007bff;
      background-color: rgba(0, 123, 255, 0.05);
      box-shadow: 0 4px 12px rgba(0, 123, 255, 0.2);
    }
    
    .card.hovered {
      transform: translateY(-2px);
      box-shadow: 0 6px 20px rgba(0,0,0,0.1);
    }
    
    .card.loading {
      opacity: 0.7;
      pointer-events: none;
    }
    
    .card.disabled {
      opacity: 0.5;
      cursor: not-allowed;
    }
    
    .card-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 15px;
    }
    
    .card-header h4 {
      margin: 0;
      color: #333;
    }
    
    .btn {
      padding: 8px 16px;
      border: none;
      border-radius: 4px;
      cursor: pointer;
      background: #6c757d;
      color: white;
      transition: all 0.3s ease;
    }
    
    .btn.loading {
      background: #ffc107;
      color: #333;
    }
    
    .controls {
      margin-top: 20px;
      display: flex;
      gap: 10px;
    }
    
    .controls button {
      padding: 10px 20px;
      border: none;
      border-radius: 6px;
      cursor: pointer;
      background: #007bff;
      color: white;
      transition: all 0.3s ease;
    }
    
    .controls button:hover {
      background: #0056b3;
    }
  `]
})
export class NgClassObjectComponent {
  userInput = '';
  isValid = false;
  isInvalid = false;
  isRequired = true;
  isFocused = false;
  isSelected = false;
  isHovered = false;
  isLoading = false;
  isDisabled = false;
  
  get validationMessage() {
    if (this.isValid) return '入力が有効です';
    if (this.isInvalid) return '入力が無効です';
    return '';
  }
  
  validateInput() {
    this.isValid = this.userInput.length > 3;
    this.isInvalid = this.userInput.length <= 3 && this.userInput.length > 0;
  }
  
  toggleSelection() {
    if (!this.isDisabled) {
      this.isSelected = !this.isSelected;
    }
  }
  
  toggleLoading() {
    this.isLoading = !this.isLoading;
    if (this.isLoading) {
      setTimeout(() => {
        this.isLoading = false;
      }, 2000);
    }
  }
  
  toggleDisabled() {
    this.isDisabled = !this.isDisabled;
    if (this.isDisabled) {
      this.isSelected = false;
    }
  }
  
  resetStates() {
    this.isValid = false;
    this.isInvalid = false;
    this.isFocused = false;
    this.isSelected = false;
    this.isHovered = false;
    this.isLoading = false;
    this.isDisabled = false;
    this.userInput = '';
  }
}
```

## 実践的な活用例
- フォームバリデーション
- インタラクティブなカード
- 状態に応じたスタイル適用

## ベストプラクティス
- 明確な条件設定
- 適切なクラス命名
- パフォーマンスの考慮

## 注意点
- 条件の複雑さ管理
- クラスの競合回避
- 可読性の維持

## 関連技術
- オブジェクト構文
- 複数条件管理
- 動的クラス制御
