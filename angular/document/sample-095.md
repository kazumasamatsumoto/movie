# #095 「@Input() エイリアス指定」

## 概要
公開プロパティ名と内部プロパティ名を分離するための@Input()エイリアス機能を紹介し、API互換性を保ちながらリファクタする方法を学びます。

## 学習目標
- エイリアスの付け方と親テンプレートからの参照方法を理解する
- 内部プロパティ名を変えても外部APIを保つテクニックを習得する
- ESLintルールとの整合性に注意するポイントを把握する

## 技術ポイント
- **エイリアス構文**: `@Input('appTitle') title!: string;`
- **公開API管理**: 外部からはエイリアス名でアクセス
- **リネーム戦略**: 内部実装と公開名を切り離し、段階的移行が可能

## 📺 画面表示用コード（動画用）
**表示ルール**: 最大3個、各10行以内、動画で見せる部分のみ

```typescript
@Input('appTitle') title!: string;
```

```html
<app-header [appTitle]="pageTitle"></app-header>
```

```html
<!-- 親はエイリアス名のみを意識する -->
```

## 💻 詳細実装例（学習用）
```typescript
// header.component.ts
import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-header',
  standalone: true,
  templateUrl: './header.component.html',
})
export class HeaderComponent {
  @Input('appTitle')
  title = '';

  @Input('appSubtitle')
  subtitle?: string;
}
```

```html
<!-- header.component.html -->
<header class="app-header">
  <h1>{{ title }}</h1>
  <p *ngIf="subtitle">{{ subtitle }}</p>
</header>
```

```typescript
// parent.component.ts
import { Component } from '@angular/core';
import { HeaderComponent } from './header.component';

@Component({
  selector: 'app-root-page',
  standalone: true,
  imports: [HeaderComponent],
  template: `
    <app-header
      [appTitle]="title"
      [appSubtitle]="subtitle"
    ></app-header>
  `,
})
export class RootPageComponent {
  title = 'Angularのエイリアス活用';
  subtitle = '公開APIと内部名を分離する';
}
```

## ベストプラクティス
- 外部向けAPIを定義するときはエイリアス名を慎重に選び、ドキュメントで公開する
- 内部プロパティ名は意味のある命名にし、リファクタ時はエイリアスで互換性を保つ
- ESLintの`no-input-rename`を無効化するか設定を調整して、エイリアス使用時でも警告が出ないようにする

## 注意点
- エイリアス名はテンプレートでkebab-caseに変換されるため、衝突しないようにする
- エイリアスを付けるとプロパティのデコレータ引数が文字列になるため、リネーム時にIDEリファクタが効かない場合がある
- API移行が完了したら古いエイリアスを削除し、コードをクリーンに保つ

## 関連技術
- ESLint `@angular-eslint/no-input-rename`
- Angular Style Guide（Input/Output命名規約）
- deprecationパターンと段階的移行戦略
