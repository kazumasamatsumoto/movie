# #052 [(ngModel)] FormsModule のインポート

## 概要
Angular v20におけるFormsModuleのインポート方法を学びます。standaloneコンポーネントでの新しいインポート方式と従来のNgModule方式の違いを理解し、[(ngModel)]を使用するための適切な設定方法を習得します。

## 学習目標
- FormsModuleのインポート方法を理解する
- standaloneコンポーネントでの設定方法を習得する
- エラーの原因と解決方法を把握する

## 📺 画面表示用コード

```typescript
// standaloneコンポーネント
import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-form',
  standalone: true,
  imports: [FormsModule],
  template: `<input [(ngModel)]="name">`
})
export class FormComponent {
  name = '';
}
```

```typescript
// 従来のNgModule方式（参考）
@NgModule({
  imports: [FormsModule],
  declarations: [FormComponent]
})
export class FormModule {}
```

```typescript
// ReactiveFormsModuleも同様
import { ReactiveFormsModule } from '@angular/forms';
```

## 技術ポイント

### 1. Standaloneコンポーネントでのインポート
```typescript
import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-form',
  standalone: true,
  imports: [FormsModule],
  template: `<input [(ngModel)]="name">`
})
export class FormComponent {
  name = '';
}
```

### 2. ReactiveFormsModuleのインポート
```typescript
import { ReactiveFormsModule } from '@angular/forms';

@Component({
  selector: 'app-reactive-form',
  standalone: true,
  imports: [ReactiveFormsModule],
  template: `<form [formGroup]="form"></form>`
})
export class ReactiveFormComponent {
  form = new FormGroup({
    name: new FormControl('')
  });
}
```

### 3. 従来のNgModule方式（参考）
```typescript
import { NgModule } from '@angular/core';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';

@NgModule({
  imports: [FormsModule, ReactiveFormsModule],
  declarations: [FormComponent, ReactiveFormComponent]
})
export class FormModule {}
```

## 実践的な活用例

### 複数モジュールの組み合わせ
```typescript
@Component({
  selector: 'app-comprehensive-form',
  standalone: true,
  imports: [
    FormsModule,
    ReactiveFormsModule,
    CommonModule
  ],
  template: `
    <form [formGroup]="form">
      <input [(ngModel)]="templateName">
      <input formControlName="reactiveName">
    </form>
  `
})
export class ComprehensiveFormComponent {
  templateName = '';
  form = new FormGroup({
    reactiveName: new FormControl('')
  });
}
```

### 条件付きインポート
```typescript
@Component({
  selector: 'app-conditional-form',
  standalone: true,
  imports: [
    CommonModule,
    ...(useReactiveForms ? [ReactiveFormsModule] : [FormsModule])
  ]
})
export class ConditionalFormComponent {
  static useReactiveForms = true;
}
```

## よくあるエラーと解決方法

### 1. "Can't bind to 'ngModel' since it isn't a known property"
**原因**: FormsModuleがインポートされていない
**解決方法**: imports配列にFormsModuleを追加

### 2. "FormControl is not defined"
**原因**: ReactiveFormsModuleがインポートされていない
**解決方法**: imports配列にReactiveFormsModuleを追加

### 3. "Standalone component cannot be declared"
**原因**: standaloneコンポーネントをNgModuleで宣言している
**解決方法**: declarationsから削除し、importsに追加

## ベストプラクティス

1. **適切なモジュール選択**: 用途に応じてFormsModuleまたはReactiveFormsModuleを選択
2. **最小限のインポート**: 必要なモジュールのみをインポート
3. **型安全性**: TypeScriptの型定義を活用
4. **パフォーマンス**: OnPush戦略との組み合わせを検討

## 注意点

- standaloneコンポーネントではimports配列を使用
- 従来のNgModule方式とは異なる設定方法
- バンドルサイズの最適化を意識したインポート
- Angular v20の新機能との組み合わせも考慮

## 関連技術
- Standalone Components
- FormsModule
- ReactiveFormsModule
- NgModule
- コンポーネント設定
