# #132 「ViewChild の基本構文」

## 概要
`@ViewChild`の基本構文と、テンプレート参照変数を使った要素・コンポーネントの取得方法を整理します。

## 学習目標
- ViewChildデコレータの書式を身につける
- テンプレート参照変数との対応関係を理解する
- 取得した参照を安全に扱うタイミングを把握する

## 技術ポイント
- **宣言**: `@ViewChild('refName') element?: ElementRef<HTMLDivElement>;`
- **テンプレート参照変数**: `<div #refName></div>`
- **アクセス時期**: `ngAfterViewInit`以降が安全

## 📺 画面表示用コード（動画用）
**表示ルール**: 最大3個、各10行以内、動画で見せる部分のみ

```html
<div #box class="box"></div>
```

```typescript
@ViewChild('box')
box?: ElementRef<HTMLDivElement>;
```

```typescript
this.box?.nativeElement.classList.add('active');
```

## 💻 詳細実装例（学習用）
```typescript
// box.component.ts
import { AfterViewInit, Component, ElementRef, ViewChild } from '@angular/core';

@Component({
  selector: 'app-box',
  standalone: true,
  templateUrl: './box.component.html',
  styleUrls: ['./box.component.css'],
})
export class BoxComponent implements AfterViewInit {
  @ViewChild('box') box?: ElementRef<HTMLDivElement>;

  ngAfterViewInit(): void {
    this.box?.nativeElement.classList.add('initialized');
  }
}
```

```html
<!-- box.component.html -->
<div #box class="box">ViewChild 基本構文</div>
```

```css
/* box.component.css */
.box {
  padding: 12px;
  border: 1px solid #ccc;
}
.initialized {
  border-color: #42a5f5;
}
```

## ベストプラクティス
- 参照が存在しない場合に備え、アクセス前にnullチェックを行う
- テンプレート参照変数には意味のある名前を付け、コードとの関連を明確にする
- ViewChildを増やしすぎるとテンプレート依存が深くなるため、必要最小限に留める

## 注意点
- `static: true`を指定しない限り、`ngOnInit`では参照が取得できない
- Template構文の*ngIfなどでDOMが切り替わると参照がnullになる場合がある
- 直接DOM操作をする場合はSSRへの影響を考慮する

## 関連技術
- `@ViewChild`オプション（static, read）
- `@ContentChild`との違い
- Renderer2による安全なDOM操作
