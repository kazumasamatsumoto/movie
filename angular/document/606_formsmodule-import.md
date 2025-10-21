# #606 「FormsModule のインポート」

## 概要
テンプレート駆動フォームを利用するにはFormsModuleをインポートし、コンポーネントやNgModuleのimportsに登録する必要がある。

## 学習目標
- FormsModuleをインポートする場所を理解する
- スタンドアロンとNgModuleの書き方の違いを把握する
- モジュール共有戦略をイメージする

## 技術ポイント
- @angular/formsからFormsModuleをインポート
- スタンドアロンでは@Componentのimportsに追加
- NgModule方式ではimports配列で共有モジュール化可能

## 📺 画面表示用コード（動画用）
```typescript
import { FormsModule } from '@angular/forms';
```

```typescript
@Component({
  standalone: true,
  imports: [FormsModule]
})
```

## 💻 詳細実装例（学習用）
```typescript
@Component({
  selector: 'app-template-form',
  templateUrl: './template-form.component.html',
  standalone: true,
  imports: [CommonModule, FormsModule]
})
export class TemplateFormComponent {}
```

## ベストプラクティス
- フォーム関連の共有モジュールを作成し再利用しやすくする
- Importsの追加はスキャフォールディングスクリプトで自動化する
- レビュー時にフォームディレクティブの利用有無を確認する

## 注意点
- FormsModuleを追加しないとngModelが解決できずテンプレートが壊れる
- 不要な画面にFormsModuleを読み込むとバンドルサイズが増える
- NgModuleとスタンドアロンの両方で記述が重複しないよう整理する

## 関連技術
- @angular/forms
- Standalone Components
- SharedModule設計
