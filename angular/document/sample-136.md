# #136 「ViewChild read オプション」

## 概要
`@ViewChild`の`read`オプションを使い、同じ要素に関連する異なる型（ElementRef、ディレクティブ、テンプレート等）を選択的に取得する方法を学びます。

## 学習目標
- `read`オプションの役割と構文を理解する
- ディレクティブ・テンプレート・DOM要素を使い分けて取得する
- 複数のViewChild参照が必要なケースに対応する

## 技術ポイント
- **基本構文**: `@ViewChild('input', { read: ElementRef })`
- **ディレクティブ取得**: `@ViewChild(MyDirective, { read: MyDirective })`
- **Renderer2併用**: ElementRefを取得した後はRenderer2で操作するのが安全

## 📺 画面表示用コード（動画用）

```html
<input #field myInputDirective />
```

```typescript
@ViewChild('field', { read: ElementRef })
fieldElement?: ElementRef<HTMLInputElement>;
```

```typescript
@ViewChild('field', { read: MyInputDirective })
fieldDirective?: MyInputDirective;
```

## 💻 詳細実装例（学習用）
```typescript
// my-input.directive.ts
import { Directive, ElementRef } from '@angular/core';

@Directive({
  selector: '[myInputDirective]',
  standalone: true,
})
export class MyInputDirective {
  constructor(private readonly elementRef: ElementRef<HTMLInputElement>) {}

  focus(): void {
    this.elementRef.nativeElement.focus();
  }
}
```

```typescript
// form.component.ts
import { AfterViewInit, Component, ElementRef, ViewChild } from '@angular/core';
import { MyInputDirective } from './my-input.directive';

@Component({
  selector: 'app-form',
  standalone: true,
  imports: [MyInputDirective],
  templateUrl: './form.component.html',
})
export class FormComponent implements AfterViewInit {
  @ViewChild('nameField', { read: ElementRef })
  nameInput?: ElementRef<HTMLInputElement>;

  @ViewChild('nameField', { read: MyInputDirective })
  nameDirective?: MyInputDirective;

  ngAfterViewInit(): void {
    this.nameDirective?.focus();
  }

  clear(): void {
    if (this.nameInput) {
      this.nameInput.nativeElement.value = '';
    }
  }
}
```

```html
<!-- form.component.html -->
<input #nameField myInputDirective placeholder="名前" />
<button type="button" (click)="clear()">クリア</button>
```

## ベストプラクティス
- 同じ要素から複数の型を取得する場合、ViewChildに`read`を明示して意図を伝える
- ElementRefを取得した場合でも、可能な操作はディレクティブ経由で提供する
- テンプレートを取得したい場合は`{ read: TemplateRef }`を利用する

## 注意点
- readオプションを指定しない場合、Angularはディレクティブ→コンポーネント→ElementRefの優先順で解決する
- SSRではElementRefが存在しないので、ブラウザ環境でのみ使用するコードにガードを入れる
- `read`の型と実際の参照が一致しない場合はnullが返るため、nullチェックを行う

## 関連技術
- TemplateRefとViewContainerRef
- Renderer2によるDOM操作
- `@ViewChildren`のreadオプション
