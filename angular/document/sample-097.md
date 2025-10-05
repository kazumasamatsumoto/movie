# #097 「@Input() プリミティブ型の受け渡し」

## 概要
Angular v20における@Input()でのプリミティブ型の受け渡しを学びます。string、number、booleanなどの基本的な型を安全に受け渡し、値渡しの特性を理解する方法について解説します。

## 学習目標
- プリミティブ型の受け渡し方法を理解する
- 値渡しの特性を把握する
- 型安全性を考慮した実装方法を習得する

## 📺 画面表示用コード

```typescript
// プリミティブ型の受け渡し
@Component({
  selector: 'app-primitive-types',
  standalone: true,
  template: `
    <div class="primitive-display">
      <h3>{{title}}</h3>
      <p>数値: {{count}}</p>
      <p>有効: {{isActive}}</p>
      <p>タグ: {{tag}}</p>
    </div>
  `
})
export class PrimitiveTypesComponent {
  @Input() title: string = '';
  @Input() count: number = 0;
  @Input() isActive: boolean = false;
  @Input() tag: string = '';
}
```

```html
<!-- 親コンポーネントでの使用 -->
<app-primitive-types
  [title]="'プリミティブ型の例'"
  [count]="42"
  [isActive]="true"
  [tag]="'angular'">
</app-primitive-types>
```

```typescript
// 動的な値の受け渡し
export class DynamicPrimitiveComponent {
  @Input() dynamicValue: string | number = '';
  
  ngOnInit() {
    console.log('受信した値:', this.dynamicValue);
    console.log('型:', typeof this.dynamicValue);
  }
}
```

## 技術ポイント

### 1. プリミティブ型の種類
- **string**: 文字列型
- **number**: 数値型
- **boolean**: 真偽値型
- **undefined**: 未定義型
- **null**: null型

### 2. 値渡しの特性
- **コピー**: プリミティブ型は値のコピーが渡される
- **独立性**: 子で変更しても親に影響しない
- **メモリ効率**: 軽量でメモリ効率が良い

### 3. 型安全性の考慮
- **型指定**: 明確な型定義による型安全性
- **デフォルト値**: 適切なデフォルト値の設定
- **バリデーション**: 実行時の値チェック

## 実践的な活用例

### 1. 設定コンポーネントでのプリミティブ型
```typescript
// settings.component.ts
@Component({
  selector: 'app-settings',
  standalone: true,
  template: `
    <div class="settings">
      <h3>{{title}}</h3>
      <div class="setting-item">
        <label>最大値:</label>
        <span>{{maxValue}}</span>
      </div>
      <div class="setting-item">
        <label>自動保存:</label>
        <span>{{autoSave ? 'ON' : 'OFF'}}</span>
      </div>
      <div class="setting-item">
        <label>テーマ:</label>
        <span>{{theme}}</span>
      </div>
      <div class="setting-item">
        <label>更新間隔:</label>
        <span>{{updateInterval}}秒</span>
      </div>
    </div>
  `
})
export class SettingsComponent {
  @Input() title: string = '設定';
  @Input() maxValue: number = 100;
  @Input() autoSave: boolean = true;
  @Input() theme: string = 'light';
  @Input() updateInterval: number = 30;
  
  ngOnInit() {
    this.validateSettings();
  }
  
  private validateSettings() {
    if (this.maxValue < 0) {
      console.warn('最大値が負の値です');
    }
    
    if (this.updateInterval < 1) {
      console.warn('更新間隔が1秒未満です');
    }
  }
}
```

### 2. カウンターコンポーネントでの数値型
```typescript
// counter.component.ts
@Component({
  selector: 'app-counter',
  standalone: true,
  template: `
    <div class="counter">
      <button (click)="decrement()" [disabled]="currentValue <= minValue">-</button>
      <span class="count">{{currentValue}}</span>
      <button (click)="increment()" [disabled]="currentValue >= maxValue">+</button>
      <div class="info">
        <p>最小値: {{minValue}}</p>
        <p>最大値: {{maxValue}}</p>
        <p>ステップ: {{step}}</p>
      </div>
    </div>
  `
})
export class CounterComponent {
  @Input() initialValue: number = 0;
  @Input() minValue: number = 0;
  @Input() maxValue: number = 100;
  @Input() step: number = 1;
  @Input() disabled: boolean = false;
  
  @Output() valueChange = new EventEmitter<number>();
  
  currentValue: number = 0;
  
  ngOnInit() {
    this.currentValue = this.initialValue;
    this.validateBounds();
  }
  
  increment() {
    if (!this.disabled && this.currentValue < this.maxValue) {
      this.currentValue = Math.min(this.currentValue + this.step, this.maxValue);
      this.valueChange.emit(this.currentValue);
    }
  }
  
  decrement() {
    if (!this.disabled && this.currentValue > this.minValue) {
      this.currentValue = Math.max(this.currentValue - this.step, this.minValue);
      this.valueChange.emit(this.currentValue);
    }
  }
  
  private validateBounds() {
    if (this.minValue > this.maxValue) {
      console.error('最小値が最大値を超えています');
    }
    
    if (this.step <= 0) {
      console.error('ステップ値は正の数である必要があります');
    }
  }
}
```

### 3. トグルコンポーネントでの真偽値型
```typescript
// toggle.component.ts
@Component({
  selector: 'app-toggle',
  standalone: true,
  template: `
    <div class="toggle" [class.disabled]="disabled">
      <label class="toggle-label">
        <input 
          type="checkbox" 
          [checked]="isOn" 
          [disabled]="disabled"
          (change)="onToggle()">
        <span class="toggle-slider"></span>
        <span class="toggle-text">{{label}}</span>
      </label>
      <div *ngIf="description" class="toggle-description">
        {{description}}
      </div>
    </div>
  `
})
export class ToggleComponent {
  @Input() isOn: boolean = false;
  @Input() label: string = 'トグル';
  @Input() description: string = '';
  @Input() disabled: boolean = false;
  @Input() size: 'small' | 'medium' | 'large' = 'medium';
  
  @Output() toggleChange = new EventEmitter<boolean>();
  
  onToggle() {
    if (!this.disabled) {
      this.isOn = !this.isOn;
      this.toggleChange.emit(this.isOn);
    }
  }
  
  get toggleClasses(): string {
    return `toggle toggle-${this.size} ${this.isOn ? 'toggle-on' : 'toggle-off'}`;
  }
}
```

### 4. テキスト表示コンポーネントでの文字列型
```typescript
// text-display.component.ts
@Component({
  selector: 'app-text-display',
  standalone: true,
  template: `
    <div class="text-display" [class]="displayClasses">
      <h3 *ngIf="title">{{title}}</h3>
      <div class="text-content" [innerHTML]="formattedText"></div>
      <div *ngIf="showMeta" class="text-meta">
        <p>文字数: {{characterCount}}</p>
        <p>単語数: {{wordCount}}</p>
        <p>行数: {{lineCount}}</p>
      </div>
    </div>
  `
})
export class TextDisplayComponent {
  @Input() text: string = '';
  @Input() title: string = '';
  @Input() maxLength: number = 0;
  @Input() showMeta: boolean = false;
  @Input() allowHtml: boolean = false;
  @Input() size: 'small' | 'medium' | 'large' = 'medium';
  @Input() color: string = 'black';
  
  get formattedText(): string {
    if (!this.text) return '';
    
    let processedText = this.text;
    
    if (this.maxLength > 0 && processedText.length > this.maxLength) {
      processedText = processedText.substring(0, this.maxLength) + '...';
    }
    
    if (!this.allowHtml) {
      processedText = this.escapeHtml(processedText);
    }
    
    return processedText;
  }
  
  get characterCount(): number {
    return this.text ? this.text.length : 0;
  }
  
  get wordCount(): number {
    return this.text ? this.text.split(/\s+/).filter(word => word.length > 0).length : 0;
  }
  
  get lineCount(): number {
    return this.text ? this.text.split('\n').length : 0;
  }
  
  get displayClasses(): string {
    return `text-display text-${this.size} text-color-${this.color}`;
  }
  
  private escapeHtml(text: string): string {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
  }
}
```

## ベストプラクティス

1. **型安全性**: 明確な型定義による型安全性の確保
2. **デフォルト値**: 適切なデフォルト値の設定
3. **バリデーション**: 実行時の値チェック
4. **パフォーマンス**: プリミティブ型の軽量性を活用

## 注意点

- プリミティブ型は値渡しなので、子で変更しても親に影響しない
- 型の不一致がある場合、Angularが自動的に変換を試みる
- デフォルト値は実行時に設定されるため、コンパイル時の型チェックとは別

## 関連技術
- TypeScript型システム
- 値渡し
- 型安全性
- バリデーション
