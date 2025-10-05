# #054 複数のバインディングを組み合わせる

## 概要
Angular v20における複数のバインディングを同一要素に組み合わせる方法を学びます。プロパティバインディング、イベントバインディング、クラスバインディングなどを効果的に組み合わせて、柔軟でインタラクティブなUIを構築する技術を習得します。

## 学習目標
- 複数のバインディングを同時に使用する方法を理解する
- 異なるタイプのバインディングの組み合わせ方を習得する
- 実践的なUI開発パターンを身につける

## 📺 画面表示用コード

```html
<!-- 複数のバインディングを組み合わせ -->
<button 
  [disabled]="isLoading" 
  [class.active]="isSelected" 
  (click)="onClick()"
  (mouseover)="onHover()">
  クリック
</button>
```

```html
<!-- フォーム要素の組み合わせ -->
<input 
  [value]="userInput" 
  [placeholder]="placeholderText"
  (input)="onInput($event)"
  (blur)="onBlur()">
```

```typescript
// コンポーネント
export class MyComponent {
  isLoading = false;
  isSelected = true;
  userInput = '';
  
  onClick() {
    this.isLoading = true;
  }
}
```

## 技術ポイント

### 1. 基本的な組み合わせ
```html
<button 
  [disabled]="isLoading" 
  [class.active]="isSelected" 
  (click)="onClick()"
  (mouseover)="onHover()">
  クリック
</button>
```

### 2. フォーム要素の組み合わせ
```html
<input 
  [value]="userInput" 
  [placeholder]="placeholderText"
  (input)="onInput($event)"
  (blur)="onBlur()">
```

### 3. スタイルとイベントの組み合わせ
```html
<div 
  [style.background-color]="backgroundColor"
  [style.color]="textColor"
  (mouseenter)="onMouseEnter()"
  (mouseleave)="onMouseLeave()">
  ホバーエフェクト
</div>
```

## 実践的な活用例

### インタラクティブなボタン
```typescript
export class InteractiveButtonComponent {
  isLoading = false;
  isSelected = false;
  clickCount = 0;
  
  onClick() {
    this.isLoading = true;
    this.clickCount++;
    
    // シミュレートされた非同期処理
    setTimeout(() => {
      this.isLoading = false;
      this.isSelected = !this.isSelected;
    }, 1000);
  }
  
  onHover() {
    console.log('ボタンにホバーしました');
  }
}
```

### 動的フォームフィールド
```typescript
export class DynamicFormComponent {
  fields = [
    { id: 1, label: '名前', value: '', required: true },
    { id: 2, label: 'メール', value: '', required: true },
    { id: 3, label: '電話', value: '', required: false }
  ];
  
  onFieldChange(fieldId: number, value: string) {
    const field = this.fields.find(f => f.id === fieldId);
    if (field) {
      field.value = value;
    }
  }
  
  onFieldFocus(fieldId: number) {
    console.log(`フィールド${fieldId}にフォーカス`);
  }
  
  onFieldBlur(fieldId: number) {
    console.log(`フィールド${fieldId}からフォーカスが外れました`);
  }
}
```

### 条件付きスタイリング
```html
<div 
  [class.card]="true"
  [class.selected]="isSelected"
  [class.disabled]="isDisabled"
  [style.opacity]="isDisabled ? 0.5 : 1"
  (click)="onCardClick()"
  (dblclick)="onCardDoubleClick()">
  
  <h3 [style.color]="isSelected ? 'blue' : 'black'">
    {{title}}
  </h3>
  
  <p [class.highlight]="isHighlighted">
    {{description}}
  </p>
</div>
```

### リストアイテムのインタラクション
```typescript
export class ListItemComponent {
  items = signal([
    { id: 1, name: 'アイテム1', selected: false, hovered: false },
    { id: 2, name: 'アイテム2', selected: true, hovered: false },
    { id: 3, name: 'アイテム3', selected: false, hovered: false }
  ]);
  
  onItemClick(itemId: number) {
    this.items.update(items => 
      items.map(item => 
        item.id === itemId 
          ? { ...item, selected: !item.selected }
          : item
      )
    );
  }
  
  onItemHover(itemId: number, isHovering: boolean) {
    this.items.update(items =>
      items.map(item =>
        item.id === itemId
          ? { ...item, hovered: isHovering }
          : item
      )
    );
  }
}
```

## 高度な組み合わせパターン

### 1. 属性とイベントの組み合わせ
```html
<img 
  [src]="imageUrl"
  [alt]="imageAlt"
  [class.loading]="isLoading"
  (load)="onImageLoad()"
  (error)="onImageError()"
  (click)="onImageClick()">
```

### 2. フォームバリデーション付き
```html
<input 
  [value]="email"
  [class.invalid]="!isValidEmail"
  [placeholder]="emailPlaceholder"
  (input)="onEmailInput($event)"
  (blur)="validateEmail()"
  (focus)="clearValidation()">
```

### 3. アニメーション付き要素
```html
<div 
  [class.slide-in]="isVisible"
  [class.slide-out]="!isVisible"
  [style.transform]="transformValue"
  (animationend)="onAnimationEnd()"
  (transitionend)="onTransitionEnd()">
  アニメーション要素
</div>
```

## ベストプラクティス

1. **論理的なグループ化**: 関連するバインディングをグループ化
2. **読みやすさ**: 適切な改行とインデントを使用
3. **パフォーマンス**: 不要な変更検知を避ける
4. **保守性**: 複雑なロジックはコンポーネント側で処理

## 注意点

- バインディングの実行順序に注意
- 循環参照を避ける
- パフォーマンスへの影響を考慮
- アクセシビリティの確保

## 関連技術
- プロパティバインディング
- イベントバインディング
- クラスバインディング
- スタイルバインディング
- テンプレート式
- Angular v20のSignal
