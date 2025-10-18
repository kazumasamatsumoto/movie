# #154 「ElementRef での直接 DOM アクセス」

## 概要
`ElementRef`を通じてDOM要素へ直接アクセスし、簡単な操作を行う方法と、その際の注意点を学びます。

## 学習目標
- ElementRefの役割と`nativeElement`プロパティを理解する
- フォーカス移動やスクロールなど軽量なDOM操作を実装する
- SSRやセキュリティを考慮した防御的コーディングを身につける

## 技術ポイント
- **ElementRef**: `nativeElement`に実DOM要素が格納される
- **操作例**: `focus()`, `scrollIntoView()`, `setAttribute()`
- **プラットフォーム判定**: SSR対応には`isPlatformBrowser`でチェック

```typescript
@ViewChild('input') input?: ElementRef<HTMLInputElement>;
```

```typescript
this.input?.nativeElement.focus();
```

```typescript
this.input?.nativeElement.scrollIntoView({ behavior: 'smooth' });
```

## 💻 詳細実装例（学習用）
```typescript
// focus-input.component.ts
import { AfterViewInit, Component, ElementRef, Inject, PLATFORM_ID, ViewChild } from '@angular/core';
import { isPlatformBrowser } from '@angular/common';

@Component({
  selector: 'app-focus-input',
  standalone: true,
  templateUrl: './focus-input.component.html',
})
export class FocusInputComponent implements AfterViewInit {
  @ViewChild('field')
  field?: ElementRef<HTMLInputElement>;

  constructor(@Inject(PLATFORM_ID) private readonly platformId: object) {}

  ngAfterViewInit(): void {
    if (isPlatformBrowser(this.platformId)) {
      this.field?.nativeElement.focus();
    }
  }

  selectAll(): void {
    const element = this.field?.nativeElement;
    element?.setSelectionRange(0, element.value.length);
  }
}
```

```html
<!-- focus-input.component.html -->
<input #field placeholder="ElementRefで操作" />
<button type="button" (click)="selectAll()">すべて選択</button>
```

## ベストプラクティス
- DOM操作は最小限に留め、可能な限りRenderer2やAngular CDKを利用する
- SSR対応アプリでは必ずプラットフォームを確認してから`nativeElement`を操作する
- DOMを直接操作するメソッドはテストを容易にするためコンポーネント内に閉じ込める

## 注意点
- `nativeElement`を直接書き換えるとXSSの危険があるため、信頼できるデータのみ扱う
- サーバーサイドレンダリングではDOMが存在しないため、条件分岐が必要
- 直接操作はChangeDetectionと競合する可能性があるので、状態変更を伴う場合はChangeDetectorRefを考慮する

## 関連技術
- Renderer2によるDOM抽象化
- `@ViewChild`での要素取得
- CDK OverlayやPortalなどの高度なDOM操作補助
