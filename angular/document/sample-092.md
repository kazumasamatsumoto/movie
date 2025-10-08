# #092 「@Input() の基本構文」

## 概要
@Input()の宣言方法と、子コンポーネントで複数の入力プロパティを定義する基本構文を確認します。

## 学習目標
- @Input()デコレータの書き方を理解する
- 初期値や型注釈の付け方を習得する
- Standalone Componentでのimportsの考え方を確認する

## 技術ポイント
- **デコレータ構文**: `@Input() propertyName: Type = default;`
- **複数定義**: プロパティごとに@Input()を付与
- **テンプレート同期**: 親テンプレートでのプロパティバインディングと対になる

## 📺 画面表示用コード（動画用）
**表示ルール**: 最大3個、各10行以内、動画で見せる部分のみ

```typescript
@Input() title = '';
@Input() subtitle?: string;
```

```html
<app-header
  [title]="pageTitle"
  [subtitle]="pageSubtitle"
></app-header>
```

```typescript
// 受け側はクラスフィールドに定義する
```

## 💻 詳細実装例（学習用）
```typescript
// app-header.component.ts
import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-header',
  standalone: true,
  templateUrl: './app-header.component.html',
})
export class AppHeaderComponent {
  @Input() title = '';
  @Input() subtitle: string | null = null;
  @Input() showDivider = true;
}
```

```html
<!-- app-header.component.html -->
<header class="page-header">
  <h1>{{ title }}</h1>
  <p *ngIf="subtitle">{{ subtitle }}</p>
  <hr *ngIf="showDivider" />
</header>
```

```typescript
// parent.component.ts
import { Component } from '@angular/core';
import { AppHeaderComponent } from './app-header.component';

@Component({
  selector: 'app-page',
  standalone: true,
  imports: [AppHeaderComponent],
  template: `
    <app-header
      [title]="title"
      [subtitle]="description"
      [showDivider]="false"
    ></app-header>
  `,
})
export class PageComponent {
  title = 'Angular Inputs';
  description = '子コンポーネントに値を渡す基本構文';
}
```

## ベストプラクティス
- プロパティ名はlowerCamelCaseで宣言し、テンプレートではkebab-caseに自動変換される点を理解する
- undefinedを許容する場合は明示的に型へ`| undefined`を含め、利用側でガードを書く
- 初期値を設定しておくと親が未設定でも安全に描画できる

## 注意点
- `@Input() property!: Type;` と`!`で初期化を抑制する場合でも、親が必ず渡す設計か確認する
- 複数の@Input()を宣言する順番に意味はないが、カテゴリごとに並べると可読性が高い
- StandaloneでないModule構成でも同様に動くが、importsで子を宣言することを忘れない

## 関連技術
- TypeScriptのDefinitely Assigned Assertions (`!`)
- Template syntaxのプロパティバインディング
- ESLintルール `@angular-eslint/no-input-rename`
