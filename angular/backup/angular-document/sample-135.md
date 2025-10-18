# #135 「ViewChild ディレクティブ参照」

## 概要
テンプレート上のディレクティブインスタンスへ`@ViewChild`でアクセスし、ディレクティブが提供するAPIを親コンポーネントから利用する方法を学びます。

## 学習目標
- ディレクティブ型を指定したViewChildの書き方を理解する
- `read`オプションを使った参照方法を習得する
- ディレクティブの公開プロパティ・メソッドを親が安全に操作する手順を学ぶ

## 技術ポイント
- **型指定**: `@ViewChild(MyDirective) dir?: MyDirective;`
- **テンプレート参照**: `<div myDirective></div>`
- **readオプション**: 同一要素で異なる型を取得したい場合に利用

```html
<div myHighlight></div>
```

```typescript
@ViewChild(MyHighlightDirective)
highlight?: MyHighlightDirective;
```

```typescript
this.highlight?.setColor('#ff7043');
```

## 💻 詳細実装例（学習用）
```typescript
// my-highlight.directive.ts
import { Directive, ElementRef, Input } from '@angular/core';

@Directive({
  selector: '[myHighlight]',
  standalone: true,
})
export class MyHighlightDirective {
  @Input() myHighlight = '#ffee58';

  constructor(private readonly elementRef: ElementRef<HTMLElement>) {}

  setColor(color: string): void {
    this.elementRef.nativeElement.style.backgroundColor = color;
  }
}
```

```typescript
// host.component.ts
import { AfterViewInit, Component, ViewChild } from '@angular/core';
import { MyHighlightDirective } from './my-highlight.directive';

@Component({
  selector: 'app-host',
  standalone: true,
  imports: [MyHighlightDirective],
  templateUrl: './host.component.html',
})
export class HostComponent implements AfterViewInit {
  @ViewChild(MyHighlightDirective)
  highlight?: MyHighlightDirective;

  ngAfterViewInit(): void {
    this.highlight?.setColor('#64b5f6');
  }

  update(): void {
    this.highlight?.setColor('#ff8a65');
  }
}
```

```html
<!-- host.component.html -->
<div myHighlight>ディレクティブ参照のデモ</div>
<button type="button" (click)="update()">色を変更</button>
```

## ベストプラクティス
- 親が利用するメソッドはディレクティブ側でpublicとして提供し、コメントで用途を明記する
- 同じ要素に複数ディレクティブがある場合は`{ read: MyDirective }`で意図した型を取得する
- テストではホストコンポーネントを用意し、ディレクティブの公開APIを検証する

## 注意点
- ディレクティブが非表示・破棄されると参照がnullになるため、nullチェックを徹底する
- ElementRefを直接操作するメソッドを公開する場合はSSR対応を考慮する
- 複数のViewChildで同じディレクティブを参照すると管理が複雑になるので構造を整理する

## 関連技術
- `@Directive`による機能拡張
- `@ViewChildren`で複数ディレクティブを取得
- Renderer2での安全なDOM操作
