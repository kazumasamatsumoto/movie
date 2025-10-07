# #002 「CLI で Component 作成 - ng generate component」

## 概要
Angular CLIを使ったComponentの自動生成方法を学びます。ng generate componentコマンドで、必要なファイルを一括作成できます。

## 学習目標
- ng generate componentコマンドの使い方を習得する
- 自動生成されるファイルを理解する
- Standalone Componentの作成方法を学ぶ

## 技術ポイント
- **ng generate component**: Component自動生成コマンド
- **--standalone**: Standalone Component作成オプション
- **省略形**: ng g c で簡略化可能

## 📺 画面表示用コード（動画用）
**表示ルール**: 最大3個、各10行以内、動画で見せる部分のみ

```bash
# 基本的なComponent作成
ng generate component user
# または省略形
ng g c user
```

```bash
# Standalone Componentを作成（v20推奨）
ng g c user --standalone

# 生成されるファイル
# user.component.ts
# user.component.html
# user.component.css
# user.component.spec.ts
```

```bash
# インラインテンプレート/スタイルで作成
ng g c button --inline-template --inline-style
# 省略形
ng g c button -t -s
```

## 💻 詳細実装例（学習用）

### 基本的なComponent生成
```bash
# 通常のComponent生成
ng generate component components/user-profile

# 生成されるファイル構成
# src/app/components/user-profile/
#   ├── user-profile.component.ts
#   ├── user-profile.component.html
#   ├── user-profile.component.css
#   └── user-profile.component.spec.ts
```

生成されたComponent例:
```typescript
// user-profile.component.ts
import { Component } from '@angular/core';

@Component({
  selector: 'app-user-profile',
  templateUrl: './user-profile.component.html',
  styleUrls: ['./user-profile.component.css']
})
export class UserProfileComponent {}
```

### Standalone Componentの生成
```bash
# Standalone Componentとして生成
ng g c components/card --standalone

# 既存のモジュールに追加しない
ng g c components/header --standalone --skip-import
```

生成されたStandalone Component例:
```typescript
// card.component.ts
import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-card',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './card.component.html',
  styleUrls: ['./card.component.css']
})
export class CardComponent {}
```

### インラインテンプレート/スタイル
```bash
# インラインテンプレートとスタイルで生成
ng g c components/button --inline-template --inline-style --standalone
```

生成されたインラインComponent例:
```typescript
// button.component.ts
import { Component } from '@angular/core';

@Component({
  selector: 'app-button',
  standalone: true,
  template: `
    <button>
      Click me
    </button>
  `,
  styles: [`
    button {
      padding: 8px 16px;
      background-color: #007bff;
      color: white;
      border: none;
      border-radius: 4px;
      cursor: pointer;
    }
  `]
})
export class ButtonComponent {}
```

### よく使うオプション組み合わせ
```bash
# テストファイルなしで作成
ng g c components/navbar --skip-tests --standalone

# フラットな構造（フォルダ作成なし）
ng g c simple-card --flat --standalone

# プレフィックスをカスタマイズ
ng g c custom-button --prefix=custom --standalone

# 変更検知戦略を指定
ng g c optimized-list --change-detection=OnPush --standalone

# すべてインラインでテストなし
ng g c icon --inline-template --inline-style --skip-tests --standalone
```

### 複数Component一括生成スクリプト
```bash
# components.sh
#!/bin/bash

components=(
  "header"
  "footer"
  "sidebar"
  "main-content"
  "navigation"
)

for component in "${components[@]}"
do
  ng g c "components/$component" --standalone --skip-tests
done
```

### angular.jsonでデフォルト設定
```json
{
  "schematics": {
    "@schematics/angular:component": {
      "standalone": true,
      "style": "scss",
      "skipTests": false,
      "inlineTemplate": false,
      "inlineStyle": false,
      "changeDetection": "OnPush"
    }
  }
}
```

この設定により、以下のコマンドでデフォルトでStandalone Componentが生成される:
```bash
ng g c user  # 自動的に--standaloneが適用される
```

## ベストプラクティス

1. **Standalone Componentを標準化**: v20では--standaloneを推奨
2. **適切なディレクトリ構造**: 機能ごとにフォルダ分け
3. **命名規則の統一**: ケバブケースで明確な名前
4. **デフォルト設定の活用**: angular.jsonで一括設定

## 注意点

- Component名はケバブケースで指定
- パスを指定すると自動的にフォルダが作成される
- --standaloneオプションは明示的に指定（v20推奨）
- 既存ファイルの上書きに注意

## 関連技術
- Angular CLI
- Schematics
- Workspace Configuration
- File Structure Best Practices
