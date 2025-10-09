# #093 「@Input() 必須プロパティ - required」

## 概要
Angular v16以降で利用できる`@Input({ required: true })`を使い、親が必ず値を提供しなければならない必須プロパティを定義する方法を学びます。

## 学習目標
- requiredオプションの構文を理解する
- 親が未設定の場合に発生するエラーを確認する
- テンプレートでの型安全性を高める

## 技術ポイント
- **requiredオプション**: `@Input({ required: true }) field!: Type;`
- **ビルド時検査**: 親テンプレートで未指定だとコンパイル時にエラー
- **null安全**: 非nullアサーション`!`と組み合わせて初期化不要にできる


```typescript
@Input({ required: true }) title!: string;
```

```html
<app-section [title]="sectionTitle"></app-section>
```

```html
<!-- 未指定の場合はテンプレートエラー -->
```

## 💻 詳細実装例（学習用）
```typescript
// section.component.ts
import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-section',
  standalone: true,
  templateUrl: './section.component.html',
})
export class SectionComponent {
  @Input({ required: true })
  title!: string;

  @Input()
  description = '';
}
```

```html
<!-- section.component.html -->
<section class="card">
  <h3>{{ title }}</h3>
  <p>{{ description }}</p>
</section>
```

```typescript
// parent.component.ts
import { Component } from '@angular/core';
import { SectionComponent } from './section.component';

@Component({
  selector: 'app-dashboard',
  standalone: true,
  imports: [SectionComponent],
  templateUrl: './dashboard.component.html',
})
export class DashboardComponent {
  featureTitle = '最新レポート';
}
```

```html
<!-- dashboard.component.html -->
<app-section
  [title]="featureTitle"
  description="レポートをチェックしましょう"
></app-section>
```

## ベストプラクティス
- 必須プロパティに対して`@Input({ required: true })`を設定し、契約をコードで表現する
- 非nullアサーションを併用すると、コンパイラが「必ず値が入る」ことを認識できる
- 必須項目にはコメントやドキュメントを添え、親側の開発者が迷わないようにする

## 注意点
- required指定してもランタイムでnullが入るケースは防げないため、バリデーションは別途必要
- Angular v16未満では利用できないため、プロジェクトのバージョンを確認する
- テスト環境でも必須Inputを忘れるとテストが失敗するので、Fixture作成時に注意する

## 関連技術
- TypeScriptのstrictNullChecks
- Angular Template type checking
- ESLintルール `@angular-eslint/no-inputs-metadata-property`
