# #052 「[(ngModel)] FormsModule のインポート」

## 概要
[(ngModel)]を利用するために必要なFormsModuleの登録方法と、Standalone構成での依存解決パターンを整理します。

## 学習目標
- FormsModuleをStandalone Componentにインポートする手順を理解する
- provideForms()を用いたブートストラップ構成を把握する
- 未登録時に発生するエラーの根本原因を説明できるようにする

## 技術ポイント
- **FormsModule**: Template-driven Forms機能一式を提供するAngularモジュール
- **Standalone imports**: `imports: [FormsModule]`でコンポーネントごとに依存を宣言
- **provideForms()**: アプリ全体にTemplate-driven Formsを提供するプロバイダー

## 📺 画面表示用コード（動画用）
**表示ルール**: 最大3個、各10行以内、動画で見せる部分のみ

```typescript
import { FormsModule } from '@angular/forms';
```

```typescript
@Component({
  imports: [FormsModule],
  standalone: true,
  template: `<input [(ngModel)]="name" />`,
})
```

```typescript
bootstrapApplication(AppComponent, {
  providers: [provideForms()],
});
```

## 💻 詳細実装例（学習用）
```typescript
// app.component.ts
import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [FormsModule],
  templateUrl: './app.component.html',
})
export class AppComponent {
  name = 'ずんだもん';
}
```

```typescript
// main.ts
import { bootstrapApplication } from '@angular/platform-browser';
import { provideForms } from '@angular/forms';
import { AppComponent } from './app.component';

bootstrapApplication(AppComponent, {
  providers: [provideForms()],
});
```

```html
<!-- app.component.html -->
<label>
  名前
  <input [(ngModel)]="name" />
</label>
<p>こんにちは、{{ name }}さん！</p>
```

## ベストプラクティス
- Standalone構成では必要なモジュールをコンポーネントごとに明示して依存を最小化する
- provideForms()をルートに設定するとサブコンポーネントでの再インポートが不要になる
- CLIで新規プロジェクトを作成する場合は`--standalone`オプションで軽量構成を選ぶ

## 注意点
- FormsModuleを登録していないと`NG0303: Can't bind to 'ngModel'`エラーが発生する
- Reactive Formsのみ利用する場合は`ReactiveFormsModule`を選び、ngModelと混在させない
- provideForms()を二重指定するとインジェクターが冗長になるため構成を整理する

## 関連技術
- Template-driven Forms と Reactive Forms の使い分け
- Standalone Component の依存宣言
- provideHttpClient などの新しいプロバイダー登録パターン
