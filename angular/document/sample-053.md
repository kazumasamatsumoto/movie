# #053 バナナインボックス構文の仕組み

## 概要
Angular v20における「バナナインボックス構文」[(ngModel)]の内部的な仕組みを学びます。糖衣構文として実装されている双方向バインディングが、実際にはどのように展開され動作するかを理解します。

## 学習目標
- バナナインボックス構文の仕組みを理解する
- 糖衣構文の展開方法を把握する
- 双方向バインディングの内部動作を習得する

## 📺 画面表示用コード

```typescript
// バナナインボックス構文（糖衣構文）
<input [(ngModel)]="userName">
```

```typescript
// 実際の展開形
<input [ngModel]="userName" (ngModelChange)="userName = $event">
```

```typescript
// コンポーネント側
export class MyComponent {
  userName = '';
  
  onNameChange(value: string) {
    this.userName = value;
    console.log('名前が変更されました:', value);
  }
}
```

```html
<!-- 明示的に書く場合 -->
<input [ngModel]="userName" (ngModelChange)="onNameChange($event)">
```

## 技術ポイント

### 1. バナナインボックス構文（糖衣構文）
```html
<input [(ngModel)]="userName">
```

### 2. 実際の展開形
```html
<input [ngModel]="userName" (ngModelChange)="userName = $event">
```

### 3. 明示的なイベントハンドリング
```html
<input [ngModel]="userName" (ngModelChange)="onNameChange($event)">
```

```typescript
export class MyComponent {
  userName = '';
  
  onNameChange(value: string) {
    this.userName = value;
    console.log('名前が変更されました:', value);
  }
}
```

## 実践的な活用例

### カスタムバリデーション付きフォーム
```typescript
export class ValidatedFormComponent {
  email = '';
  isValidEmail = true;
  
  onEmailChange(value: string) {
    this.email = value;
    this.isValidEmail = this.validateEmail(value);
    
    if (!this.isValidEmail) {
      console.log('無効なメールアドレスです');
    }
  }
  
  private validateEmail(email: string): boolean {
    const pattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return pattern.test(email);
  }
}
```

### リアルタイム文字数カウント
```typescript
export class CharacterCountComponent {
  message = '';
  maxLength = 100;
  remainingChars = this.maxLength;
  
  onMessageChange(value: string) {
    this.message = value;
    this.remainingChars = this.maxLength - value.length;
    
    if (this.remainingChars < 0) {
      this.message = value.substring(0, this.maxLength);
      this.remainingChars = 0;
    }
  }
}
```

### 複数フィールドの連動
```typescript
export class LinkedFieldsComponent {
  firstName = '';
  lastName = '';
  fullName = '';
  
  onFirstNameChange(value: string) {
    this.firstName = value;
    this.updateFullName();
  }
  
  onLastNameChange(value: string) {
    this.lastName = value;
    this.updateFullName();
  }
  
  private updateFullName() {
    this.fullName = `${this.firstName} ${this.lastName}`.trim();
  }
}
```

## 内部動作の詳細

### 1. プロパティバインディング部分
```html
[ngModel]="userName"
```
- コンポーネントのuserNameプロパティの値をngModelディレクティブに渡す
- 一方向のデータフロー（コンポーネント → テンプレート）

### 2. イベントバインディング部分
```html
(ngModelChange)="userName = $event"
```
- ngModelの値が変更された時に発火するイベント
- $eventには新しい値が含まれる
- 一方向のデータフロー（テンプレート → コンポーネント）

### 3. 双方向の実現
```typescript
// この2つの組み合わせで双方向バインディングを実現
[ngModel]="userName"           // コンポーネント → テンプレート
(ngModelChange)="userName = $event"  // テンプレート → コンポーネント
```

## カスタム双方向バインディング

### カスタムディレクティブでの実装
```typescript
@Directive({
  selector: '[myModel]',
  standalone: true
})
export class MyModelDirective {
  @Input() myModel: any;
  @Output() myModelChange = new EventEmitter<any>();
  
  @HostListener('input', ['$event'])
  onInput(event: any) {
    this.myModelChange.emit(event.target.value);
  }
}
```

### 使用例
```html
<input [myModel]="value" (myModelChange)="value = $event">
<!-- または -->
<input [(myModel)]="value">
```

## ベストプラクティス

1. **糖衣構文の理解**: 内部動作を理解してから使用する
2. **適切なイベントハンドリング**: 複雑なロジックは明示的に処理
3. **パフォーマンス考慮**: 不要な変更検知を避ける
4. **型安全性**: TypeScriptの型定義を活用

## 注意点

- 糖衣構文は読みやすさのために使用
- 複雑な処理は明示的なイベントハンドリングを使用
- カスタムディレクティブでの双方向バインディングも可能
- Angular v20でも同じ仕組みが使用される

## 関連技術
- プロパティバインディング
- イベントバインディング
- 糖衣構文
- カスタムディレクティブ
- 双方向データバインディング
