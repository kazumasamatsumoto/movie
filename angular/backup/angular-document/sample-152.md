# #152 「テンプレート参照変数 # の活用」

## 概要
テンプレート参照変数（`#variable`）を使ってテンプレート内の要素やコンポーネントにアクセスし、バインディングや`@ViewChild`と組み合わせる基本的な手法を学びます。

## 学習目標
- テンプレート参照変数の宣言と利用方法を理解する
- テンプレート式やイベントから参照変数を利用する手順を習得する
- ViewChildと併用して型安全に扱う方法を把握する

## 技術ポイント
- **宣言**: `<input #keyword />`
- **テンプレート式**: `(keyup.enter)="search(keyword.value)"`
- **ViewChild連携**: `@ViewChild('keyword') keywordInput?: ElementRef<HTMLInputElement>;`

```html
<input #keyword (keyup.enter)="search(keyword.value)" />
```

```html
<app-dialog #dialog></app-dialog>
```

```typescript
@ViewChild('dialog') dialog?: DialogComponent;
```

## 💻 詳細実装例（学習用）
```typescript
// search-form.component.ts
import { Component, ElementRef, ViewChild } from '@angular/core';

@Component({
  selector: 'app-search-form',
  standalone: true,
  templateUrl: './search-form.component.html',
})
export class SearchFormComponent {
  @ViewChild('keyword')
  keywordInput?: ElementRef<HTMLInputElement>;

  search(value: string): void {
    console.log('検索:', value);
  }

  clear(): void {
    if (this.keywordInput) {
      this.keywordInput.nativeElement.value = '';
      this.keywordInput.nativeElement.focus();
    }
  }
}
```

```html
<!-- search-form.component.html -->
<input
  #keyword
  placeholder="キーワード"
  (keyup.enter)="search(keyword.value)"
/>
<button type="button" (click)="clear()">クリア</button>
```

## ベストプラクティス
- 参照変数名には役割がわかる名前を付け、コードとの関連性を高める
- テンプレート内のみで完結する場合はViewChildを使わず、参照変数経由で処理する
- コンポーネントやディレクティブを参照する場合は型を意識し、必要ならViewChildで取得して型安全に扱う

## 注意点
- 参照変数は宣言したテンプレートのスコープ内でのみ有効。ng-template内部などスコープが変わる場合は注意
- *ngIfで要素が存在しないと参照も存在しないため、nullチェックが必要
- テンプレート参照変数を過剰に使うとテンプレートが読みづらくなるのでバランスを取る

## 関連技術
- `@ViewChild` / `@ViewChildren`
- TemplateRefとViewContainerRef
- Angularフォーム（NgForm, NgModel）との連携
