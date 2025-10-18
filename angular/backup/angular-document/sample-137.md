# #137 「ViewChild static オプション」

## 概要
`@ViewChild`の`static`オプションを理解し、参照が取得されるタイミングとライフサイクルとの関係を整理します。

## 学習目標
- `static: true`と`static: false`の動作の違いを理解する
- ライフサイクルフックと連携する適切な設定を選択する
- 条件付きテンプレートでの注意点を把握する

## 技術ポイント
- **static: false（デフォルト）**: `ngAfterViewInit`で参照が取得される
- **static: true**: `ngOnInit`で参照が利用可能（*ngIfで切り替わらない要素向け）
- **構造ディレクティブ**: `static: true`は*ngIfや*ngForによる遅延生成には不向き

```typescript
@ViewChild('title', { static: true })
title?: ElementRef<HTMLHeadingElement>;
```

```typescript
@ViewChild('panel', { static: false })
panel?: ElementRef<HTMLDivElement>;
```

```typescript
ngOnInit() { console.log(this.title?.nativeElement.textContent); }
```

## 💻 詳細実装例（学習用）
```typescript
// static-demo.component.ts
import { AfterViewInit, Component, ElementRef, OnInit, ViewChild } from '@angular/core';

@Component({
  selector: 'app-static-demo',
  standalone: true,
  templateUrl: './static-demo.component.html',
})
export class StaticDemoComponent implements OnInit, AfterViewInit {
  showPanel = true;

  @ViewChild('heading', { static: true })
  heading?: ElementRef<HTMLHeadingElement>;

  @ViewChild('panel', { static: false })
  panel?: ElementRef<HTMLDivElement>;

  ngOnInit(): void {
    console.log('heading:', this.heading?.nativeElement.textContent);
  }

  ngAfterViewInit(): void {
    console.log('panel width:', this.panel?.nativeElement.offsetWidth);
  }

  toggle(): void {
    this.showPanel = !this.showPanel;
  }
}
```

```html
<!-- static-demo.component.html -->
<h2 #heading>Static true で取得</h2>
<button type="button" (click)="toggle()">パネル表示を切り替え</button>
<div *ngIf="showPanel" #panel class="panel">
  動的に切り替わるパネル
</div>
```

```css
/* static-demo.component.css */
.panel {
  border: 1px dashed #90caf9;
  padding: 12px;
}
```

## ベストプラクティス
- 初期化段階で参照が必要か、描画完了後で良いのかを判断して`static`を選ぶ
- *ngIfで切り替える要素は`static: false`に設定し、`ngAfterViewInit`または`ngAfterViewChecked`で扱う
- コードレビューで`static`の指定理由をコメントしておくと理解が深まる

## 注意点
- `static: true`にすると、まだDOMが生成されていない要素にアクセスしようとしてエラーになる場合がある
- Angular 9以降はIvyの挙動に合わせてデフォルトが`static: false`
- テストでは`fixture.detectChanges()`の呼び出しタイミングで参照の有無が変わるため意識する

## 関連技術
- ライフサイクルフック `ngOnInit`, `ngAfterViewInit`
- `@ContentChild`の`static`オプション
- `ChangeDetectionStrategy`との組み合わせ
