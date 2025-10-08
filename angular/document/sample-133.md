# #133 「ViewChild テンプレート参照変数」

## 概要
テンプレート参照変数（`#`記法）と`@ViewChild`を組み合わせて、テンプレート内の要素やコンポーネントへアクセスする方法を詳しく解説します。

## 学習目標
- テンプレート参照変数の定義方法を理解する
- ViewChildで参照変数を指定して要素を取得する手順を習得する
- 参照変数の命名とスコープを意識した設計を学ぶ

## 技術ポイント
- **参照変数定義**: `<input #keyword />`
- **ViewChild連携**: `@ViewChild('keyword') keywordInput?: ElementRef<HTMLInputElement>;`
- **スコープ**: 同テンプレート内でのみ有効、構造ディレクティブで変化

## 📺 画面表示用コード（動画用）

```html
<input #keyword placeholder="検索語" />
```

```typescript
@ViewChild('keyword')
keywordInput?: ElementRef<HTMLInputElement>;
```

```typescript
this.keywordInput?.nativeElement.focus();
```

## 💻 詳細実装例（学習用）
```typescript
// search-box.component.ts
import { AfterViewInit, Component, ElementRef, ViewChild } from '@angular/core';

@Component({
  selector: 'app-search-box',
  standalone: true,
  templateUrl: './search-box.component.html',
})
export class SearchBoxComponent implements AfterViewInit {
  @ViewChild('keyword') keywordInput?: ElementRef<HTMLInputElement>;

  ngAfterViewInit(): void {
    this.keywordInput?.nativeElement.focus();
  }

  clear(): void {
    if (this.keywordInput) {
      this.keywordInput.nativeElement.value = '';
    }
  }
}
```

```html
<!-- search-box.component.html -->
<input #keyword placeholder="キーワードを入力" />
<button type="button" (click)="clear()">クリア</button>
```

## ベストプラクティス
- 参照変数名は読みやすく、意図が伝わる名前にする（`#form`, `#modal`など）
- 構造ディレクティブで生成される要素を参照する際はタイミングに注意する
- TemplateRefなど別の型を取得したい場合は`{ read: TemplateRef }`を併用する

## 注意点
- 参照変数は同じテンプレート内で一意である必要がある
- *ngIfで要素を切り替えると参照が一時的にnullになる場合がある
- 直接DOM操作する際はSSRやアクセス権限を考慮する

## 関連技術
- TemplateRefとViewContainerRef
- `@ViewChildren`との違い
- テンプレート参照変数とAngularフォーム（ngModel, NgForm）
